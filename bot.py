from web3 import Web3
import time
from colorama import Fore, Style, init
import datetime
import requests

# Inisialisasi colorama
init(autoreset=True)

# RPC URL dan WETH contract address
RPC_URL = "https://rpc.ankr.com/taiko"
WETH_CONTRACT_ADDRESS = "0xA51894664A773981C6C112C43ce576f315d5b1B6"

# Baca private key dari file
with open('pvkey.txt', 'r') as f:
    PRIVATE_KEY = f.read().strip()

# Telegram bot info
TELEGRAM_BOT_TOKEN = "7482058034:AAGnXDqvNVOZ5gle4Jw0YOMjG6JD4KnP1KI"
TELEGRAM_CHAT_ID = "6644783233"

# Koneksi ke jaringan Taiko
web3 = Web3(Web3.HTTPProvider(RPC_URL))
account = web3.eth.account.from_key(PRIVATE_KEY)
address = account.address

# ABI ERC20 standar
erc20_abi = [
    {
        "constant": True,
        "inputs": [{"name": "owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "deposit",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [{"name": "wad", "type": "uint256"}],
        "name": "withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# Load contract WETH
weth_contract = web3.eth.contract(address=WETH_CONTRACT_ADDRESS, abi=erc20_abi)

# Fungsi untuk mendapatkan saldo ETH dan WETH
def get_balances():
    eth_balance = web3.eth.get_balance(address)
    weth_balance = weth_contract.functions.balanceOf(address).call()
    return web3.from_wei(eth_balance, 'ether'), web3.from_wei(weth_balance, 'ether')

# Fungsi untuk mendapatkan gas price dinamis (nilai tetap)
def get_fixed_gas_price():
    return web3.to_wei(0.050000001, 'gwei')

# Fungsi untuk mengirim transaksi
def send_transaction(transaction):
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

    # Tunggu hingga transaksi terkonfirmasi
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash

# Fungsi untuk melakukan wrapping ETH ke WETH
def wrap_eth_to_weth(amount):
    gas_price = get_fixed_gas_price()
    transaction = weth_contract.functions.deposit().build_transaction({
        'from': address,
        'value': web3.to_wei(amount, 'ether'),
        'nonce': web3.eth.get_transaction_count(address),
        'gas': 70000,
        'gasPrice': gas_price
    })
    tx_hash = send_transaction(transaction)
    print(f"{Fore.GREEN}Transaksi wrap {amount} ETH ke WETH (Tx Hash: {tx_hash.hex()})")

# Fungsi untuk melakukan unwrapping WETH ke ETH
def unwrap_weth_to_eth(amount):
    gas_price = get_fixed_gas_price()
    transaction = weth_contract.functions.withdraw(web3.to_wei(amount, 'ether')).build_transaction({
        'from': address,
        'nonce': web3.eth.get_transaction_count(address),
        'gas': 70000,
        'gasPrice': gas_price
    })
    tx_hash = send_transaction(transaction)
    print(f"{Fore.GREEN}Transaksi unwrap {amount} WETH ke ETH (Tx Hash: {tx_hash.hex()})")

# Fungsi untuk mengirim notifikasi ke Telegram
def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

# Fungsi untuk menunggu hingga jam 7 pagi
def wait_until_morning():
    now = datetime.datetime.now()
    target = now.replace(hour=7, minute=0, second=0, microsecond=0)
    
    # Jika waktu sekarang lebih besar dari jam 7 pagi, set target untuk besok pagi
    if now > target:
        target += datetime.timedelta(days=1)
    
    wait_time = (target - now).total_seconds()
    print(f"{Fore.YELLOW}Maksimum transaksi tercapai. Menunggu hingga jam 7 pagi...")
    time.sleep(wait_time)

# Fungsi utama untuk pengecekan saldo dan wrap/unwrap otomatis
def auto_wrap_unwrap():
    last_wrap_amount = 0  # Untuk menyimpan jumlah terakhir yang di-wrap
    unwrap_count = 0
    max_unwrap_count = 104

    while True:
        eth_balance, weth_balance = get_balances()
        print(f"{Fore.CYAN}Saldo ETH: {eth_balance} | Saldo WETH: {weth_balance}")
        
        if eth_balance > weth_balance:
            # Wrap 90% dari saldo ETH
            wrap_amount = eth_balance * 0.9
            last_wrap_amount = wrap_amount  # Simpan jumlah yang di-wrap
            print(f"{Fore.YELLOW}Saldo ETH lebih banyak. Melakukan wrap {wrap_amount} ETH ke WETH...")
            wrap_eth_to_weth(wrap_amount)
        elif weth_balance > eth_balance and last_wrap_amount > 0 and unwrap_count < max_unwrap_count:
            # Unwrap jumlah yang sama dengan wrap terakhir
            print(f"{Fore.YELLOW}Saldo WETH lebih banyak. Melakukan unwrap {last_wrap_amount} WETH ke ETH...")
            unwrap_weth_to_eth(last_wrap_amount)
            unwrap_count += 1
            last_wrap_amount = 0  # Reset setelah unwrap
            print(f"{Fore.CYAN}Jumlah unwrap: {unwrap_count} dari {max_unwrap_count}")
        else:
            print(f"{Fore.YELLOW}Saldo ETH dan WETH seimbang. Tidak ada tindakan yang diperlukan.")
        
        # Cek apakah sudah mencapai batas maksimum unwrap
        if unwrap_count >= max_unwrap_count:
            eth_balance, _ = get_balances()
            message = f"Unwrap telah mencapai 104 kali. Saldo ETH saat ini: {eth_balance} ETH."
            send_telegram_notification(message)
            wait_until_morning()
            unwrap_count = 0  # Reset counter setelah menunggu hingga pagi

        time.sleep(60)  # Jeda antar pengecekan saldo

if __name__ == "__main__":
    auto_wrap_unwrap()

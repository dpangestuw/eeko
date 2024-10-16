from web3 import Web3, exceptions
import time
from colorama import Fore, Style, init
import datetime
from decimal import Decimal
import requests

print(Fore.GREEN + "░▒▓████████▓▒░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░" + Style.RESET_ALL)
print(Fore.GREEN + "   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░" + Style.RESET_ALL)
print(Fore.GREEN + "   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░" + Style.RESET_ALL)
print(Fore.GREEN + "   ░▒▓█▓▒░  ░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░" + Style.RESET_ALL)
print(Fore.GREEN + "   ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░" + Style.RESET_ALL)
print(Fore.GREEN + "   ░▒▓█▓▒░  ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░" + Style.RESET_ALL)
print(Fore.GREEN + "t.me/dpangestuw31" + Style.RESET_ALL)

# Inisialisasi colorama
init(autoreset=True)

# RPC URL dan WETH contract address
RPC_URL = "https://rpc.ankr.com/taiko"
WETH_CONTRACT_ADDRESS = "0xA51894664A773981C6C112C43ce576f315d5b1B6"

# Baca private key dari file
with open('pvkey.txt', 'r') as f:
    PRIVATE_KEY = f.read().strip()

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

# Fungsi untuk mendapatkan gas price dinamis
def get_fixed_gas_price():
    return web3.to_wei(Decimal("0.050000001"), 'gwei')

# Fungsi untuk mengirim transaksi dan menangani kesalahan dengan retry
def send_transaction_with_retry(transaction, max_retries=3, delay=60):
    retries = 0
    while retries < max_retries:
        try:
            signed_txn = web3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
            
            # Tunggu transaksi dikonfirmasi
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
            return tx_hash  # Jika berhasil, return hash transaksi
        except web3.exceptions.TimeExhausted:
            retries += 1
            print(f"Transaksi tidak ditemukan di chain setelah 120 detik. Mencoba ulang ({retries}/{max_retries})...")
            time.sleep(delay)  # Tunggu sebelum mencoba ulang
    raise Exception("Transaksi gagal setelah beberapa kali percobaan")

# Fungsi untuk melakukan wrapping ETH ke WETH
def wrap_eth_to_weth(amount, gas_price):
    transaction = weth_contract.functions.deposit().build_transaction({
        'from': address,
        'value': web3.to_wei(amount, 'ether'),
        'nonce': web3.eth.get_transaction_count(address),
        'gas': 70000,
        'gasPrice': gas_price
    })

    tx_hash = send_transaction_with_retry(transaction)
    print(f"{Fore.GREEN}Transaksi wrap {amount} ETH ke WETH (Tx Hash: {tx_hash.hex()}, Gas Price: {web3.from_wei(gas_price, 'gwei')} gwei)")

# Fungsi untuk melakukan unwrapping WETH ke ETH
def unwrap_weth_to_eth(amount, gas_price):
    transaction = weth_contract.functions.withdraw(web3.to_wei(amount, 'ether')).build_transaction({
        'from': address,
        'nonce': web3.eth.get_transaction_count(address),
        'gas': 70000,
        'gasPrice': gas_price
    })

    tx_hash = send_transaction_with_retry(transaction)
    print(f"{Fore.GREEN}Transaksi unwrap {amount} WETH ke ETH (Tx Hash: {tx_hash.hex()}, Gas Price: {web3.from_wei(gas_price, 'gwei')} gwei)")

# Fungsi untuk mengirim notifikasi ke Telegram
def send_telegram_notification(message):
    telegram_token = "6405568722:AAHijXOLIOAwiR5vhrhn7qlN4bITPb3tbB4"  # Ganti dengan token bot Telegram Anda
    telegram_chat_id = "6644783233"  # Ganti dengan chat ID Anda
    url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
    payload = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(f"{Fore.GREEN}Notifikasi terkirim ke Telegram: {message}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Gagal mengirim notifikasi: {e}")

# Fungsi untuk menunggu hingga jam 7 pagi
def wait_until_morning():
    now = datetime.datetime.now()
    target = now.replace(hour=7, minute=0, second=0, microsecond=0)
    
    if now > target:
        target += datetime.timedelta(days=1)
    
    wait_time = (target - now).total_seconds()
    print(f"{Fore.YELLOW}Maksimum transaksi tercapai. Menunggu hingga jam 7 pagi...")
    time.sleep(wait_time)

# Fungsi utama untuk melakukan wrap dan unwrap
def auto_wrap_unwrap():
    wrap_count = 0
    unwrap_count = 0
    max_transactions = 2

    while True:
        eth_balance, weth_balance = get_balances()
        print(f"{Fore.CYAN}Saldo ETH: {eth_balance} | Saldo WETH: {weth_balance}")
        gas_price = get_fixed_gas_price()

        # Wrap jika saldo ETH lebih besar
        if eth_balance > weth_balance and wrap_count < max_transactions:
            amount_to_wrap = eth_balance * Decimal("0.90")  # 90% dari saldo ETH
            wrap_eth_to_weth(amount_to_wrap, gas_price)
            wrap_count += 1
            print(f"{Fore.CYAN}Wrap sukses: {wrap_count} dari {max_transactions}")
        
        # Unwrap jika saldo WETH lebih besar
        elif weth_balance > eth_balance and unwrap_count < max_transactions:
            unwrap_weth_to_eth(amount_to_wrap, gas_price)  # Unwrap jumlah yang sama
            unwrap_count += 1
            print(f"{Fore.CYAN}Unwrap sukses: {unwrap_count} dari {max_transactions}")
        
        # Jika sudah mencapai batas maksimum transaksi unwrap
        if unwrap_count >= max_transactions:
            send_telegram_notification(f"Batas maksimum transaksi unwrap tercapai. Saldo ETH: {eth_balance} ETH.")
            wait_until_morning()  # Tunggu hingga jam 7 pagi sebelum melanjutkan
            unwrap_count = 0  # Reset counter unwrap setelah menunggu
            
        time.sleep(10)  # Tunggu sebelum loop berikutnya

if __name__ == "__main__":
    auto_wrap_unwrap()

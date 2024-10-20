<img height="250" alt="EEKO" src="https://github.com/user-attachments/assets/698730c4-c0e6-498f-a3ee-8ab757de3fb4"> <img height="250" alt="Notif Tele" src="https://github.com/user-attachments/assets/de45b100-690e-44ef-b34f-fc9362ab3921">


## Deskripsi

Dalam bahasa Jawa, kata "tai" memiliki arti kotor, sehingga untuk menjaga kesopanan dan kebersihan, kata tersebut diganti dengan "ee."


## Fitur

- **eeko.VDIN** : Versi Wrap/Unwrap TAIKO untuk gwei dinamis. Otomatis berhenti Wrap/Unwrap saat mencapai maksimal fee *"total_transaction_fee"*.

- **eeko.VINC** : Versi Wrap/Unwrap TAIKO untuk kenaikan gwei, dimulai dari *"min_gwei"* dengan kelipatan *"gwei_increment"* dengan maksimal gwei *"max_gwei"*. Otomatis berhenti Wrap/Unwrap saat mencapai maksimal fee *"total_transaction_fee"*.

- **eeko** : Versi Wrap/Unwrap TAIKO untuk fix gwei *"gwei"*. Otomatis berhenti Wrap/Unwrap saat mencapai transaksi max *"max_transactions"*.

- **Custom JSON**: Pengguna dapat menentukan memodifikasi nilai masing-masing.
  
- **Notifikasi Transaksi**: Sistem akan mengirimkan notifikasi melalui Telegram ketika transaksi selesai atau jika terjadi kesalahan selama proses transaksi. *Hanya lisensi yang di dapat dari bot*

- [**Get License and Notifikasi**](https://t.me/Laporan_Sayang_bot)

## Instalasi

   ```bash
   git clone https://github.com/dpangestuw/eeko.git
   ```
   ```bash
   pip install web3 requests colorama
   ```
   ```bash
   cd eeko
   ```
   ```bash
   python3 eeko.py
   ```
**create pvkey.txt and input your privatekey**

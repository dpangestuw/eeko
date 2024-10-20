
## Deskripsi

Dalam bahasa Jawa, kata "tai" memiliki arti kotor, sehingga untuk menjaga kesopanan dan kebersihan, kata tersebut diganti dengan "ee."

<details>
<summary><strong>Screenshots</strong></summary>

![EEKO.VINC](https://github.com/user-attachments/assets/2dfaca39-93f8-4eb1-a68c-28bd05da7c92)

![EEKO.VDIN](https://github.com/user-attachments/assets/5b447a88-2740-4d7d-939a-d6b9c1a46f0f)

![EEKO](https://github.com/user-attachments/assets/eed3936e-1b72-49b5-9cf6-0e684541f543)

</details>

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

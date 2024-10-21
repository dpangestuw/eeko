
## Deskripsi

Dalam bahasa Jawa, kata "tai" memiliki arti kotor, sehingga untuk menjaga kesopanan dan kebersihan, kata tersebut diganti dengan "ee."

<details>
<summary><strong>Screenshots</strong></summary>

<img height="311" alt="image" src="https://github.com/user-attachments/assets/2dfaca39-93f8-4eb1-a68c-28bd05da7c92">
<img height="311" alt="image" src="https://github.com/user-attachments/assets/5b447a88-2740-4d7d-939a-d6b9c1a46f0f">
<img height="415" alt="image" src="https://github.com/user-attachments/assets/8b81c702-8082-4ef1-aaf7-55aa80946e73">

</details>

## Fitur

- **eeko.VDIN** : Versi EEKO dengan gwei dinamis. Otomatis berhenti Wrap/Unwrap saat mencapai *total_transaction_fee*.

- **eeko.VINC** : Versi EEKO dengan kenaikan gwei yang dimulai dari *min_gwei* dengan kelipatan *gwei_increment* dengan *max_gwei*. Otomatis berhenti Wrap/Unwrap saat mencapai *total_transaction_fee*.

- **eeko.VUP** : Versi EEKO dengan gwei dinamis. Namun akan ada peningkatan 0.0005 apabila melebihi batas waktu, dengan maksimal +0.005 dari gwei jaringan. OOtomatis berhenti Wrap/Unwrap saat mencapai *total_transaction_fee*. **(Recommended)**

- **Anda bisa melanjutkan tx apabila terjadi gangguan, sesuai total tx fee terakhir** Misal total terakhir 0.00003
  ```bash
  python eeko.VDIN.py --fee 0.00003
  ```

- **Custom JSON**: Pengguna dapat memodifikasi nilai variabel yang dicetak miring sesuai versi EEKO. 
  
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

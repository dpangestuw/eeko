
## Description

In Javanese, the word "tai" means dirty, so to maintain politeness and cleanliness, it is replaced with "ee."
That’s why this program is named **"EEKO"** instead of **"TAIKO."**

## Screenshots
<details>
<summary><strong>View Details</strong></summary>
   
<img width="500" alt="image" src="https://github.com/user-attachments/assets/acb01157-39b1-4893-96b7-393b9bfacb39">
<img width="500" alt="image" src="https://github.com/user-attachments/assets/eac6e6d3-d536-476d-b100-b4e0f320d8bd">
<img width="311" alt="image" src="https://github.com/user-attachments/assets/26e0c02c-1f44-4379-a786-63e8c138535f">


</details>

## Fitur EEKO

- **Automatic Count and Fee Tracking**: The system saves transaction counts and total fees, allowing you to resume transactions seamlessly.
- **Auto Stop for Wrap/Unwrap**: The process halts once the total transaction fee is reached.
- **Transaction Notifications**: The system will send notifications via Telegram when transactions are completed or if any errors occur during the process
- [**Get License and Notifications**](https://t.me/Laporan_Sayang_bot)

## Command-Line Arguments

- `--gass FLOAT`  
  **Default:** `0.111`  
  The gas price threshold in Gwei. This determines the maximum gas price to pay for transactions.

- `--limit FLOAT`  
  **Default:** `0.00036`  
  The total transaction fee limit in ETH. This value controls when to stop wrapping or unwrapping based on the accumulated fees.

   To run the script with default values:

   ```bash
   python3 EEKO.py
   ```
   To specify custom values:
   ```bash
   python3 EEKO.py --gass 0.09 --limit 0.000345
   ```

## Installation

   ```bash
   git clone https://github.com/dpangestuw/eeko.git
   ```
   ```bash
   cd eeko
   ```
   ```bash
   pip install web3==7.3.0 requests colorama
   ```
   ```bash
   python3 EEKO.py
   ```
**Create a file named pvkey.txt and input your private key**

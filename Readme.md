
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

## EEKO Features

- **Voting Mode (Low-Fee Transactions)**: If the gas fee is above the specified limit, the script switches to a voting method. This helps reduce transaction costs, but does not accrue point value.
- **Wrap/Unwrap Mode (Earn Points)**: When the gas fee drops below the specified limit, the script returns to using the wrap/unwrap method. This allows point value to be collected with each transaction.
- **Automatic Count and Fee Tracking**: The system saves transaction counts and total fees, allowing you to resume transactions seamlessly.
- **Auto Stop for Wrap/Unwrap**: The process halts once the total transaction fee is reached.

## VOTE_EEKO Features

- **Before voting, ensure that the balance is in ETH to avoid a shortage of transaction fees.**

- **Controlled Transaction Spam**: Send a specific number of transactions, as specified by the user. This feature enables targeted transaction spamming.


## Command-Line EEKO Arguments

- `--gass (limit gas price)`  
  **Default:** `0.111`  
  The gas price threshold in Gwei. This determines the maximum gas price to pay for transactions.

- `--limit (limit total fee)`  
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

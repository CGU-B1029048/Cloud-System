import os
import sys

storage_path = 'ledgers/'

def app_checkLog(username):
    block_id = 1
    while os.path.exists(storage_path + str(block_id) + '.txt'):
        with open(storage_path + str(block_id) + '.txt', 'r') as f:
            block_data = f.read().splitlines()[2:]
            for data in block_data:
                payer, payee, amount = data.strip().split()
                if payer == username or payee == username:
                    print(f'Ledger {block_id}: {data}')
        block_id += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app_checkLog.py <account name>")
        sys.exit(1)
    target = sys.argv[1].lower()

    app_checkLog(target)
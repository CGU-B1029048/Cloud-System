import os
import sys

storage_path = 'ledgers/'

def app_checkMoney(username):
    block_id = 1
    Money = 0
    while os.path.exists(storage_path + str(block_id) + '.txt'):
        with open(storage_path + str(block_id) + '.txt', 'r') as f:
            block_data = f.read().splitlines()[2:]
            for data in block_data:
                payer, payee, amount = data.strip().split()
                if payer == username:
                    Money -= int(amount)
                elif payee == username:
                    Money += int(amount)
        block_id += 1
    return Money

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app_checkMoney.py <account name>")
        sys.exit(1)
    target = sys.argv[1].lower()

    bal = app_checkMoney(target)

    print(f'Balanece of {target}: {bal}')
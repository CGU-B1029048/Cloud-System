import os
import sys
import hashlib

storge_path = 'ledgers/'

def hash_block(block_path):
    with open(block_path, 'r') as block_file:
        block_data = block_file.read()
        block_data = block_data.encode('utf-8')
        block_hash = hashlib.sha256(block_data).hexdigest()
    return block_hash

# create a new block with hash and next block, no transaction
# blockid : The id of the block being create
def create_block(block_id):
    block_data = f'SHA256 of previous block: {hash_block(storge_path+str(block_id-1)+".txt")}\nNext block: {block_id+1}.txt\n'
    block_path = storge_path + str(block_id) + '.txt'
    with open(block_path, 'w') as block_file:
        block_file.write(block_data)
    return block_path

def find_last_block():
    blockid = 1
    blocksize = 0
    while os.path.exists(storge_path + str(blockid) + '.txt'):
        blockid += 1
    with open(storge_path + str(blockid - 1) + '.txt', 'r') as block_file:
        block_data = block_file.read().splitlines()
        if len(block_data)-2 == 5:
            create_block(blockid)
            return blockid
    return blockid - 1

def record_transaction(payer, payee, payment_amount):
    block_id = find_last_block()
    block_path = storge_path + str(block_id) + '.txt'
    with open(block_path, 'a') as block_file:
        block_file.write(f'{payer} {payee} {payment_amount}\n')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python app_transaction.py <payer> <payee> <payment amount>")
        sys.exit(1)
    if sys.argv[1] == sys.argv[2]:
        print("payer and payee cannot be the same")
        sys.exit(1)
    try:
        payment_amount = int(sys.argv[3])
    except ValueError:
        print("payment amount must be a integer number")
        sys.exit(1)
    if payment_amount <= 0:
        print("payment amount must be a positive integer number")
        sys.exit(1)
    payer = sys.argv[1].lower()
    payee = sys.argv[2].lower()
    record_transaction(payer, payee, payment_amount)
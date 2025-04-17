import os
import sys
import hashlib
from app_transaction import record_transaction

storge_path = 'ledgers/'

def hash_block(block_path):
    with open(block_path, 'r') as block_file:
        block_data = block_file.read()
        block_data = block_data.encode('utf-8')
        block_hash = hashlib.sha256(block_data).hexdigest()
    return block_hash

def app_checkChain(target):
    block_id = 1
    block_path = storge_path + str(block_id) + '.txt'
    while os.path.exists(block_path) :
        # get previous block hash
        prev_hash = hash_block(storge_path + str(block_id-1) + '.txt')
        # extract current block hash and check if it is corrupt
        with open(block_path, 'r') as block_file:
            block_data = block_file.read().splitlines()
            if block_data[0] != f'SHA256 of previous block: {prev_hash}':
                print(f'\033[31mLedger Corrupted\033[0m: Block {block_id} is corrupted')
                return False
        block_id+=1
        block_path = storge_path + str(block_id) + '.txt'

    print('\033[32mLedger Integrity Verified\033[0m, Chain isn\'t currupted.')
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python app_checkChain.py <account name>")
        sys.exit(1)
    target = sys.argv[1].lower()
    succ = app_checkChain(target)

    if succ:
        record_transaction('angel', target, 10)
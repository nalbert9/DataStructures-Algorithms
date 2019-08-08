import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        self.timestamp     = timestamp
        self.data          = data
        self.previous_hash = previous_hash
        self.hash          = self.calc_hash()

    def calc_hash(self):
	    sha = hashlib.sha256()
	    hash_str = self.data.encode('utf-8')
	    sha.update(hash_str)

	    return sha.hexdigest()

class Node:
    def __init__(self, value, next):
        self.value = value
        self.next  = next

class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Block(datetime.now(), data, 0)
            #self.next = self.head

        previous_hash = self.next
        self.next.previous_hash = previous_hash
        block = Block(datetime.now(), data, previous_hash)
        self.head = Node(block, self.head)



# Tests
# Instantiate blocks
block0 = Block(datetime.now(), "Block 0", 0)
block1 = Block(datetime.now(), "Block 1", block0)
block2 = Block(datetime.now(), "Block 2", block1)

# print("Data: {} \n Timestamp: {} \n SHA256 Hash: {} \n Prev_Hash: {} \n ".format(block0.data, block0.timestamp, block0.hash, 0))
# print("Data: {} \n Timestamp: {} \n SHA256 Hash: {} \n Prev_Hash: {} \n ".format(block1.data, block1.timestamp, block1.hash, block1.previous_hash.hash))
# print("Data: {} \n Timestamp: {} \n SHA256 Hash: {} \n Prev_Hash: {} \n ".format(block2.data, block2.timestamp, block2.hash, block2.previous_hash.hash))

# Fonction to print the blocks of the block chain
def print_blockchain(block_name):
    print("Data: {}\n Timestamp: {} \n SHA256 Hash: {} \n Prev_Hash: {} \n ".format(block_name.data, 
                                                                                     block_name.timestamp, 
                                                                                     block_name.hash, 
                                                                                     block_name.previous_hash.hash))
print_blockchain(block0)
print_blockchain(block1)
print_blockchain(block2)


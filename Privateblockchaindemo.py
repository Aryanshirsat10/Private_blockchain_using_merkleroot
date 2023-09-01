import hashlib

N = int(input("Enter the number of nodes in the blockchain: "))
n = int(input("Enter the number of transactions per block in exponent of 2: "))
difficulty = int(input("Enter the difficulty level (number of leading zeros required in block hash): "))

def merkleroot(n):
    transactions = []
    for i in range(n):
        transaction_data = input("Enter the transaction: ")
        transactions.append(hashlib.sha256(transaction_data.encode('utf-8')).hexdigest())
    tree = transactions[:]

    for j in range(n):
        for i in range(2**(n-1)):
            left = tree[i]
            right = tree[i + (2**j)] if i + (2**j) < len(tree) else left
            combined_data = left + right
            tree.append(hashlib.sha256(combined_data.encode('utf-8')).hexdigest())
    return tree[-1]

def mine_block(block_data, difficulty):
    nonce = 0
    while True:
        block = block_data + str(nonce)
        block_hash = hashlib.sha256(block.encode('utf-8')).hexdigest()
        if block_hash[:difficulty] == "0" * difficulty:
            return block_hash, nonce
        nonce += 1

def blockhashgenerator(N):
    prevhash = '0000'
    for i in range(N):
        if i == 0:
            merkle_root = merkleroot(n)
            block_data = prevhash + merkle_root
        else:
            block_data = prevhash + merkleroot(n)

        block_hash, nonce = mine_block(block_data, difficulty)
        prevhash = block_hash
        print("Hash of Block " + str(i + 1) + " is " + block_hash + " (Nonce: " + str(nonce) + ")")

blockhashgenerator(N)

import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash="0"):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Generate SHA-256 hash for the block"""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def display_block(self):
        """Display block information"""
        print(f"Block {self.index}:")
        print(f"  Timestamp: {self.timestamp}")
        print(f"  Data: {self.data}")
        print(f"  Previous Hash: {self.previous_hash}")
        print(f"  Hash: {self.hash}")
        print(f"  Nonce: {self.nonce}")
        print("-" * 50)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        """Create the first block in the chain"""
        return Block(0, "Genesis Block", "0")
    
    def get_latest_block(self):
        """Get the most recent block"""
        return self.chain[-1]
    
    def add_block(self, data):
        """Add a new block to the chain"""
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)
    
    def display_chain(self):
        """Display all blocks in the chain"""
        print("BLOCKCHAIN:")
        print("=" * 50)
        for block in self.chain:
            block.display_block()
    
    def is_chain_valid(self):
        """Validate the entire blockchain"""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            # Check if current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {i}")
                return False
            
            # Check if current block points to previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid previous hash at block {i}")
                return False
        
        return True

def main():
    # Create blockchain and add 3 blocks
    blockchain = Blockchain()
    
    print("Creating blockchain with 3 blocks...\n")
    blockchain.add_block("Alice sends 10 BTC to Bob")
    blockchain.add_block("Charlie sends 5 BTC to Dave")
    blockchain.add_block("Eve sends 15 BTC to Frank")
    
    # Display original blockchain
    blockchain.display_chain()
    
    # Validate blockchain
    print(f"Is blockchain valid? {blockchain.is_chain_valid()}\n")
    
    # CHALLENGE: Tamper with Block 1
    print("CHALLENGE: Tampering with Block 1...")
    print("Changing 'Alice sends 10 BTC to Bob' to 'Alice sends 1000 BTC to Bob'\n")
    
    # Tamper with the data
    blockchain.chain[1].data = "Alice sends 1000 BTC to Bob"
    
    # Display tampered blockchain
    print("BLOCKCHAIN AFTER TAMPERING:")
    print("=" * 50)
    blockchain.display_chain()
    
    # Check validity after tampering
    print(f"Is blockchain valid after tampering? {blockchain.is_chain_valid()}\n")
    
    # Show the impact on subsequent blocks
    print("IMPACT ANALYSIS:")
    print("Block 1's hash changed, but Block 2 still points to the old hash.")
    print("This breaks the chain linkage, making all subsequent blocks invalid!")
    
    # Fix the chain by recalculating hashes
    print("\nFIXING THE CHAIN:")
    print("Recalculating hashes for all affected blocks...\n")
    
    # Recalculate hash for tampered block
    blockchain.chain[1].hash = blockchain.chain[1].calculate_hash()
    
    # Update subsequent blocks' previous_hash and recalculate their hashes
    for i in range(2, len(blockchain.chain)):
        blockchain.chain[i].previous_hash = blockchain.chain[i-1].hash
        blockchain.chain[i].hash = blockchain.chain[i].calculate_hash()
    
    # Display fixed blockchain
    print("BLOCKCHAIN AFTER FIXING:")
    print("=" * 50)
    blockchain.display_chain()
    
    print(f"Is blockchain valid after fixing? {blockchain.is_chain_valid()}")

if __name__ == "__main__":
    main()
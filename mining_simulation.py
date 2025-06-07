import hashlib
import time
from datetime import datetime

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        attempts = 0
        start_time = time.time()
        
        print(f"\nMining block with difficulty {difficulty}...")
        print(f"Target hash pattern: {target}")
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            attempts += 1
            
            # Print progress every 100,000 attempts
            if attempts % 100000 == 0:
                elapsed_time = time.time() - start_time
                hash_rate = attempts / elapsed_time if elapsed_time > 0 else 0
                print(f"Attempts: {attempts:,}, Current hash: {self.hash}")
                print(f"Current hash rate: {hash_rate:.2f} hashes/second")
        
        end_time = time.time()
        mining_time = max(end_time - start_time, 0.001)  # Ensure minimum time of 1ms
        
        print(f"\nBlock mined successfully!")
        print(f"Final hash: {self.hash}")
        print(f"Total attempts: {attempts:,}")
        print(f"Mining time: {mining_time:.3f} seconds")
        print(f"Hash rate: {attempts/mining_time:.2f} hashes per second")
        
        return attempts, mining_time

def run_mining_simulation():
    # Test different difficulty levels
    difficulties = [2, 3, 4, 5]
    results = []
    
    print("=== Mining Simulation ===")
    print("Testing different difficulty levels...")
    
    for difficulty in difficulties:
        print(f"\n{'='*50}")
        print(f"Difficulty Level: {difficulty}")
        print(f"{'='*50}")
        
        # Create a new block for each difficulty level
        block = Block(1, f"Test Block - Difficulty {difficulty}", "0")
        attempts, mining_time = block.mine_block(difficulty)
        
        results.append({
            'difficulty': difficulty,
            'attempts': attempts,
            'time': mining_time,
            'hash_rate': attempts/mining_time
        })
    
    # Display summary with improved formatting
    print("\n=== Mining Simulation Summary ===")
    print("=" * 75)
    print(f"{'Difficulty':^12} | {'Attempts':^15} | {'Time (s)':^12} | {'Hash Rate':^20}")
    print("-" * 75)
    
    for result in results:
        print(f"{result['difficulty']:^12} | {result['attempts']:^15,} | {result['time']:^12.3f} | {result['hash_rate']:^20.2f}")
    
    print("=" * 75)
    print("Hash Rate is measured in hashes per second")

def main():
    run_mining_simulation()

if __name__ == "__main__":
    main()

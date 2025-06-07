import random
import time
from typing import List, Dict

class Validator:
    def __init__(self, name: str, power: float = 0, stake: float = 0, votes: int = 0):
        self.name = name
        self.power = power  # For PoW
        self.stake = stake  # For PoS
        self.votes = votes  # For DPoS

class ConsensusSimulation:
    def __init__(self):
        # Initialize mock validators
        self.validators = {
            'miners': [
                Validator("Miner1", power=random.uniform(1, 100)),
                Validator("Miner2", power=random.uniform(1, 100)),
                Validator("Miner3", power=random.uniform(1, 100))
            ],
            'stakers': [
                Validator("Staker1", stake=random.uniform(1000, 10000)),
                Validator("Staker2", stake=random.uniform(1000, 10000)),
                Validator("Staker3", stake=random.uniform(1000, 10000))
            ],
            'delegates': [
                Validator("Delegate1", votes=random.randint(1, 100)),
                Validator("Delegate2", votes=random.randint(1, 100)),
                Validator("Delegate3", votes=random.randint(1, 100))
            ]
        }

    def proof_of_work(self) -> Validator:
        """Simulate PoW by selecting validator with highest computational power"""
        selected = max(self.validators['miners'], key=lambda x: x.power)
        print("\n=== Proof of Work (PoW) ===")
        print("Selection based on computational power (hash rate)")
        print("Validator Power Distribution:")
        for miner in self.validators['miners']:
            print(f"{miner.name}: {miner.power:.2f} hash power")
        print(f"\nSelected Validator: {selected.name}")
        print(f"Reason: Highest computational power ({selected.power:.2f})")
        return selected

    def proof_of_stake(self) -> Validator:
        """Simulate PoS by selecting validator with highest stake"""
        selected = max(self.validators['stakers'], key=lambda x: x.stake)
        print("\n=== Proof of Stake (PoS) ===")
        print("Selection based on amount of cryptocurrency staked")
        print("Validator Stake Distribution:")
        for staker in self.validators['stakers']:
            print(f"{staker.name}: {staker.stake:.2f} tokens staked")
        print(f"\nSelected Validator: {selected.name}")
        print(f"Reason: Highest stake amount ({selected.stake:.2f} tokens)")
        return selected

    def delegated_proof_of_stake(self) -> Validator:
        """Simulate DPoS by selecting delegate with most votes"""
        selected = max(self.validators['delegates'], key=lambda x: x.votes)
        print("\n=== Delegated Proof of Stake (DPoS) ===")
        print("Selection based on number of votes from token holders")
        print("Delegate Vote Distribution:")
        for delegate in self.validators['delegates']:
            print(f"{delegate.name}: {delegate.votes} votes")
        print(f"\nSelected Validator: {selected.name}")
        print(f"Reason: Most votes received ({selected.votes} votes)")
        return selected

    def run_simulation(self):
        print("=== Consensus Mechanisms Simulation ===")
        print("Comparing PoW, PoS, and DPoS selection methods")
        print("=" * 50)

        # Run each consensus mechanism
        pow_validator = self.proof_of_work()
        time.sleep(1)  # Add delay for better readability
        
        pos_validator = self.proof_of_stake()
        time.sleep(1)
        
        dpos_validator = self.delegated_proof_of_stake()

        # Display comparison summary
        print("\n=== Simulation Summary ===")
        print("=" * 50)
        print(f"PoW  Selected: {pow_validator.name} (Power: {pow_validator.power:.2f})")
        print(f"PoS  Selected: {pos_validator.name} (Stake: {pos_validator.stake:.2f})")
        print(f"DPoS Selected: {dpos_validator.name} (Votes: {dpos_validator.votes})")
        print("=" * 50)

def main():
    # Create and run the simulation
    simulation = ConsensusSimulation()
    simulation.run_simulation()

if __name__ == "__main__":
    main()

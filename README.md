# Blockchain_Simulations_BSB

# Blockchain Implementation and Simulation Suite

This repository contains a collection of Python implementations demonstrating core blockchain concepts, including basic blockchain structure, mining simulation, and consensus mechanisms.

## Projects Overview

### 1. Basic Blockchain Implementation (`blockchain.py`)
A fundamental blockchain implementation that demonstrates the core concepts of blockchain technology.

#### Features:
- Block creation with index, timestamp, data, and hash
- SHA-256 hashing implementation
- Block linking through previous hash
- Chain validation
- Tamper detection
- Proof of work implementation

#### Key Concepts:
- **Block Structure**: Each block contains:
  - Index
  - Timestamp
  - Data
  - Previous hash
  - Current hash
  - Nonce
- **Chain Validation**: Verifies the integrity of the entire blockchain
- **Tamper Detection**: Demonstrates how modifying one block affects the entire chain

### 2. Mining Simulation (`mining_simulation.py`)
A detailed simulation of the mining process with different difficulty levels.

#### Features:
- Multiple difficulty levels (2-5)
- Real-time mining statistics
- Hash rate calculation
- Mining time measurement
- Detailed performance metrics

#### Key Concepts:
- **Proof of Work**: Demonstrates the computational effort required for mining
- **Difficulty Levels**: Shows how increasing difficulty affects mining time
- **Hash Rate**: Measures mining performance in hashes per second
- **Mining Statistics**: Tracks attempts, time, and success rates

### 3. Consensus Mechanisms Simulation (`consensus_mechanisms_sim.py`)
A comparative simulation of different blockchain consensus mechanisms.

#### Features:
- Proof of Work (PoW) simulation
- Proof of Stake (PoS) simulation
- Delegated Proof of Stake (DPoS) simulation
- Random validator generation
- Selection process visualization

#### Key Concepts:
- **PoW**: Selection based on computational power
- **PoS**: Selection based on stake amount
- **DPoS**: Selection based on voting
- **Validator Selection**: Demonstrates different selection criteria

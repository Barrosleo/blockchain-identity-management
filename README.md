# Blockchain-Based Identity Management System

This project implements a decentralized identity management system using blockchain technology. It allows users to create and manage their identities securely and transparently.

## Table of Contents
- Introduction
- Features
- Technologies Used
- Setup Instructions
- Usage
- Smart Contract
- Python Script
- Contributing
- License

## Introduction
In a world where digital identities are increasingly important, this project leverages blockchain technology to provide a secure and decentralized way to manage identities. By using blockchain, we ensure that identities are immutable, transparent, and secure from tampering.

## Features
- **Decentralized Identity Management**: Identities are stored on the blockchain, ensuring they are secure and tamper-proof.
- **Public and Private Keys**: Each identity is associated with a public and private key pair for secure communication.
- **Smart Contract**: A Solidity smart contract handles the creation and retrieval of identities.
- **Python Integration**: A Python script interacts with the smart contract to create and manage identities.

## Technologies Used
- **Blockchain**: Ethereum, Ganache
- **Smart Contract**: Solidity
- **Python**: Web3.py, PyCryptodome
- **Virtualization**: Ganache for local blockchain setup

## Setup Instructions
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Barrosleo/blockchain-identity-management.git
    cd blockchain-identity-management
    ```

2. **Install Dependencies**:
    ```bash
    pip install web3 pycryptodome
    ```

3. **Set Up Local Blockchain**:
    - Download and install Ganache.
    - Start Ganache to create a local blockchain environment.

4. **Compile and Deploy Smart Contract**:
    - Use Remix IDE to compile and deploy the `IdentityManagement.sol` smart contract to your local blockchain (Ganache).
    - Copy the deployed contract address and ABI.

5. **Update Python Script**:
    - Update the `identity_management.py` script with the contract address and ABI.

## Usage
1. **Run the Python Script**:
    ```bash
    python identity_management.py
    ```

2. **Create an Identity**:
    - Choose the option to create an identity.
    - Enter your name and email.
    - The script will generate a public/private key pair and store the identity on the blockchain.

3. **Get an Identity**:
    - Choose the option to get an identity.
    - Enter the address of the identity you want to retrieve.
    - The script will fetch and display the identity details from the blockchain.

## Smart Contract
The smart contract is written in Solidity and handles the creation and retrieval of identities. Here is the contract code:

```solidity
pragma solidity ^0.8.0;

contract IdentityManagement {
    struct Identity {
        string name;
        string email;
        string publicKey;
    }

    mapping(address => Identity) private identities;

    function createIdentity(string memory _name, string memory _email, string memory _publicKey) public {
        identities[msg.sender] = Identity(_name, _email, _publicKey);
    }

    function getIdentity(address _address) public view returns (string memory, string memory, string memory) {
        Identity memory identity = identities[_address];
        return (identity.name, identity.email, identity.publicKey);
    }
}
```
## Python Script
The Python script interacts with the smart contract to create and manage identities. Here is a brief overview of the script:

- **Connect to Blockchain**: Connects to the local blockchain using Web3.py.
- **Create Identity**: Generates a public/private key pair and stores the identity on the blockchain.
- **Get Identity**: Retrieves and displays identity details from the blockchain.

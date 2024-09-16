pip install web3 pycryptodome

from web3 import Web3
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import json

# Connect to the Blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

with open('IdentityManagement.json') as f:
    contract_data = json.load(f)

contract_address = "your_contract_address"
contract = web3.eth.contract(address=contract_address, abi=contract_data['abi'])

# Create Identity Function
def create_identity(name, email):
    key = RSA.generate(2048)
    public_key = key.publickey().export_key().decode()
    private_key = key.export_key().decode()

    tx_hash = contract.functions.createIdentity(name, email, public_key).transact()
    web3.eth.waitForTransactionReceipt(tx_hash)

    return private_key

# Get Identity Function
def get_identity(address):
    identity = contract.functions.getIdentity(address).call()
    return {
        "name": identity[0],
        "email": identity[1],
        "public_key": identity[2]
    }

# Main Function to Run the System
if __name__ == "__main__":
    choice = input("Do you want to (c)reate or (g)et an identity? ")

    if choice == 'c':
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        private_key = create_identity(name, email)
        print(f"Identity created successfully. Your private key: {private_key}")

    elif choice == 'g':
        address = input("Enter the address to get the identity: ")
        identity = get_identity(address)
        print(f"Name: {identity['name']}\nEmail: {identity['email']}\nPublic Key: {identity['public_key']}")

import random
import hashlib
import time

# Sample wallet addresses (randomly generated for testing purposes)
WALLETS = [
    "0xAb23CDef45678901234567890123456789012345",
    "0xBf98Ghij90123456789012345678901234567890",
    "0xCd67Klmn23456789012345678901234567890123",
    "0xDe45Opqr56789012345678901234567890123456",
    "0xEf23Stuv89012345678901234567890123456789"
]

# Function to generate a random transaction
def generate_random_tx():
    sender = random.choice(WALLETS)
    receiver = random.choice([w for w in WALLETS if w != sender])
    amount = round(random.uniform(0.001, 5), 6)  # Amount in crypto
    timestamp = int(time.time())
    tx_data = f"{sender}{receiver}{amount}{timestamp}"
    tx_hash = hashlib.sha256(tx_data.encode()).hexdigest()
    
    return {
        "sender": sender,
        "receiver": receiver,
        "amount": amount,
        "timestamp": timestamp,
        "tx_hash": tx_hash
    }

if __name__ == "__main__":
    # Generate and print 5 random transactions
    for _ in range(5):
        print(generate_random_tx())

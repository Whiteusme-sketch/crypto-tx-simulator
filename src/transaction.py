crypto-tx-simulator/
│── src/
│   ├── transaction.py
│   ├── wallet.py
│   ├── network.py
│── tests/
│   ├── test_transaction.py
│   ├── test_wallet.py
│── README.md
│── requirements.txt
│── .gitignore
│── LICENSE


import hashlib
import random
import time

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()
        self.tx_id = self.generate_tx_id()

    def generate_tx_id(self):
        data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return hashlib.sha256(data.encode()).hexdigest()

    def __repr__(self):
        return f"TX({self.tx_id[:10]}... | {self.sender} -> {self.receiver} | {self.amount} BTC)"

if __name__ == "__main__":
    tx = Transaction("Alice", "Bob", round(random.uniform(0.001, 2.5), 6))
    print(tx)

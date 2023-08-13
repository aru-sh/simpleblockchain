from decimal import Decimal
from pprint import pprint
from typing import Optional

from address import Address


class Transaction:
    TRANSACTION_NUMBER = 0

    def __init__(self, sender: Address, receiver: Address, amount: Decimal):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self._transaction_signature: Optional[str] = None

    def transact(self):
        self.sender.subtract_balance(self.amount)
        self.receiver.add_balance(self.amount)
        self.increase_transaction_number()
        self._sign_transaction()
        pprint(f"Transaction from {self.sender.hash_address} to {self.receiver.hash_address} "
               f" of amount {self.amount} successful "
               f"transaction signature: {self._transaction_signature}")

    def _sign_transaction(self):
        txn_concat_str = f'{self.sender.hash_address}:{self.receiver.hash_address}:{self.amount}:{self.TRANSACTION_NUMBER}'
        txn_signature = self.sender.sign_bytes(txn_concat_str.encode('utf-8')).hex()
        self._transaction_signature = txn_signature

    @property
    def transaction_signature(self):
        return self._transaction_signature

    @transaction_signature.setter
    def transaction_signature(self, transaction_signature):
        raise AttributeError("cannot set transaction hash")

    @classmethod
    def increase_transaction_number(cls):
        cls.TRANSACTION_NUMBER += 1


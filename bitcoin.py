from decimal import Decimal
from typing import Optional, List, Dict

from address import Address
from block import Block
from transaction import Transaction


class Bitcoin:
    GENESIS_BLOCK: Optional[Block] = None
    TOP_BLOCK: Optional[Block] = None
    ADDRESSES: Dict[str, Address] = {}
    BLOCK_TRANSACTION_LIMIT = 2
    UNCONFIRMED_TRANSACTIONS: List[Transaction] = []

    @classmethod
    def create_address(cls, username: str, initial_balance: Decimal) -> Address:
        address = Address(username=username, initial_balance=initial_balance)
        cls.ADDRESSES[address.hash_address] = address
        return address

    @classmethod
    def transact(cls, sender: Address, receiver: Address, amount: Decimal) -> Transaction:
        txn = Transaction(sender=sender, receiver=receiver, amount=amount)
        txn.transact()

        if len(cls.UNCONFIRMED_TRANSACTIONS) < cls.BLOCK_TRANSACTION_LIMIT:
            cls.UNCONFIRMED_TRANSACTIONS.append(txn)
        else:
            # mint a new block
            block = Block(
                transactions=cls.UNCONFIRMED_TRANSACTIONS,
                previous_block=cls.TOP_BLOCK
            )

            cls.TOP_BLOCK = block

            if cls.GENESIS_BLOCK is None:
                cls.GENESIS_BLOCK = block

            cls.UNCONFIRMED_TRANSACTIONS = []

        return txn

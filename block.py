from typing import List, Optional
from datetime import datetime

from transaction import Transaction
from utils import generate_hash_digest


class Block:
    class BlockHeader:
        """
        Block Header Composition:
        The block header consists of several fields, including:
        Version: A numerical value indicating the block's version.
        Previous Block Hash: The hash of the previous block in the blockchain, which links the blocks together.
        Merkle Root Hash: The hash of the Merkle root of all the transactions in the block.
        Timestamp: The time at which the block was mined.
        Difficulty Target: A value that determines the level of difficulty required for mining the block.
        Nonce: A random number that miners adjust to find a valid hash.
        """
        def __init__(
                self,
                version: str,
                previous_block_hash: str,
                timestamp: int,
                transactions: List[Transaction],
                difficulty_target: int,
                nonce: int
        ):
            self.version = version
            self.previous_block_hash = previous_block_hash
            self.timestamp = timestamp
            self.difficulty_target = difficulty_target
            self.merkle_root_hash: str = self._calculate_merkle_root_hash(transactions=transactions)
            self.nonce = nonce

        def _calculate_merkle_root_hash(self, transactions: List[Transaction]) -> str:
            initial_txn_sign = [transaction.transaction_signature for transaction in transactions]
            return self._calculate_merkle_root_recursively(initial_txn_sign)

        def _calculate_merkle_root_recursively(self, transaction_hash_list: List[str]) -> str:
            if len(transaction_hash_list) == 1:  # base condition
                return transaction_hash_list[0]

            elif len(transaction_hash_list) % 2 != 0:
                transaction_hash_list.append(transaction_hash_list[-1])

            new_transaction_hash_list = []

            for i in range(0, len(transaction_hash_list), 2):
                transaction_pair_hash = generate_hash_digest(
                    f'{transaction_hash_list[i]}:{transaction_hash_list[i + 1]}'
                )
                new_transaction_hash_list.append(transaction_pair_hash)

            return self._calculate_merkle_root_recursively(new_transaction_hash_list)

        def calculate_block_hash(self) -> str:
            block_concat = f'{self.version}:{int(self.timestamp)}:{self.previous_block_hash}:' \
                           f'{self.difficulty_target}:{self.merkle_root_hash}:{self.nonce}'

            return generate_hash_digest(block_concat)

    def __init__(
            self,
            transactions: List[Transaction],
            previous_block
    ):
        self.transactions = transactions

        self.block_header = self.BlockHeader(
            version="0.1.0",
            previous_block_hash=previous_block.block_hash if previous_block else "",
            timestamp=int(datetime.now().timestamp()),
            transactions=transactions,
            difficulty_target=10,
            nonce=100
        )
        self.previous_block: Optional[Block] = previous_block
        self.block_hash: Optional[str] = self.block_header.calculate_block_hash()


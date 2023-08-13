from decimal import Decimal

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

from utils import generate_hash_digest, generate_public_private_key


class Address:
    def __init__(self, username: str, initial_balance: Decimal):
        self._username = username
        self.hash_address: str = generate_hash_digest(self._username)
        self.balance = initial_balance
        public_private_keys = generate_public_private_key()
        self.public_key: bytes = public_private_keys[0]
        self._private_key: RSAPrivateKey = public_private_keys[1]

    def subtract_balance(self, balance: Decimal):
        assert balance <= self.balance
        self.balance -= balance

    def add_balance(self, balance: Decimal):
        self.balance += balance

    def sign_bytes(self, bytes_to_be_signed: bytes):
        signature = self._private_key.sign(
            bytes_to_be_signed,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return signature

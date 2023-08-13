import hashlib
from typing import Tuple

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


def generate_hash_digest(string_to_encode: str):
    return hashlib.sha256(
        f'{string_to_encode}'.encode("utf-8")
    ).hexdigest()


def generate_public_private_key() -> Tuple[bytes, RSAPrivateKey]:
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return public_pem, private_key


if __name__ == '__main__':
    public, private = generate_public_private_key()
    print(public)
    print(private)

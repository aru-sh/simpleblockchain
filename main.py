from decimal import Decimal

from bitcoin import Bitcoin

if __name__ == '__main__':

    bitcoin_blockchain = Bitcoin()
    address_1 = bitcoin_blockchain.create_address(username="Arush", initial_balance=Decimal("0.0"))
    address_2 = bitcoin_blockchain.create_address(username="Ankit", initial_balance=Decimal("0.0"))

    address_1.add_balance(Decimal("1.0"))
    address_2.add_balance(Decimal("2.0"))

    print(address_1.balance)
    print(address_2.balance)

    txn_1 = bitcoin_blockchain.transact(sender=address_1, receiver=address_2, amount=Decimal("0.1"))

    print(address_1.balance)
    print(address_2.balance)

    txn_2 = bitcoin_blockchain.transact(sender=address_1, receiver=address_2, amount=Decimal("0.2"))

    print(address_1.balance)
    print(address_2.balance)

    txn_3 = bitcoin_blockchain.transact(sender=address_2, receiver=address_1, amount=Decimal("0.2"))

    print(address_1.balance)
    print(address_2.balance)

    txn_4 = bitcoin_blockchain.transact(sender=address_1, receiver=address_2, amount=Decimal("0.1"))

    print(address_1.balance)
    print(address_2.balance)

    txn_5 = bitcoin_blockchain.transact(sender=address_1, receiver=address_2, amount=Decimal("0.2"))

    print(address_1.balance)
    print(address_2.balance)

    txn_6 = bitcoin_blockchain.transact(sender=address_2, receiver=address_1, amount=Decimal("0.2"))

    print(address_1.balance)
    print(address_2.balance)

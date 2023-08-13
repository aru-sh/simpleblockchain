
# The following is the abstract of Bitcoin, the first blockchain based cryptocurrency.
# I'll try to decode each term as I encounter them

"""
Abstract.
A purely peer-to-peer version of electronic cash would allow online
payments to be sent directly from one party to another without going through a
financial institution.

Key Terms:
Peer-to-peer System: Decentralized network architecture where each participant has equal footing.
Every node can act as both client and servers and there is resource sharing among nodes.
There is no central authority to govern the peers.
Resource include CPU / Memory / Files etc.
BitTorrent is an example of peer-to-peer file system.


Digital signatures provide part of the solution, but the main
benefits are lost if a trusted third party is still required to prevent double-spending.

Key Terms:
Digital Signature: A cryptographic technique in which is used to verify the authenticity and
integrity of digital transactions.
Here is how it works:

i. Signing process:
The Sender of transaction uses their own private key, which is a component
of asymmetric encryption key pair. The private key is used to create a unique digital signature
for the transaction.

Important: The digital signature is essentially a hash (a fixed size representation) of the document's
content that has been encrypted using private key. This creates a unique identifier for the document.

ii. Verification Process:
The recipient or verifier of the transaction uses the public key associated with the sender's private key to
decrypt the digital signature, revealing hash value.
The verifier then generates a new hash value from the received document or message.
If the decrypted hash value matches the newly generated hash value, it indicates that the document has not been altered
since it was signed and that the signature is valid.

2. Double spending
The act by which a single currency can be spent two times, this problem is trivial to solve in centralized system, but
what about decentralized system?





The network timestamps transactions by hashing them into an ongoing chain of
hash-based proof-of-work, forming a record that cannot be changed without redoing
the proof-of-work. The longest chain not only serves as proof of the sequence of
events witnessed, but proof that it came from the largest pool of CPU power. As
long as a majority of CPU power is controlled by nodes that are not cooperating to
attack the network, they'll generate the longest chain and outpace attackers. The
network itself requires minimal structure. Messages are broadcast on a best effort
basis, and nodes can leave and rejoin the network at will, accepting the longest
proof-of-work chain as proof of what happened while they were gone.

"""
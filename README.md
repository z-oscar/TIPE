# TIPE
Elliptic-curve cryptography
e messaging system using asymmetric encryption based on the ElGamal cryptosystem over elliptic curves. The system ensures secure communication by leveraging the hardness of the discrete logarithm problem in elliptic curve cryptography (ECC).

# Secure Messaging with Elliptic Curve ElGamal Encryption

## Overview

This project implements a secur

## Features

- **Asymmetric Encryption**: Uses public-key cryptography for secure message exchange.
- **Elliptic Curve Cryptography (ECC)**: Provides strong security with smaller key sizes compared to traditional RSA.
- **Message Integrity**: Ensures that only the intended recipient can decrypt messages.
- **Efficient Implementation**: Optimized algorithms for key generation, encryption, and decryption.

## Background

Elliptic curve cryptography is widely used for secure communications due to its strong security properties and efficiency. The ElGamal cryptosystem, originally designed for cyclic groups, can be adapted to work on elliptic curves, providing a secure method for encrypting messages.

## Project Structure

```
├── src
│   ├── key_generation.py  # Generate elliptic curve keys
│   ├── encryption.py      # Encrypt messages using ECC-ElGamal
│   ├── decryption.py      # Decrypt messages
│   ├── utils.py           # Helper functions for elliptic curve operations
│   ├── messaging.py       # Implementation of secure message exchange
│
├── examples
│   ├── demo.py            # Example usage of the secure messaging system
│
├── README.md              # Project documentation
├── requirements.txt       # Dependencies
```

## Installation

Ensure you have Python installed. Then, install the necessary dependencies:

```sh
pip install -r requirements.txt
```

## Usage

### Generating Keys

```python
from src.key_generation import generate_keys
private_key, public_key = generate_keys()
```

### Encrypting a Message

```python
from src.encryption import encrypt
ciphertext = encrypt(public_key, "Hello, World!")
```

### Decrypting a Message

```python
from src.decryption import decrypt
plaintext = decrypt(private_key, ciphertext)
```

### Running the Demo

A demo script is provided in `examples/demo.py`:

```sh
python examples/demo.py
```

## Security Considerations

- Ensure that private keys remain confidential.
- Use sufficiently large key sizes to mitigate attacks.
- Be cautious of side-channel attacks when deploying in real-world applications.

## References

- "Elliptic Curve Cryptography" - [https://math.univ-bpclermont.fr/\~rebolledo/page-fichiers/projetMichael.pdf](https://math.univ-bpclermont.fr/~rebolledo/page-fichiers/projetMichael.pdf)
- "Cryptography and Network Security" - William Stallings

## License

This project is licensed under the MIT License.


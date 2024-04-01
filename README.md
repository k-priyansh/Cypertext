## <a href="https://github.com/k-priyansh/Cypertext" style="text-decoration:none">Cypertext</a>
Cypertext is a Python-based tool for encrypting and decrypting text using symmetric key cryptography. It provides a simple command-line interface for users to encrypt their sensitive text data and generate keys securely.

<img src="img/1. interface.png">

### Features
- Encrypt plaintext into ciphertext using a symmetric key.
- Decrypt ciphertext back to plaintext using the same key.
- Generate a secure key for encryption and decryption.

### Installation
You have to  install cryptography module of python using pip:

```
pip install cryptography
```

### Usage
Encrypting Text
<strong>To encrypt text, use the following command:</strong>

<img src="img/2. encrypted 1.png">

<img src="img/3. encrypted 2.png">

This will prompt you to enter a key for encryption. Once the encryption is complete, it will display the ciphertext.

Decrypting Text
<strong>To decrypt ciphertext, use the following command:</strong>

<img src="img/4. decrypted.png">

This will prompt you to enter the key used for encryption. Once the decryption is complete, it will display the original plaintext.

### Examples
<strong>Encrypting text:</strong>

```
$ python3 cypertext.py
1. encrypt
2. decrypt
enter options: 1
key: b'SaHikTxl9Zs1aVwahFkODJ9POETy9KtoFL0vBdOnAP4='
Enter text: cypertext
Encrypted text: b'gAAAAABmCrwyRBX7fEfIesReieR5xqhmCWNGls4Aep5Lm2UBJS7mF8-NBML_E_qIne-jm8omz-ljBUsU7IBoweFy5F8cNUFyVg=='
```
<strong>Decrypting text:</strong>

```
$ python3 cypertext.py
1. encrypt
2. decrypt
enter options: 2
Enter key: b'SaHikTxl9Zs1aVwahFkODJ9POETy9KtoFL0vBdOnAP4='
Enter encrypted token: b'gAAAAABmCrwyRBX7fEfIesReieR5xqhmCWNGls4Aep5Lm2UBJS7mF8-NBML_E_qIne-jm8omz-ljBUsU7IBoweFy5F8cNUFyVg=='
Decrypted text: cypertext
```


### Contributing
Contributions are welcome! Please feel free to open issues or pull requests.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

#pip install cryptography
from cryptography.fernet import Fernet

#encrypter function
def encrypt_text(text,key):
    f = Fernet(key)
    token = f.encrypt(text.encode())
    return token


#decrypter function
def decrypt_text(encrypted_token,key):
    f = Fernet(key) 
    decrypted_text = f.decrypt(encrypted_token).decode()
    print("Decrypted text:", decrypted_text)
    return decrypted_text


#banner
print(" ")
print("dP""b8   Yb  dP   88""Yb   888888   88""Yb     888888   888888   Yb  dP   888888 ")
print('dP   `"   YbdP    88__dP   88__     88__dP       88     88__      YbdP      88   ')
print('Yb         8P     88"""    88""     88"Yb        88     88""      dPYb      88   ')
print("YboodP     dP     88       888888   88  Yb       88     888888   dP  Yb     88   ")
print("")


#option
print('select the option from the given below: ')
print("1. encrypt") 
print("2. decrypt")
option=int(input("enter option: "))



if option == 1:
    #generating the key
    key = Fernet.generate_key()
    print("key: ",key)
    #text
    text = input("Enter text: ")
    #calling encrypter function
    encrypted_text = encrypt_text(text, key)
    print("Encrypted text:", encrypted_text)
elif option == 2:
    #key
    key = input("Enter key: ")
    #encryptec text
    encrypted_token = input("Enter encrypted token: ")
    #calling decrypter function
    decrypt_text(encrypted_token, key)
else:
    print("Wrong option selected")

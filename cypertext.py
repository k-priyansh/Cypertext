from cryptography.fernet import Fernet 
def encrypt_text(text,key): 
  f = Fernet(key) 
  token = f.encrypt(text.encode()) 
  return token 
  
def decrypt_text(encrypted_token,key): 
  f = Fernet(key) 
  decrypted_text = f.decrypt(encrypted_token).decode() p
  rint("Decrypted text:", decrypted_text) 
  return decrypted_text 
  
print("1. encrypt") 
print("2. decrypt") 
option=int(input("enter option: ")) 
if option == 1: 
  key = Fernet.generate_key() 
  print("key: ",key) 
  text = input("Enter text: ") 
  encrypted_text = encrypt_text(text, key) 
  print("Encrypted text:", encrypted_text) 
elif option == 2: 
  key = input("Enter key: ") 
  encrypted_token = input("Enter encrypted token: ") 
  decrypt_text(encrypted_token, key) 
else: 
  print("Wrong option selected")

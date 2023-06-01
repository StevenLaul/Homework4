from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_tekst(plain_tekst):
    with open("avalik_voti.txt", "rb") as file:
        public_key = RSA.import_key(file.read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_text = cipher_rsa.encrypt(plain_text.encode())
    with open("encrypted_tekst.txt", "wb") as file:
        file.write(encrypted_tekst)

#Encrypt tekst
plain_text = input("Sisesta tekst krüpteerimiseks: ")
encrypt_teks(plain_tekst)
print("Tekst on krüpteeritud ja salvestatud.")
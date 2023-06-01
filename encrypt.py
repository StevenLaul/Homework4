from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_tekst(plain_tekst):
    with open("avalik_voti.txt", "rb") as file:
        avalik_voti = RSA.import_key(file.read())
    cipher_rsa = PKCS1_OAEP.new(avalik_voti)
    encrypted_tekst = cipher_rsa.encrypt(plain_tekst.encode())
    with open("encrypted_tekst.txt", "wb") as file:
        file.write(encrypted_tekst)

#Encrypt tekst
plain_tekst = input("Sisesta tekst krüpteerimiseks: ")
encrypt_tekst(plain_tekst)
print("Tekst on krüpteeritud ja salvestatud.")
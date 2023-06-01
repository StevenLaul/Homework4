from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def decrypt_tekst():
    with open("privaat_voti.txt", "rb") as file:
        privaat_voti = RSA.import_key(file.read())
    with open("encrypted_tekst.txt", "rb") as file:
        encrypted_tekst = file.read()
    cipher_rsa = PKCS1_OAEP.new(privaat_voti)
    decrypted_tekst = cipher_rsa.decrypt(encrypted_tekst)
    return decrypted_tekst.decode()

# Decrypti tekst
decrypted_tekst = decrypt_tekst()
print("Decrypted tekst:", decrypted_tekst)
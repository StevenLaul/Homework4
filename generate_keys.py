from Crypto.PublicKey import RSA

def genereeri_voti():
    key = RSA.generate(2048)
    avalik_voti = key.publickey().export_key()
    privaat_voti = key.export_key()
    with open("privaat_voti.txt", "wb") as file:
        file.write(privaat_voti)
    with open("avalik_voti.txt", "wb") as file:
        file.write(avalik_voti)

# Genereeri võti
genereeri_voti()
print("RSA võti genereeritud ja salvestatud.")
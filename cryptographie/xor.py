# XOR simple

def xor_chiffrer(texte, cle):
    return bytes(a ^ cle for a in texte.encode())

message = "secret"
cle = 7
chiffre = xor_chiffrer(message, cle)
print("Message:", message)
print("Chiffré:", chiffre)

# Déchiffrement
print("Déchiffré:", bytes(a ^ cle for a in chiffre).decode())

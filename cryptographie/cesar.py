# Chiffrement de César simple


def chiffrer_cesar(texte, decalage):
    resultat = ""
    for lettre in texte:
        if lettre.isalpha():
            base = ord('a') if lettre.islower() else ord('A')
            resultat += chr((ord(lettre) - base + decalage) % 26 + base)
        else:
            resultat += lettre
    return resultat


message = "bonjour"
print("Texte original:", message)
print("Texte chiffré:", chiffrer_cesar(message, 3))

# Cryptographie en Python

Ce dossier contient de petits exemples simples pour commencer avec la cryptographie.

## 1. Hashage
Le hashage transforme un texte en valeur unique, souvent utilisée pour vérifier l'intégrité.

Exemple : `hashage.py`

## 2. Base64
Base64 sert à encoder des données sous forme de texte.

Exemple : `base64_example.py`

## 3. Chiffrement de César
C'est un chiffrement très simple où chaque lettre est décalée.

Exemple : `cesar.py`

## 4. XOR
Le XOR est une opération binaire utilisée dans les algorithmes simples.

Exemple : `xor.py`

## À retenir
- Le hashage ne permet pas de retrouver le message original.
- Base64 n'est pas du chiffrement, c'est juste une conversion.
- Le chiffrement de César est pédagogique, mais pas sécurisé.
- Pour la vraie sécurité, il faut utiliser des bibliothèques modernes comme `cryptography`.

## Prochaine étape
Tu peux ensuite apprendre :
- Fernet
- AES
- HMAC
- chiffrement asymétrique RSA

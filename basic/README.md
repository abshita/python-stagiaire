# Dossier basic

Ce dossier contient les bases de Python.

## Contenu
- `types.py` : types de données
- `condition.py` : conditions (`if`, `elif`, `else`)
- `for_loop.py` : boucle `for`
- `for_each.py` : boucle sur une liste
- `while_loop.py` : boucle `while`
- `functions.py` : fonctions
- `try_except.py` : gestion des erreurs
- `main.py` : petit script d'introduction

## Objectif
Apprendre les concepts fondamentaux avant d'aller vers le niveau avancé.

# Python pour débutants

Ce mini projet sert à apprendre les bases de Python avec des exemples simples.

## 1. Variables
Les variables servent à stocker des valeurs.

```python
nom = "Alice"
age = 20
prix = 15.5
est_etudiant = True
```

### Types de base
- `int` : nombre entier
- `float` : nombre décimal
- `str` : texte
- `bool` : vrai ou faux

---

## 2. Conditions
On utilise `if`, `elif` et `else` pour tester des conditions.

```python
age = 18

if age >= 18:
    print("Tu es adulte")
else:
    print("Tu es mineur")
```

### Exemple
```python
note = 80

if note >= 90:
    print("Excellent")
elif note >= 70:
    print("Bien")
else:
    print("À améliorer")
```

---

## 3. Boucles `for`
La boucle `for` sert à répéter une action plusieurs fois.

```python
for i in range(1, 6):
    print(i)
```

Sortie :
```python
1
2
3
4
5
```

### `for` sur une liste
```python
fruits = ["pomme", "banane", "orange"]

for fruit in fruits:
    print(fruit)
```

---

## 4. Boucle `while`
La boucle `while` continue tant qu'une condition est vraie.

```python
compteur = 1

while compteur <= 5:
    print(compteur)
    compteur += 1
```

---

## 5. Fonctions
Une fonction permet de regrouper du code réutilisable.

```python
def addition(a, b):
    return a + b

print(addition(3, 4))
```

### Exemple plus simple
```python
def dire_bonjour(nom):
    return f"Bonjour {nom}"

print(dire_bonjour("Alice"))
```

---

## 6. Listes
Une liste contient plusieurs valeurs.

```python
nombres = [1, 2, 3, 4, 5]
print(nombres[0])
print(len(nombres))
```

---

## 7. Gestion des erreurs (`try` / `except`)
On utilise `try` pour tester du code et `except` pour gérer une erreur.

```python
try:
    nombre = int(input("Entrez un nombre : "))
    print(10 / nombre)
except ValueError:
    print("Ce n'est pas un nombre valide")
except ZeroDivisionError:
    print("On ne peut pas diviser par zéro")
finally:
    print("Fin du programme")
```

---

## 8. Entrée utilisateur
```python
nom = input("Quel est ton nom ? ")
print("Bonjour", nom)
```

---

## Aide-mémoire Python

### Syntaxe de base
- `print()` : afficher quelque chose
- `input()` : demander une information
- `if` : teste une condition
- `for` : répète sur une liste ou un intervalle
- `while` : répète tant qu'une condition est vraie
- `def` : définit une fonction
- `return` : renvoie une valeur
- `try` / `except` : gère les erreurs

### Exemple complet
```python
nom = "Alice"
age = 20

if age >= 18:
    print("Bienvenue", nom)
else:
    print("Tu es mineur")

for i in range(1, 4):
    print(i)

def bonjour(nom):
    return f"Bonjour {nom}"

print(bonjour(nom))
```

---

## Conseils pour apprendre
1. Écris un petit script simple.
2. Teste chaque exemple dans Python.
3. Modifie les valeurs pour comprendre.
4. Répète les bases avant d'aller plus loin.

---

## Fichiers de ce projet
- `types.py` : types de base
- `condition.py` : conditions
- `for_loop.py` : boucle `for`
- `for_each.py` : boucle sur une liste
- `while_loop.py` : boucle `while`
- `functions.py` : fonctions
- `try_except.py` : gestion d'erreurs

---

## Prochaine étape
Tu peux maintenant apprendre :
- les listes avancées
- les dictionnaires
- les tuples
- les modules
- les classes
- les projets simples

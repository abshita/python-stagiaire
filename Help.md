# Aide-mémoire Python et Linux

Ce fichier regroupe les commandes utiles pour commencer avec Python, Linux et pip.

---

## 1. Vérifier Python

```bash
python --version
python3 --version
```

Pour savoir où Python est installé :

```bash
which python
which python3
```

---

## 2. Lancer un script Python

```bash
python nom_script.py
python3 nom_script.py
```

Pour lancer un fichier dans un dossier :

```bash
cd mon_dossier
python main.py
```

---

## 3. Créer un environnement virtuel

```bash
python -m venv .venv
```

Activer l'environnement virtuel :

### Linux / Mac
```bash
source .venv/bin/activate
```

### Windows PowerShell
```powershell
.\.venv\Scripts\Activate.ps1
```

### Windows CMD
```cmd
.venv\Scripts\activate.bat
```

---

## 4. Installer des paquets avec pip

Installer un paquet :

```bash
pip install nom_du_paquet
```

Installer une version précise :

```bash
pip install nom_du_paquet==1.2.3
```

Mettre à jour pip :

```bash
python -m pip install --upgrade pip
```

Voir les paquets installés :

```bash
pip list
```

Voir une information sur un paquet :

```bash
pip show nom_du_paquet
```

Désinstaller un paquet :

```bash
pip uninstall nom_du_paquet
```

---

## 5. Créer un fichier requirements.txt

```bash
pip freeze > requirements.txt
```

Installer depuis requirements.txt :

```bash
pip install -r requirements.txt
```

---

## 6. Commandes Linux de base

### Se déplacer
```bash
pwd
ls
cd dossier
cd ..
```

### Créer et supprimer
```bash
mkdir dossier
rmdir dossier
rm fichier.txt
rm -r dossier
```

### Copier et déplacer
```bash
cp fichier.txt copie.txt
mv ancien.txt nouveau.txt
```

### Afficher un fichier
```bash
cat fichier.txt
less fichier.txt
more fichier.txt
```

### Chercher un mot dans un fichier
```bash
grep "mot" fichier.txt
```

### Voir les processus
```bash
ps
ps aux
```

### Arrêter un processus
```bash
kill 1234
```

---

## 7. Bases Python

### Variables
```python
nom = "Alice"
age = 20
prix = 15.5
est_etudiant = True
```

### Conditions
```python
if age >= 18:
    print("Adulte")
else:
    print("Mineur")
```

### Boucles
```python
for i in range(1, 6):
    print(i)
```

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

### Fonctions
```python
def addition(a, b):
    return a + b

print(addition(2, 3))
```

### Listes
```python
fruits = ["pomme", "banane", "orange"]
print(fruits[0])
```

### Dictionnaires
```python
personne = {"nom": "Alice", "age": 25}
print(personne["nom"])
```

### Exceptions
```python
try:
    x = int("abc")
except ValueError:
    print("Erreur de conversion")
```

---

## 8. Installer un package Python spécifique

```bash
pip install requests
pip install flask
pip install numpy
```

---

## 9. Vérifier l'installation d'un module

```bash
python -c "import requests; print(requests.__version__)"
```

---

## 10. Aide-mémoire rapide

### Commandes de base
```bash
pwd
ls
cd
mkdir
rm
cp
mv
cat
grep
```

### Commandes Python
```bash
python --version
python nom_script.py
python -m venv .venv
pip install nom_paquet
pip freeze > requirements.txt
```

---

## 11. Conseils pratiques

- Utilise toujours un environnement virtuel pour les projets.
- Garde les dépendances dans `requirements.txt`.
- Teste tes scripts souvent.
- Lis l'erreur Python avant de corriger.
- Cherche toujours le message d'erreur exact.

---

## 12. Exemple de projet simple

```bash
mkdir mon_projet
cd mon_projet
python -m venv .venv
source .venv/bin/activate
pip install requests
python main.py
```

---

## 13. Syntaxe Windows / Linux

### Windows PowerShell
```powershell
Get-ChildItem
Set-Location
New-Item -ItemType Directory -Name dossier
```

### Linux
```bash
ls
cd
mkdir
```

---

## 14. Résumé

En résumé :
- `python` = exécuter Python
- `pip` = gérer les paquets Python
- `ls`, `cd`, `mkdir` = gérer les fichiers sous Linux
- `venv` = créer un environnement isolé
- `requirements.txt` = liste des dépendances du projet

---

## 15. Mini checklist

Avant de lancer un projet, vérifie :

```bash
python --version
pip --version
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```


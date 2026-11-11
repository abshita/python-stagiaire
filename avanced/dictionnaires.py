# Dictionnaires

personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

print(personne)
print("Nom:", personne["nom"])
print("Age:", personne["age"])

# Ajouter une clé
personne["metier"] = "Dev"
print("Après ajout:", personne)

# Modifier une valeur
personne["age"] = 26
print("Age mis à jour:", personne["age"])

# Supprimer une clé
personne.pop("ville")
print("Après suppression:", personne)

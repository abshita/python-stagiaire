# Niveau 5 - Projet Gestion Notes


def evaluer_note(note):
    if note >= 90:
        return "Très bien"
    elif note >= 75:
        return "Bien"
    elif note >= 60:
        return "Acceptable"
    else:
        return "À revoir"


notes = {
    "Alice": 95,
    "Bob": 82,
    "Charlie": 70,
    "Diana": 58,
    "Ethan": 88,
}

for nom, note in notes.items():
    resultat = evaluer_note(note)
    print(f"{nom}: {note} -> {resultat}")

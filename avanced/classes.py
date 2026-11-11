# Classes

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je m'appelle {self.nom} et j'ai {self.age} ans."


p1 = Personne("Alice", 25)
print(p1.se_presenter())

p2 = Personne("Bob", 30)
print(p2.se_presenter())

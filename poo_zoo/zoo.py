
from animal import Animal

class Zoo:
    def __init__(self, animaux=None):
        if animaux is None:
            animaux = []
        self.animaux = animaux

    def ajouter_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Seuls les objets de type Animal peuvent être ajoutés")
        self.animaux.append(animal)

    def lister_animaux(self):
        for animal in self.animaux:
            print(animal)  # utilise __str__ de Animal

    # Fusion de deux zoos
    def __add__(self, autre_zoo):
        if not isinstance(autre_zoo, Zoo):
            raise TypeError("On ne peut additionner qu'avec un autre Zoo")
        # Retourne un nouveau Zoo avec tous les animaux
        return Zoo(self.animaux + autre_zoo.animaux)

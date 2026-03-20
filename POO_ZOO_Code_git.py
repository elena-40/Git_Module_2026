
class Animal:     
    def __init__(self, nom: str, poids: float, taille: float):
        self._nom = nom
        self._poids = poids
        self._taille = taille

    def se_deplacer(self):
        pass
    
    def get_poids(self):
        return self._poids
    
    def set_poids(self, poids):
        if poids < 0:
            raise ValueError("Le poids ne peut pas être négatif")
        self._poids = poids

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = nom

    def __str__(self):
        return f"{self.get_nom()} - {self.get_poids()} kg"


class Serpent(Animal):
    def se_deplacer(self):
        print(self.get_nom(), "je rampe")


class Oiseau(Animal):
    def __init__(self, nom: str, poids: float, taille: float, altitude_max):
        super().__init__(nom, poids, taille)
        self.altitude_max = altitude_max 

    def se_deplacer(self):
        print(self.get_nom(), "peut voler jusqu'à", self.altitude_max, "mètres")


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
            print(animal)   # __str__ sera utilisé automatiquement

     # Méthode __add__ pour fusionner deux zoos
    def __add__(self, autre_zoo):
        if not isinstance(autre_zoo, Zoo):
            raise TypeError("On ne peut additionner qu'avec un autre Zoo")
        # Crée un nouveau Zoo avec la concaténation des listes d'animaux
        nouveaux_animaux = self.animaux + autre_zoo.animaux
        return Zoo(nouveaux_animaux)
        


# Programme principal
serpent = Serpent("AKA", 5, 200)
oiseau = Oiseau("Gugu", 1, 30, altitude_max=1000)
lion = Animal("Simba", 150, 120)
lapin = Animal("panpan", 20, 50)

mon_zoo = Zoo([serpent, oiseau])
mon_zoo.ajouter_animal(lion)

# Affichage
mon_zoo.lister_animaux()

# Zoo 1
zoo1 = Zoo([serpent, oiseau])

# Zoo 2
zoo2 = Zoo([lion])

# Zoo 3
zoo3 = Zoo([lapin])

# Fusion des zoos : zoo_final = zoo1 + zoo2 + zoo3
zoo_final = zoo1 + zoo2 + zoo3

# Affichage du zoo final
zoo_final.lister_animaux()
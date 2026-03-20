from animal import Animal

class Oiseau(Animal):
    def __init__(self, nom: str, poids: float, taille: float, altitude_max):
        super().__init__(nom, poids, taille)
        self.altitude_max = altitude_max 

    def se_deplacer(self):
        print(self.get_nom(), "peut voler jusqu'à", self.altitude_max, "mètres")



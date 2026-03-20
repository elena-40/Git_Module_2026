
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



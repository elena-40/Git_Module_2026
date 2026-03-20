
from animal import Animal
from serpant import Serpent
from oiseau import Oiseau
from zoo import Zoo
        


# Création des animaux
serpent = Serpent("AKA", 5, 200)
oiseau = Oiseau("Gugu", 1, 30, altitude_max=1000)
lion = Animal("Simba", 150, 120)
lapin = Animal("Panpan", 20, 50)

# Zoo 1
zoo1 = Zoo([serpent, oiseau])

# Zoo 2
zoo2 = Zoo([lion])

# Zoo 3
zoo3 = Zoo([lapin])

# Fusion des zoos
zoo_final = zoo1 + zoo2 + zoo3

# Affichage du zoo final
zoo_final.lister_animaux()
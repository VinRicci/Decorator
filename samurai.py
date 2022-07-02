from fighter import Fighter
import random


class Samurai(Fighter):
    def __init__(self):
        self.__hp: float = 100
        self.__ataque: float = 9
        self.__defensa: float = 9
        self.__velocidad: float = 15

    def __str__(self):
        return f"Samurai - HP {self.__hp} - Ataq {self.__ataque} - Def {self.__defensa} - Vel {self.__velocidad}\n"

    def set_vida(self, vida: float):
        self.__hp = vida
        return ""

    def obtener_hp(self):
        return self.__hp

    def obtener_ataque(self):
        return self.__ataque

    def obtener_defensa(self):
        return self.__defensa

    def obtener_velocidad(self):
        return self.__velocidad

    def reduce_hp(self, damage: float):
        vida = self.__decorated_fighter.obtener_hp() + damage
        self.__decorated_fighter.set_vida(vida)
        return vida

    def compute_damage(self, enemy: Fighter):
        soporta: float = random.uniform(0, self.__defensa)
        soporta -= enemy.obtener_ataque
        self.reduce_hp(soporta)
        return print(f"{soporta} de danio")

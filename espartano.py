import random
from fighter import Fighter


class Espartano(Fighter):
    def __init__(self):
        self.hp: float = 100
        self.ataque: float = 13
        self.defensa: float = 8
        self.velocidad: float = 10

    def __str__(self):
        print(f"Espartano - HP 100 ")
        print(f"- Ataq 13")
        print(f" - Def 8")
        print(f" - Vel 10")

    def obtener_hp(self):
        return self.__hp

    def obtener_ataque(self):
        return self.__ataque

    def obtener_defensa(self):
        return self.__defensa

    def obtener_velocidad(self):
        return self.__velocidad

    def reduce_hp(self, damage: float):
        self.__hp -= damage
        return self.__hp

    def compute_damage(self, enemy: Fighter):
        soporta: float = random.uniform(0, self.__defensa)
        soporta -= Fighter.obtener_ataque
        self.reduce_hp(soporta)
        return print(f"El danio de ataque es: {soporta}")

import random

from fighter import Fighter


class Vikingo(Fighter):
    def __init__(self):
        self.__hp: float = 100
        self.__ataque: float = 15
        self.__defensa: float = 6
        self.__velocidad: float = 10

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

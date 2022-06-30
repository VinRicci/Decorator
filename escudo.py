from fighterdecorator import FighterDecorator
from fighter import Fighter


class Escudo(FighterDecorator):
    def __init__(self):
        self.__defensa: float = 10.0
        self.__velocidad: float = -2.0

    def obtener_hp(self):
        pass

    def obtener_ataque(self):
        pass

    def obtener_defensa(self):
        return self.__defensa

    def obtener_velocidad(self):
        return self.__velocidad

    def reduce_hp(self, damage: float):
        pass

    def compute_damage(self, enemy: Fighter):
        pass

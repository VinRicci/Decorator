from fighterdecorator import FighterDecorator


class Espada(FighterDecorator):
    def __init__(self, fighterdecorator: FighterDecorator):
        super().__init__(fighterdecorator)
        self.__ataque: float = 8.0
        self.__hp: float = -2.0

    def __str__(self):
        return f"Espada - Ataq {self.__ataque} - HP {self.__hp}"

    def obtener_hp(self):
        return float(super().obtener_hp()+self.__hp)

    def obtener_ataque(self):
        return float(super().obtener_ataque()+self.__ataque)

from fighterdecorator import FighterDecorator


class Espada(FighterDecorator):
    def __init__(self, fighterdecorator: FighterDecorator):
        super().__init__(fighterdecorator)
        self.__ataque: float = 8.0
        self.__hp: float = -2.0

    @property
    def __str__(self):
        return print(f"Espada - Ataq {self.__ataque} - HP {self.__hp}")

    def obtener_hp(self):
        return super().obtener_hp()+self.__hp

    def obtener_ataque(self):
        return super().obtener_ataque()+self.__ataque

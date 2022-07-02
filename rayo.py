from fighterdecorator import FighterDecorator


class Rayo(FighterDecorator):
    def __init__(self, fighterdecorator: FighterDecorator):
        super().__init__(fighterdecorator)
        self.__ataque: float = -10.0
        self.__velocidad: float = 16.0

    @property
    def __str__(self):
        return print(f"Botas - Ataq {self.__ataque} - Vel {self.__velocidad}")

    def obtener_ataque(self):
        return super().obtener_ataque()+self.__ataque

    def obtener_velocidad(self):
        return super().obtener_velocidad()+self.__velocidad

from fighterdecorator import FighterDecorator


class Casco(FighterDecorator):
    def __init__(self, fighterdecorator: FighterDecorator):
        super().__init__(fighterdecorator)
        self.__defensa: float = 10.0
        self.__velocidad: float = -2.0

    @property
    def __str__(self):
        return print(f"Casco - Def {self.__defensa} - Vel {self.__velocidad}")

    def obtener_defensa(self):
        return super().obtener_defensa()+self.__defensa

    def obtener_velocidad(self):
        return super().obtener_velocidad()+self.__velocidad

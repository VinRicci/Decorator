from fighterdecorator import FighterDecorator


class Hongo(FighterDecorator):
    def __init__(self, fighterdecorator: FighterDecorator):
        super().__init__(fighterdecorator)
        self.__defensa: float = -6.0
        self.__hp: float = 12.0

    def __str__(self):
        return f"Hongos - Def {self.__defensa} - HP {self.__hp}"

    def obtener_hp(self):
        return super().obtener_hp()+self.__hp

    def obtener_defensa(self):
        return super().obtener_defensa()+self.__defensa

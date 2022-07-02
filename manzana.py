from fighterdecorator import FighterDecorator


class Manzana(FighterDecorator):
    def __init__(self, fighterdecorator: FighterDecorator):
        super().__init__(fighterdecorator)
        self.__defensa: float = -10.0
        self.__hp: float = 16.0

    @property
    def __str__(self):
        return print(f"Hongos - Def {self.__defensa} - HP {self.__hp}")

    def obtener_hp(self):
        return super().obtener_hp()+self.__hp

    def obtener_defensa(self):
        return super().obtener_defensa()+self.__defensa

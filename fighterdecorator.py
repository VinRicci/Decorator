from fighter import Fighter
import random


class FighterDecorator(Fighter):
    def __init__(self, fighter: Fighter):
        self.__decorated_fighter: Fighter = fighter

    @property
    def __str__(self):
        raise NotImplementedError

    def obtener_hp(self):
        return self.__decorated_fighter.obtener_hp()

    def obtener_ataque(self):
        return self.__decorated_fighter.obtener_ataque()

    def obtener_defensa(self):
        return self.__decorated_fighter.obtener_defensa()

    def obtener_velocidad(self):
        return self.__decorated_fighter.obtener_velocidad()

    def reduce_hp(self, damage: float):
        vida = self.__decorated_fighter.obtener_hp() + damage
        self.__decorated_fighter.set_vida(vida)
        return vida

    def compute_damage(self, enemy: Fighter):
        soporta: float = random.uniform(0, self.__decorated_fighter.obtener_defensa())
        soporta -= enemy.obtener_ataque()
        self.__decorated_fighter.reduce_hp(soporta)
        return f"El danio de ataque es: {soporta}"

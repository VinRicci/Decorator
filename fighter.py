from abc import ABCMeta
from abc import abstractmethod


class Fighter(metaclass=ABCMeta):
    @property
    def __str__(self):
        raise NotImplementedError

    @abstractmethod
    def obtener_hp(self):
        raise NotImplementedError

    @abstractmethod
    def obtener_ataque(self):
        raise NotImplementedError

    @abstractmethod
    def obtener_defensa(self):
        raise NotImplementedError

    @abstractmethod
    def obtener_velocidad(self):
        raise NotImplementedError

    @abstractmethod
    def reduce_hp(self, damage: float):
        raise NotImplementedError

    @abstractmethod
    def compute_damage(self, enemy):
        raise NotImplementedError

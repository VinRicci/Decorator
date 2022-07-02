from botas import Botas
from casco import Casco
from escudo import Escudo
from espada import Espada
from espartano import Espartano
from fighter import Fighter
from fighterdecorator import FighterDecorator
from gladiador import Gladiador
from hongo import Hongo
from manzana import Manzana
from mazo import Mazo
from rayo import Rayo
from samurai import Samurai
from vikingo import Vikingo


op: int = int(input(f"J1: Ingrese el tipo de peleador\n1.{Espartano.__class__.__name__}2.{Gladiador.__str__}"
                    f"3.{Samurai.__str__}4.{Vikingo.__str__}"))
peleador1: Fighter
if 1 == op:
    peleador1 = Espartano()
elif 2 == op:
    peleador1 = Gladiador()
elif 3 == op:
    peleador1 = Samurai()
elif 4 == op:
    peleador1 = Vikingo()
peleador1: FighterDecorator = FighterDecorator(peleador1)
op: int = int(input(f"J2: Ingrese el tipo de Item\n1.{Escudo.__str__}2.{Casco.__str__}3.{Espada.__str__}"
                    f"4.{Mazo.__str__}5.{Botas.__str__}6.{Rayo.__str__}7.{Hongo.__str__}8.{Manzana.__str__}"))
if 1 == op:
    peleador1 = Escudo(peleador1)
elif 2 == op:
    peleador1 = Casco(peleador1)
elif 3 == op:
    peleador1 = Espada(peleador1)
elif 4 == op:
    peleador1 = Mazo(peleador1)
elif 5 == op:
    peleador1 = Botas(peleador1)
elif 6 == op:
    peleador1 = Rayo(peleador1)
elif 7 == op:
    peleador1 = Hongo(peleador1)
elif 8 == op:
    peleador1 = Manzana(peleador1)

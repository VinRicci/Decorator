import os

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

op: int = int(input(f"J1: Ingrese el tipo de peleador\n1.{Espartano().__str__()}2.{Gladiador().__str__()}"
                    f"3.{Samurai().__str__()}4.{Vikingo().__str__()}"))
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
op: int = int(input(f"J2: Ingrese el tipo de Item\n1.{Escudo(FighterDecorator).__str__()}"
                    f"\n2.{Casco(FighterDecorator).__str__()}\n"
                    f"3.{Espada(FighterDecorator).__str__()} \n4.{Mazo(FighterDecorator).__str__()}"
                    f"\n5.{Botas(FighterDecorator).__str__()}"
                    f"\n6.{Rayo(FighterDecorator).__str__()}\n7.{Hongo(FighterDecorator).__str__()}\n"
                    f"8.{Manzana(FighterDecorator).__str__()}\n"))
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

op: int = int(input(f"J2: Ingrese el tipo de peleador\n1.{Espartano().__str__()}2.{Gladiador().__str__()}"
                    f"3.{Samurai().__str__()}4.{Vikingo().__str__()}"))
peleador2: Fighter
if 1 == op:
    peleador2 = Espartano()
elif 2 == op:
    peleador2 = Gladiador()
elif 3 == op:
    peleador2 = Samurai()
elif 4 == op:
    peleador2 = Vikingo()
peleador2: FighterDecorator = FighterDecorator(peleador2)
op: int = int(input(f"J2: Ingrese el tipo de Item\n1.{Escudo(FighterDecorator).__str__()}"
                    f"\n2.{Casco(FighterDecorator).__str__()}\n"
                    f"3.{Espada(FighterDecorator).__str__()} \n4.{Mazo(FighterDecorator).__str__()}"
                    f"\n5.{Botas(FighterDecorator).__str__()}"
                    f"\n6.{Rayo(FighterDecorator).__str__()}\n7.{Hongo(FighterDecorator).__str__()}\n"
                    f"8.{Manzana(FighterDecorator).__str__()}\n"))
if 1 == op:
    peleador2 = Escudo(peleador2)
elif 2 == op:
    peleador2 = Casco(peleador2)
elif 3 == op:
    peleador2 = Espada(peleador2)
elif 4 == op:
    peleador2 = Mazo(peleador2)
elif 5 == op:
    peleador2 = Botas(peleador2)
elif 6 == op:
    peleador2 = Rayo(peleador2)
elif 7 == op:
    peleador2 = Hongo(peleador2)
elif 8 == op:
    peleador2 = Manzana(peleador2)
print("Juego Iniciado")
os.system("pause")
print(f"J1 HP Actual: {peleador1.obtener_hp()}")
print(f"J2 HP Actual: {peleador2.obtener_hp()}")
os.system("pause")
while (peleador1.obtener_hp() > 0) and (peleador2.obtener_hp() > 0):
    print(f"J1: Ha recibido {peleador1.compute_damage(peleador2)}")
    print(f"J1 HP Actual: {peleador1.obtener_hp()}")
    os.system("pause")
    print(f"J2: Ha recibido {peleador2.compute_damage(peleador1)}")
    print(f"J2 HP Actual: {peleador2.obtener_hp()}")
    os.system("pause")
    print("Vida Actual")
    print(f"J1 HP: {peleador1.obtener_hp()}")
    print(f"J2 HP: {peleador2.obtener_hp()}")
    os.system("pause")

if peleador1.obtener_hp() <= 0:
    print("J2 Haz ganado")
else:
    print("J1 Haz ganado")

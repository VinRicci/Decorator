from espartano import Espartano
from fighter import Fighter
from fighterdecorator import FighterDecorator

peleador1: Fighter = Espartano()
peleador1 = FighterDecorator(peleador1)

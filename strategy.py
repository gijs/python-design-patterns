#!/usr/bin/env python

"""Examples of the strategy pattern.

A good way around inheritance and keeping functionality separate so it can be
used anywhere easily.

A great explanation of why composition (strategy pattern) is awesome:
http://berniesumption.com/software/inheritance-is-evil-and-must-be-destroyed/
"""


class Aircraft(object):
    def __init__(self, engine):
        self.engine = engine
    def start_engine(self):
        self.engine.start_engine()

class GasTurbineEngine(object):
    def __init__(self):
        pass
    def start_engine(self):
        print("Wrrrrrrrrrr!")

class RocketEngine(object):
    def __init__(self):
        pass
    def start_engine(self):
        print("Fshhhhhhhhhh")


engine = GasTurbineEngine()
plane = Aircraft(engine)
plane.start_engine()

class Jedi(object):
    def __init__(self, power_set):
        self.powers =  power_set

    def attack(self):
        self.powers.force_push()

class DarkJedi(Jedi):
    def attack(self):
        self.powers.force_choke()

class JediPowers(object):
    def force_push(self):
        print('Get out of here!')

class DarKJediPowers(JediPowers):
    def force_choke(self):
        print('Am I going to have to choke a bitch!?')


dark_powers = DarKJediPowers()
darth = DarkJedi(dark_powers)

jedi_powers = DarKJediPowers()
Obi = Jedi(jedi_powers)

darth.attack()
Obi.attack()


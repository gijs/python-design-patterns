#!/usr/bin/env python

"""Examples of the strategy pattern.

A good way around inheritance and keeping functionality separate so it can be
used anywhere easily.

A great explanation of why composition (strategy pattern) is awesome:
http://berniesumption.com/software/inheritance-is-evil-and-must-be-destroyed/
"""


class AirVehicle(object):
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start_engine()


class GroundVehicle(object):
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        self.engine.start_engine()


class GasTurbineEngine(object):
    """
    This class can be developed independently of its "container" class.
    """

    def start_engine(self):
        print("Wrrrrrrrrrr!")


if __name__ == '__main__':
    engine1 = GasTurbineEngine()
    raptor = AirVehicle(engine1)
    raptor.start_engine()

    engine2 = GasTurbineEngine()
    abrams = GroundVehicle(engine2)
    abrams.start_engine()
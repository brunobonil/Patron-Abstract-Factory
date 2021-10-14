from abstractFactory import AbstractFactory
from concreteFactory import *


class Cliente():

    def __init__(self, factory):
        self.factory = factory
        self.remera = factory.createRemera()
        self.pantalon = factory.createPantalon()
        self.calzado = factory.createCalzado()

if __name__ == '__main__':

    factory = CasualRemera()
    c1 = Cliente(factory)
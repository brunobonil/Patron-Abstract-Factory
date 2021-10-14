from abstractFactory import AbstractFactory
from productos import *
from deporteFactory import *
from casualFactory import *
from formalFactory import *

class CasualRemera(AbstractFactory):

    def createRemera(self):
        return RemeraCasual()
    
    def createPantalon(self):
        return PantalonCasual()

    def createCalzado(self):
        return CalzadoCasual()


class DeporteRemera(AbstractFactory):

    def createRemera(self):
        return RemeraDeporte()
    
    def createPantalon(self):
        return PantalonDeporte()

    def createCalzado(self):
        return CalzadoDeporte()


class FormalRemera(AbstractFactory):

    def createRemera(self):
        return RemeraFormal()
    
    def createPantalon(self):
        return PantalonFormal()

    def createCalzado(self):
        return PantalonFormal()
from productos import *

class RemeraDeporte(Remera):
    def __init__(self):
        super().__init__()
        print(' Deportiva')

class PantalonDeporte(Pantalon):
    def __init__(self):
        super().__init__()
        print(' Deportivo')

class CalzadoDeporte(Calzado):
    def __init__(self):
        super().__init__()
        print(' Deportivo')
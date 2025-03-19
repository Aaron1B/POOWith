class Vehiculo:
    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color
    
    class Coche(Vehiculo):
        def __init__(self, ruedas, color, velocidad, cilindrada):
            super().__init__(ruedas, color)
            self.velocidad = velocidad
            self.cilindrada = cilindrada
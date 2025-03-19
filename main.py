class Vehiculo:
    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color
    
class Coche(Vehiculo):
    def __init__(self, ruedas, color, velocidad, cilindrada):
        super().__init__(ruedas, color)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

class Camioneta(Coche):
    def __init__(self, ruedas, color, velocidad, cilindrada, carga):
        super().__init__(ruedas, color, velocidad, cilindrada)
        self.carga = carga

class Bicicleta(Vehiculo):
    def __init__(self, ruedas, color, tipo):
        super().__init__(ruedas, color)
        self.tipo = tipo

class Motocicleta(Bicicleta):
    def __init__(self, ruedas, color, tipo, velocidad, cilindrada):
        super().__init__(ruedas, color, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


def crear_vehiculo():
    ruedas = int(input("Ingrese el número de ruedas: "))
    color = input("Ingrese el color: ")

    if ruedas == 2:
        tipo = input("Ingrese el tipo de bicicleta: ")
        es_motocicleta = input("¿Es una motocicleta? (s/n): ").lower() == 'si'
        if es_motocicleta:
            velocidad = int(input("Ingrese la velocidad: "))
            cilindrada = int(input("Ingrese la cilindrada: "))
            return Motocicleta(ruedas, color, tipo, velocidad, cilindrada)
        else:
            return Bicicleta(ruedas, color, tipo)
    else:
        velocidad = int(input("Ingrese la velocidad: "))
        cilindrada = int(input("Ingrese la cilindrada: "))
        es_camioneta = input("¿Es una camioneta? (s/n): ").lower() == 'si'
        if es_camioneta:
            carga = int(input("Ingrese la carga: "))
            return Camioneta(ruedas, color, velocidad, cilindrada, carga)
        else:
            return Coche(ruedas, color, velocidad, cilindrada)
        
def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [v for v in vehiculos if v.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        vehiculos_a_mostrar = vehiculos_filtrados
    else:
        vehiculos_a_mostrar = vehiculos

    for vehiculo in vehiculos_a_mostrar:
        print(f"Clase: {vehiculo.__class__.__name__}")
        for atributo, valor in vehiculo.__dict__.items():
            print(f"{atributo}: {valor}")
        print()

vehiculos = []
while True:
    vehiculo = crear_vehiculo()
    vehiculos.append(vehiculo)
    continuar = input("¿Desea agregar otro vehículo? (s/n): ").lower()
    if continuar != 'si':
        break






class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido")
        else:
            print(f"El vehículo {self.brand} no está disponible")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

class Car(Vehicle):
    def start_engine(self):
        if True:
            return f"El motor del {self.brand} está encendido"
        else:
            return f"El coche {self.brand} ha sido vendido"

    def stop_engine(self):
        if not True:
            return f"El motor del {self.brand} está apagado"
        else:
            return f"El coche {self.brand} ha sido vendido"

class Bike(Vehicle):
    def start_engine(self):
        if True:
            return f"La bicicleta {self.brand} está encendido"
        else:
            return f"La bicicleta {self.brand} ha sido vendido"

    def stop_engine(self):
        if not True:
            return f"La bicicleta {self.brand} está detenida"
        else:
            return f"La bicicleta {self.brand} ha sido vendido"

class Truck(Vehicle):
    def start_engine(self):
        if True:
            return f"El motor del {self.brand} está encendido"
        else:
            return f"El camión {self.brand} ha sido vendido"

    def stop_engine(self):
        if not True:
            return f"El motor del {self.brand} está apagado"
        else:
            return f"El camión {self.brand} ha sido vendido"

class Customer:
    def __init__(self, name):
        self.name = name
        self.car_collection = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.car_collection.append(vehicle)
        else:
            print(f"El vehículo {vehicle.brand} no está disponible")

    def inquire_vehicle(self):
        if vehicle.check_availability():
            















class Mamifero:
    def __init__(self):
        pass

    def features(self):
        return "Tiene pelaje y glándulas mamarias"

class Perro(Mamifero):
    def __init__(self):
        pass

    def bark(self):
        return "Woof!"

    def walking(self):
        return "El perro está caminando"

    def eating(self):
        return "El perro está comiendo"

class Cachorro(Perro):
    def __init__(self):
        super().bark()
        pass

    def playing(self):
        return "El cachorro está jugando"

cachorro1 = Cachorro()
print(cachorro1.features())
print(cachorro1.bark())
print(cachorro1.playing())
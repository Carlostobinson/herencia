from classanimal import animal 
class ave (animal):

    def __init__(self,nombre, peso, nacimiento, propietario):
        super().__init__(nombre,peso)
        self.nacimiento = nacimiento
        self.propietario = propietario
        
    def calcularedad(self):
            edad= 2024*self.nacimiento
            print (edad)
ave1 = ave("paloma",2,2014,"carlos")
ave1.calcularedad()
ave1.imprimirnombre()


class Cuil:
    def __init__(self,tipoPersona,dni):
        self.valor1 = str(tipoPersona) + str(dni)
        self.valor2 = [5,4,3,2,7,6,5,4,3,2]
        self.index = 0
    
    def calcular(self):
        valor3 = 0
        for caracter in self.valor1:
            valor3 += int(caracter) * self.valor2[self.index]
            self.index += 1

        valor3 = valor3 / 11
        valor3 = int(11 - valor3)
        self.valor1 += str(valor3)

    # Esta funcion no es necesario. Pero queda facherita....
    def getCuil(self):
        self.index = 0
        cuil = ""
        for elemento in self.valor1:
            if self.index == 2 :
                cuil += "-"
                cuil += elemento
            else:
                cuil +=elemento
            self.index +=1
        print(cuil)


cuil = Cuil(27,12817672)
cuil.calcular()
cuil.getCuil()
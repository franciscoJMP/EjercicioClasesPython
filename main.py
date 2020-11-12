import math

class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y



class Forma:
    def __init__(self,Coordenada,color,nombreForma):
        self.color=color
        self.nombreForma=nombreForma
        self.Coordenada=Coordenada

    def imprimir(self):
        print("Forma->" + self.nombreForma)
        print("Color->"+self.color)
        print("Coordeanda X->"+str(self.Coordenada.x))
        print("Coordeanda Y->" + str(self.Coordenada.y))


    def cambiarColor(self,color):
        self.color=color

    def cambiarForma(self,Coordenada):
        self.Coordenada=Coordenada

    def obtenerColor(self):
        return self.color

class Rectangulo(Forma):
    def __init__(self,Coordenada,color,nombreForma,lMenor,lMayor):
        super().__init__(Coordenada,color,nombreForma)
        self.lMenor=lMenor
        self.lMayor=lMayor

    def imprimir(self):
        super().imprimir()
        print("Lado menor->"+str(self.lMenor))
        print("Lado mayor->"+str(self.lMayor))

    def calcularArea(self):
        area=self.lMenor*self.lMayor
        return area

    def calcularPerimetro(self):
        perimetro=2*self.lMenor+2*self.lMayor
        return perimetro

    def cambiarTamanio(self,factorEscala):
        self.lMayor=self.lMayor*factorEscala
        self.lMenor=self.lMenor*factorEscala

class Elipse(Forma):
    def __init__(self,Coordenada,color,nombreForma,radioMayor,radioMenor):
        super().__init__(Coordenada,color,nombreForma)
        self.radioMayor=radioMayor
        self.radioMenor=radioMenor

    def imprimir(self):
        super().imprimir()
        area = math.pi * self.radioMayor * self.radioMenor
        print("Area del "+self.nombreForma+"-> " + str(area))



class Cuadrado(Rectangulo):
    def __init__(self,Coordenada,color,nombreForma,lMenor,lMayor):
        super().__init__(Coordenada, color, nombreForma,lMenor,lMayor)


class Circulo(Elipse):
    def __init__(self,Coordenada,color,nombreForma,radioMayor,radioMenor):
        super().__init__(Coordenada,color,nombreForma,radioMayor,radioMenor)





Punto1=Punto(2,2)
Rectangulo1 = Rectangulo(Punto1,"Amarillo","Rectangulo",3,4)
Punto2=Punto(4,2)
Cuadrado1= Cuadrado(Punto2,"Rojo","Cuadrado",4,5)
Punto3=Punto(2,6)
Circulo1=Circulo(Punto3,"Verde","Circulo",4,9)

Rectangulo1.imprimir()
print("--------------------------------------------")
print()
color=Rectangulo1.obtenerColor()
print("El color del Rectangulo es "+color)
print()
Punto4=Punto(5,4)

Rectangulo1.cambiarForma(Punto4)
Rectangulo1.imprimir()
print("--------------------------------------------")
print()

print("El area del Rectangulo es "+str(Rectangulo1.calcularArea()))
print("El perimetro del Rectangulo es "+str(Rectangulo1.calcularPerimetro()))
Rectangulo1.cambiarTamanio(2)
print("Rectangulo con la forma cambiada")
Rectangulo1.imprimir()

print("--------------------------------------------")
print()
print("Creando otras formas")


tupla=(Rectangulo1,Cuadrado1,Circulo1)
x=2
y=2
for forma in tupla:
    forma.color="Amarillo"
    PuntoForma=Punto(x,y)
    forma.cambiarForma(PuntoForma)
    x=x+1
    y=y+1
    forma.imprimir()
    print("--------------------------------------------")
    print()



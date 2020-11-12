class Empleado:

    def __init__(self,nombre, apellidos, dni, direccion,antiguedad,telefono,salario,puesto,Supervisor):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.antiguedad=antiguedad
        self.telefono=telefono
        self.salario=salario
        self.puesto=puesto
        self.Supervisor=Supervisor

    def imprimir(self):
        nombreSupervisor="No tiene"

        if self.Supervisor is not None:
            nombreSupervisor=self.Supervisor.nombre

        print("Nombre->"+self.nombre)
        print("Apellidos->"+self.apellidos)
        print("DNI->"+self.dni)
        print("Direccion->"+self.direccion)
        print("Antiguedad->" + str(self.antiguedad)+" años")
        print("Telefono->" + self.telefono)
        print("Salario->" + str(self.salario))
        print("Puesto->"+self.puesto)
        print("Supervisor->"+nombreSupervisor)

    def cambiarSupervisor(self,Supervisor):
        self.Supervisor=Supervisor
    def incrementarSalario(self,incremento):
        salarioaIncrementar=self.salario*incremento/100
        self.salario+=salarioaIncrementar

class Coche:
    def __init__(self,matricula,marca,modelo):
        self.matricula=matricula
        self.marca=marca
        self.modelo=modelo

class Secretario(Empleado):
    def __init__(self,nombre, apellidos, dni, direccion,antiguedad,telefono,salario,puesto,Supervisor,despacho,numFax,incremento):
        super().__init__(nombre, apellidos, dni, direccion,antiguedad,telefono,salario,puesto,Supervisor)
        self.despacho=despacho
        self.numFax=numFax
        self.incremento=incremento


    def incrementarSalario(self):
        salarioaIncrementar=self.salario*self.incremento/100
        self.salario+=salarioaIncrementar
class Vendedor(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, antiguedad, telefono, salario,puesto, Supervisor,Coche,telfMovil,areaVenta,comision,incremento):
        super().__init__(nombre, apellidos, dni, direccion, antiguedad, telefono, salario,puesto, Supervisor)
        self.listaCliente = []
        self.incremento = incremento
        self.Coche=Coche
        self.telfMovil=telfMovil
        self.areaVenta=areaVenta
        self.comision=comision
    def incrementarSalario(self):
        salarioaIncrementar=self.salario*self.incremento/100+self.comision
        self.salario+=salarioaIncrementar

    def altaCliente(self,cliente):
        self.listaCliente.append(cliente)
    def bajaCliente(self,cliente):
        self.listaClientes.remove(cliente)
    def cambiarCoche(self,Coche):
        self.Coche=Coche

class JefeZona(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, antiguedad, telefono, salario,puesto, Supervisor,Secretario,Coche,incremento):
        super().__init__(nombre, apellidos, dni, direccion, antiguedad, telefono, salario,puesto, Supervisor)
        self.listaVendedores = []
        self.Secretario=Secretario

        self.Coche=Coche
        self.incremento=incremento

    def incrementarSalario(self):
        salarioaIncrementar=self.salario*self.incremento/100
        self.salario+=salarioaIncrementar
    def cambiarSecretario(self,Secretario):
        self.Secretario=Secretario

    def cambiarCoche(self,Coche):
        self.Coche=Coche

    def altaVendedor(self, Vendedor):
        self.listaVendedores.append(Vendedor)

    def bajaVendedor(self, Vendedor):
        self.listaVendedores.remove(Vendedor)


class Cliente:
    def __init__(self,nombre,apellido,dni):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni

Coche1=Coche("11111","Peugeot","308")
Coche2=Coche("11111","Dacia","Logan")
Coche3=Coche("11111","Citroen","Xsara")

Cliente1=Cliente("Ramon","Cortes","999999")
Cliente2=Cliente("Rafael","Sanchez","999999")
Cliente3=Cliente("Marta","Jimenez","999999")

Secretario1=Secretario("Ana","Cortes","42342342b","C/Alamos",2,"953666666",1580,"Secretaria Jefe de Ventas",None,"Despacho 1","97987",10)
Secretario1.imprimir()

print("Incremento de salario para "+Secretario1.nombre+" salario Antiguo: "+str(Secretario1.salario))
Secretario1.incrementarSalario()
print("Salario incrementado: "+str(Secretario1.salario))
print("---------------------------------------")
JefeZona1=JefeZona("Raul","Garcia","7593247359b","C/Avd Andalucia",3,"7435983247",2500,"Jefe de Ventas",None,Secretario1,Coche2,20)
JefeZona1.imprimir()
print("El secretario de "+JefeZona1.nombre+" es "+JefeZona1.Secretario.nombre)
print ("El coche de "+JefeZona1.nombre+" es un "+JefeZona1.Coche.marca+" "+JefeZona1.Coche.modelo)
print("El salario del jefe "+JefeZona1.nombre+" es "+str(JefeZona1.salario)+"€")
JefeZona1.incrementarSalario()
print("Su salario incrementado es "+str(JefeZona1.salario)+"€")
print("---------------------------------------")
Vendedor1 = Vendedor("Antonio","Panzuela","8023749B","C/Avad.Europa",2,"79832798",2,"Vendedor Informatica 1",JefeZona1,Coche3,"655677467","Informatica",5,5)
Vendedor1.imprimir()
Vendedor1.altaCliente(Cliente1)
Vendedor1.altaCliente(Cliente2)
Vendedor1.altaCliente(Cliente3)
print("Clientes del Vendedor "+Vendedor1.nombre)
listaClientes=Vendedor1.listaCliente

for i in listaClientes:
    Cliente4=i
    print(Cliente4.nombre+" "+Cliente4.apellido)

Vendedor2 = Vendedor("Juan Jose","Olmo","8023749B","C/Avad.Europa",2,"79832798",2,"Vendedor Informatica 1",JefeZona1,Coche3,"655677467","Informatica",5,5)
Vendedor3 = Vendedor("Francisco Jose","Daban","8023749B","C/Avad.Europa",2,"79832798",2,"Vendedor Informatica 1",JefeZona1,Coche3,"655677467","Informatica",5,5)
Vendedor4 = Vendedor("Cristian","Guzman","8023749B","C/Avad.Europa",2,"79832798",2,"Vendedor Informatica 1",JefeZona1,Coche3,"655677467","Informatica",5,5)
JefeZona1.altaVendedor(Vendedor1)
JefeZona1.altaVendedor(Vendedor2)
JefeZona1.altaVendedor(Vendedor3)
JefeZona1.altaVendedor(Vendedor4)

print("El jefe "+JefeZona1.nombre+" tiene a su cargo a los siguientes Vendedores: ")
listaVendedores=JefeZona1.listaVendedores
for i in listaVendedores:
    print(i.nombre+" "+i.apellidos)





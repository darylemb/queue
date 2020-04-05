#Ejercicio 2. Practica Queue por Daryl Mendoza
import Queue
class Warehouse():   #Clase creada almacen para resolver el problema planteado
    qPackets = Queue.LifoQueue() #atributo queue tipo LiFo para guardar los paquetes
    qMoney = Queue.LifoQueue()   #atributo queue tipo LiFo para llevar el registro de deuda

    def add(self,packets,price): #método agregar o compra, en el cual se agregan a los queues los valores que se ingresarán por consola
        for i in range(packets):
            self.qPackets.put(1)

    def sub(self,packets,price):  #método sustraer o vender, en el que se eliminan de los queues los valores que se ingresan por consola
        for i in range(packets):
            self.qPackets.get(1)

    def totalData(self): #método de información que mostrará por pantalla el contenido final de los queues
        print("The total packets is: ",self.qPackets.qsize())
        print("the debt is:",self.qMoney.qsize(),"\n")

warehouse = Warehouse() #Se crea una instancia de Clase Warehouse
week = ["monday","tuesday","wednesday","thursday","friday","saturday"] #Array con los días de la semana para mejor presentación
for i in range(0,len(week)): #Ciclo que registra la información por día de la semana
    print("SELECT THE OPTION FOR ",(week[i].upper())) 
    print("Select a number\n1. Purchase data\n2. Sale data\n")
    option = int(input())  #Selección de opción: Compra de paquetes o venta de paquetes, hay dos entradas, 1 o 2
    print("\n")
    if option == 1: #Compra de paquetes
        print("option selected: purchase")
        print("Write the number of packets")
        packets = int(input()) 
        print("Write the price for packet") 
        price = int(input())
        warehouse.add(packets,price) #Agrega a los queues del objeto mediante el método add
    if option == 2:
        print("option selected: sale")
        print("Write the number of packets")
        packets = int(input())
        print("Write the price for packet") 
        price = int(input())
        warehouse.sub(packets,price)#Elimina de los queues del objeto mediante el método sub

print("\nTOTAL AT THE END OF THE WEEK:\n")
warehouse.totalData() #Se llama al método totalData para mostrar el contenido total de paquetes y deuda, resolviendo el problema

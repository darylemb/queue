#Ejercicio 1. Práctica Queue por Daryl Mendoza
import Queue #modulo a practicar
q = Queue.Queue()#se crea el queue tipo FIFO

for i in range(3): #El ejercicio indica un rango de 3 elementos a introducir en el queue
    print("Salary perception: ")
    q.put(int(input()))#Se forza a entero ya que el valor por defecto de put es String
x = q.qsize()#Este método devuelve el número de elementos del queue (en este caso, 3)
sum = 0 #Varibale que ayudará a obtener la suma de los elementos del queue
while not q.empty(): #Esta linea indica un ciclo que se repetirá mientras el queue no esté vacío
    sum = sum + q.get()#Se realiza la suma de los elementos del queue
print("Average salary: ")
print(sum/x)#Se muestra el promedio de los salarios registrados

import os  #Se importa el modulo para poder limpiar la consola.
# Clase que representa al registro como tal 
class Registro:   
    students = []

    #El metodo menu, es el corazon del programa la pantalla principal.
    #Es el flujo de ejecucion del programa.
    def Menu(self):
        
        while True:
        
            print("Bienvenid@ al Registro")
            print("1. Agregar Estudiante\n2. Eliminar Estudiante\n3. Mostrar Estudiantes\n4. Salir ") 
            
            try:
                #Se toma el valor de la "decision" de lo que quiere hacer el usuario
                choices = int(input("Seleccione la opción que desea realizar: "))
            except:
                choices=5 #Significa que el usuario introdujo una letra o un valor fuera de los parametros y lo convierto en un numero
            if choices == 1:
                self.AgregarEstudiante()
            elif choices == 2:
                self.EliminarEstudiante()
            elif choices == 3:
                self.MostrarEstudiante()
            elif choices == 4:
                print("Gracias por usar, saliendo")
                break
            else:   
                os.system("cls")
            
    #Permite agregar un estudiante al registro.
    def AgregarEstudiante(self):
        #El usuario introduce los datos del estudiante.
        s = Estudiante()
        s.name = input("Introduce un nombre: ")
        s.lastname = input("Introduce un apellido: ")
        s.ci = input("Introduce Cédula: ")
        s.career = input("Introduce la carrera cursante: ")
        s.ncareer = input("Introduce el trimestre cursante: ")
        #Luego de tomar los datos, se agrega a "students".
        self.students.append(s)
        
        os.system("cls")
    #Permite eliminar a un estudiante por un numero asignado.
    def EliminarEstudiante(self):
        while True:
            #Se inicia el metodo de mostrar estudiante para que el usuario decida a que estudiante desea eliminar
            self.MostrarEstudiante()
            
            try:
                #Se toma el numero ingresado por el usuario
                erase = int(input("Introduce el numero del estudiante que deseas eliminar: "))
                self.students.pop(erase-1) # Y se elimina de la lista
                print("Estudiante eliminado exitosamente")
                break
            except:
                #Si el numero ingresado no está asignado a ningun estudiante 
                print("El estudiante no existe") 
                break

    #Metodo Para mostrar en pantalla los estudiantes registrados.
    def MostrarEstudiante(self):
        os.system("cls")
        contador = 1 #Contador que nos ayudará a asignar un valor numerico a cada estudiante
        for busqueda in self.students: #Se crea un bucle "for" que recorre students para imprimir en pantalla los estudiantes registrados
            #Se imprime en pantalla todos los estudiantes registrados
            print(f"{contador}. {busqueda.name} {busqueda.lastname} C.I:{busqueda.ci} Carrera: {busqueda.career}")
            contador+=1

class Estudiante:
    #Método especial que se llama al instanciar la clase, guardará los datos de los estudiantes.
    def __init__(self):
        self.name = " "     #Nombre del Estudiante.
        self.lastname = " " #Apellido del Estudiante.
        self.ci = " "       #Cedula de Identidad del Estudiante.
        self.career = " "   #Carrera del Estudiante.
        self.ncareer = " "  #Trimestre Cursante del Estudiante.

x = Registro() #Se instancia la clase registro.
os.system("cls")
x.Menu() #Muestra en pantalla el metodo menu, donde el usuario podrá seleccionar la accion que desee.
os.system("cls")

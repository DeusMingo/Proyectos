import os
class Usuario:
    def __init__(self, nombre, apellido, cedula, password, cuenta, saldo, guia, valort):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.password = password  # Contraseña del usuario 
        self.cuenta = cuenta
        self.saldo = saldo
        self.guia = guia  # Sirve para ubicar a cada usuario en la lista
        self.valort = valort  # Variable para las Transacciones 

    def ConsultaUsuario(self):
        print("Usuario: " + self.nombre + " " + self.apellido)
        print("Su Nro. de Cuenta: ", self.cuenta)
        print("Saldo Actual: ", self.saldo)

class BancoVenezuela:
    def __init__(self):
        # Lista donde iran almacenados los clientes
        self.userdirectorio = []

    def Interfaz(self):

        while True:
            
            print("""\n=== Bienvenido al Banco de Venezuela ===\n
            ¿Qué desea realizar?\n
            1) Registrar Cuenta
            2) Iniciar Sesión
            3) Salir del programa\n""")
            try:
                #Se toma el valor de la "decision" de lo que quiere hacer el usuario
                choices = int(input("Seleccione la opción que desea realizar: "))
            except:
                choices=5 #Significa que el usuario introdujo una letra o un valor fuera de los parametros y lo convierto en un numero  
            if choices == 1:
                self.Registrar()
            elif choices == 2:
                self.InicioSesion()
            elif choices == 3:
                print("Gracias por usar, saliendo")
                quit()
                break
            else:   
                os.system("cls")

    def Registrar(self):
        nombre = input("Introduzca su nombre: ")
        apellido = input("Introduzca su apellido: ")
        #Se usa la funcion strip para eliminar espacios vacios en el string y no tener problemas después para la verificación
        comprobacion = True
        while comprobacion:
            cedula = str(input("Introduzca su cedula (Sin puntos): ")).strip()
            comprobacion = False
            for busqueda in self.userdirectorio:
                if cedula == busqueda.cedula:
                    print("Esta cédula ya está en uso, por favor introduzca una nueva")
                    comprobacion = True
        password = str(input("Introduzca la contraseña para poder acceder a su cuenta: ")).strip()
        # Constructor del usuario con el que vamos a manejar todos los datos
        persona = Usuario(nombre, apellido, cedula, password, len(self.userdirectorio) + 1, 100,
                            len(self.userdirectorio), valort=0)  # Inicia todos los valores vacios y la cuenta en 100
        self.userdirectorio.append(persona)
        print()
        print("------------------------------------------")
        print("""\n=== Registro De Cuenta Exitoso ===\n""")
        print("------------------------------------------")
        print()

    def InicioSesion(self):
        # Uso strip para comprobar los datos introducidos con la lista 
        ci = str(input("Ingrese su número de cédula: ")).strip()
        contra = str(input("Ingrese contraseña: ")).strip()

        # Se verifica si el numero guia corresponde al del cliente (Sirve de verificador)
        guia = -1
        for cliente in self.userdirectorio:
            if ci == cliente.cedula and contra == cliente.password:
                guia = cliente.guia
        if guia == -1:
            print("El usuario ingresado no existe, volviendo al menu principal")

        else:
            persona = self.userdirectorio[guia]
            login = True
            # login como booleano para validar si desea hacer otra transaccion, sino se usa otro break
            while login:
                print("\nBienvenido", persona.nombre + " " + persona.apellido, "que desea realizar?\n"
                                                                                               "1. Deposito\n"
                                                                                               "2. Retiro\n"
                                                                                               "3. Consulta\n"
                                                                                               "4. Cerrar sesion\n")
              
                opcion = input("> ")
                if opcion == '1':
                    self.Deposito(persona)
                elif opcion == '2':
                    self.Retiro(persona)
                elif opcion == '3':
                    persona.ConsultaUsuario()
                elif opcion == '4':
                    print("Cerrando Sesión...\n")
                    break
                else:
                    print("\nHas introducido un comando inválido")
                    

    def Retiro(self, persona):

        print("Opción de retiro")
        while True:
            try:
                valort = int(input("Por favor seleccione el monto a retirar: "))
            except:
                print("Monto invalido")
                
                
            if persona.saldo - 100 >= valort:
                persona.saldo -= valort
                print("Operación realizada exitosamente")
                print("Saldo disponible: ",persona.saldo)
                return
            else:
                print("Saldo insuficiente para esta operación")
                break

    def Deposito(self, persona):
        print("Opción de deposito")
        while True:
            try:
                valort = int(input("Ingrese el monto a depositar: "))
                
            except:
                print("Monto invalido")
                  
            if valort <= 100000:        
                persona.saldo += valort
                print("Operación realizada exitosamente")
                print("Saldo disponible:", persona.saldo)
                return
            else:
                print("Transacción cancelada. El monto máximo de depósito es 100.000")
                break

banco = BancoVenezuela()
banco.Interfaz()
input()

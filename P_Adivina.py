import msvcrt
import random

# Definir parametros

ADVERTENCIA1 = "El rango de número a adivinar se encuentra desde el 1 hasta el ...?..."
ADVERTENCIA2 = "En cuantos intentos estimas adivinarlo..."
ADVERTENCIA3 = "Qué número es?..."

def pedir_numero(mensaje):
   """Retorna un número ingresado por el usuario"""
   ingreso = 0
   numero = False
   while not numero:
             try:
                 ingreso = int(input(mensaje))
                 numero = True
             except ValueError:
                 print ("\n Solo números por favor:")
             except KeyboardInterrupt:
                 print ("\n Hasta luego!")
                 exit()
             except:
                 print ("\n Error imprevisto")
                 exit()
             return ingreso

def generar_numero(l=0):
    rango = random.randint(1, l) # Genera al azar el número partiendo del rango indicado
    return rango

def main():
    cont = 0 #Contador para cerrar el ciclo
    i = pedir_numero(ADVERTENCIA1)
    j = generar_numero(i)
    k= pedir_numero(ADVERTENCIA2)
    cont = int(cont)
    while cont != k:
        l= pedir_numero(ADVERTENCIA3)
        if l == j: # El ciclo acaba si es correcto el número
            cont = k
            print ("Buen trabajo lo has acertado")
        else: # Ha ingresado número incorrecto, se acumula el contador y se decrementa el número de intentos
            cont += 1
            print ("Número errado,   Tiene", k- cont, "  intentos más")

            print ("El número es", j) # Impresión del valor oculto
            print ("Game Over")

            if __name__ == "__main:__":
                main()

            main()

msvcrt.getch() #La ventana de ejecución se mantendrá abierta hasta que se presione alguna tecla

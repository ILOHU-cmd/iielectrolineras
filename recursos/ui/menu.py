import os 
import sys
from recursos.grafos.constructor import construir_grafo  

def limpiar_pantalla():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")

def mostrar_menu():
    print("MENU DE OPCIONES")
    print("1. Cargar o construir el grafo vial")
    print("2. Ver electrolineras, puntos de referencia y vehiculos")
    print("3. Ejecutar simulacion de recorridos")
    print("4. Ver resumen estadistico")
    print("5. Generar mapa interactivo")
    print("6. Entrenar modelos de Machine Learning")
    print("7. Predecir electrolinera con ML")
    print("8. Exportar historial a Excel")
    print("9. Comparar Dijkstra y ML")
    print("0. Salir")
    print()


def opcion1():
    construir_grafo()



    
def opcion2():
    print("ver electrolineras, puntos de referencia y vehiculos")



def opcion3():
    print("Has seleccionado la Opción 1.")

def opcion4():
    print("Has seleccionado la Opción 1.")


def opcion5():
    print("Has seleccionado la Opción 1.")

def opcion6():
    print("Has seleccionado la Opción 1.")

def opcion7():
    print("Has seleccionado la Opción 1.")

def opcion8():
    print("Has seleccionado la Opción 1.")

def opcion9():
    print("Has seleccionado la Opción 1.")


def ejecutar_menu():

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        match opcion:
            case "1": 
                opcion1()
            case "2":   
                opcion2()
            case "3":   
                opcion3()
            case "4":   
                opcion4()
            case "5":   
                opcion5()
            case "6":
                opcion6()
            case "7":
                opcion7()
            case "8":
                opcion8()
            case "9":
                opcion9()
            case "0":
                print("Saliendo del programa.")
                break
            case _: 
                print("Opción no válida. Por favor, seleccione una opción válida.")
            
        print(input("Presione Enter para continuar..."))
                

# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

def ej3():
    print('Ejercicio de archivos CSV 1º')
    archivo = 'stock.csv'
    
    # Realice un programa que abra el archivo 'stock.csv'
    # en modo lectura y cuente el stock total de tornillos
    # a lo largo de todo el archivo, 
    # sumando el stock en cada fila del archivo

    # Para eso debe leer los datos del archivo
    # con "csv.DictReader", y luego recorrer los datos
    # dentro de un bucle y solo acceder a la columna "tornillos"
    # para cumplir con el enunciado del ejercicio

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    with open(archivo) as stock:
        archivo_stock = list(csv.DictReader(stock))

    suma = 0

    for i in range(len(archivo_stock)):
        producto = archivo_stock[i]
        for k,v in producto.items():
            if k == "tornillos":
                suma = suma + int(v)

    print("Existen {} tornillos en total".format(suma))


def ej4():
    print('Ejercicios con archivos CSV 2º')
    archivo = 'propiedades.csv'

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrar dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # NOTA: Si desea investigar puede evitar que el programa explote
    # utilizando "try except", tema que se verá la clase que viene.

    # Comenzar aquí, recuerde el identado dentro de esta funcion

    with open(archivo) as propiedades:
        lista_propiedades = list(csv.DictReader(propiedades))
    
    depto_2ambientes = 0
    depto_3ambientes = 0
    depto_sin_ambientes = 0

    for i in range(len(lista_propiedades)):
        props = lista_propiedades[i]
        for k,v in props.items():
            if k == "ambientes":
                try:
                    if int(v) == 2:
                        depto_2ambientes = depto_2ambientes + 1
                    if int(v) == 3:
                        depto_3ambientes = depto_3ambientes + 1
                except:
                    depto_sin_ambientes = depto_sin_ambientes + 1

    print("Existen:")
    print("{} departamentos con dos ambientes".format(depto_2ambientes))
    print("{} departamentos con tres ambientes".format(depto_3ambientes))
    print("Aclaracion: en {} departamentos no se especifica la cantidad de ambientes".format(depto_sin_ambientes))



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    ej3()
    print("")
    ej4()

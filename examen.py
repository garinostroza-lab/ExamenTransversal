#Examen Transversal
#Gary Inostroza Forma E
##  prueba de github


def mostrar_menu():
    print("============ MENU PRINCIPAL ============")
    print("1. Copias por genero")
    print("2. Busqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("========================================")

def leer_opcion():
    try:
        return int(input("Ingrese opcion"))
    except:
        return -1   
    
def copias_genero(catalogo, inventario, genero_buscado):
    suma_disponibles = 0
    for codigo, datos in catologo.items(): 
      genero_libro = datos[2]
    if genero_libro.upper() == genero_buscado.upper():
        suma_disponibles += inventario[codigo][2]
    return suma_disponibles

def buscar_libros_rango(catalogo, multa_min, multa_max):
    lista_encontrados = []
    for codigo, datos in catalogo.items():
        multa = datos[6]
    if multa >= multa_min and multa <= multa_max:
            titulo = datos[0]
            texto = titulo + "--" + codigo
            lista_encontrados.append(texto)
    return lista_encontrados

def actualizar_multa(catalogo) -> None:
    continuar = "s"
    while continuar.lower() == "s":
        codigo = input("Ingrese código del libro: ")
        if codigo in catalogo:
            try:
                nueva_multa = int(input("Ingrese nueva multa: "))
                if nueva_multa >= 0:
                    catalogo[codigo][6] = nueva_multa
                    print("Multa actualizada correctamente.")
                else:
                    print("La multa no puede ser negativa.")
            except:
                print("Error: Debe ingresar un valor numerico.")
    else:   
            print("El código no existe") 
            continuar = input("¿Desea actualizar otra multa (s/n)?: ")

def agregar_libro(catalogo, inventario):
    codigo = input("Ingrese código del libro: ")
    if codigo in catalogo:
        print("Error: Ese código de libro ya existe en el sistema.")
        return
    titulo = input("Ingrese titulo: ")
    autor = input("Ingrese autor: ")
    genero = input("Ingrese genero: ")
    try:
        anio = int(input("Ingrese año de publicación: "))
        editorial = input("Ingrese editorial: ")
        novedad_input = input("¿Es novedad? (s/n): ")
        es_novedad = False
        if novedad_input.lower() == "s":
            es_novedad = True
        multa = int(input("Ingrese precio de multa: "))
        total_copias = int(input("Ingrese cantidad de copias: "))
        
        if multa >= 0 and total_copias > 0:
            catalogo[codigo] = [titulo, autor, genero, anio, editorial, es_novedad, multa]
            inventario[codigo] = [total_copias, 0, total_copias]
            print("Libro agregado exitosamente.")
        else:
            print("Multa o copias invalidas.")
    except:
        print("Error: Ingreso valores numericos inválidos.")
        print("Libro agregado exitosamente.")
    except:
        print("Error: Ingreso valores numericos inválidos.")

def eliminar_libro(catalogo, inventario):
    codigo = input("Ingrese código del libro a eliminar: ")
    if buscar_libro(catalogo, codigo) == True:
        catalogo.pop(codigo)
        inventario.pop(codigo)
        print("Libro eliminado de los registros.")
    else:
        print("El código no existe, no se puede eliminar.")

def main():
    catalogo = {
        "L001": ["Sombras del Sur", "T. Santos", "NOVELA", 2018, "SurEdit", False, 300],
        "L002": ["El Océano", "M. Paz", "CIENCIA", 2020, "Ondas", True, 500],
        "L003": ["Mar y Viento", "T. Santos", "NOVELA", 2019, "SurEdit", False, 350],
        "L004": ["Historia Breve", "A. Ruiz", "HISTORIA", 2021, "Pasado", True, 400],
        "L006": ["Cocina Simple", "L. Chef", "COCINA", 2015, "Sabor", False, 300]
    }
    
    inventario = {
        "L001": [5, 2, 3],
        "L002": [3, 1, 2],
        "L003": [4, 3, 1],
        "L004": [2, 0, 2],
        "L006": [6, 2, 4]
    }

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese opción: "))
            
            if opcion == 1:
                genero = input("Ingrese género a consultar: ")
                resultado = copias_por_genero(catalogo, inventario, genero)
                print("El total de copias disponibles es:", resultado)
                
            elif opcion == 2:
                try:
                    m_min = int(input("Ingrese multa mínima: "))
                    m_max = int(input("Ingrese multa máxima: "))
                    libros_encontrados = buscar_libros_rango(catalogo, m_min, m_max)
                    print("Los libros encontrados son:", libros_encontrados)
                except:
                    print("Debe ingresar valores enteros")
                    
            elif opcion == 3:
                actualizar_multa(catalogo)
                
            elif opcion == 4:
                agregar_libro(catalogo, inventario)
                
            elif opcion == 5:
                eliminar_libro(catalogo, inventario)
                
            elif opcion == 6:
                print("Programa finalizado.")
                break
            else:
                print("Opcion invalida. Intente de nuevo.")
        except:
            print("Error: Ingrese un numero de opcion valido.")


###Gary Inostroza : garinostroza-lab

main()
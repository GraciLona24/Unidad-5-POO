filas = int(input("Número de filas del cine: "))
columnas = int(input("Número de asientos por fila: "))

sala = [["L" for _ in range(columnas)] for _ in range(filas)]



def mostrar_sala():
    print("\n--- Sala de cine ---")
    for fila in sala:
        print(" ".join(fila))
    print()


def reservar_asiento():
    f = int(input("Fila del asiento a reservar: ")) - 1
    c = int(input("Columna del asiento a reservar: ")) - 1

    if f < 0 or f >= filas or c < 0 or c >= columnas:
        print(" Ese asiento no existe.\n")
        return

    if sala[f][c] == "X":
        print(" Ese asiento ya está ocupado.\n")
    else:
        sala[f][c] = "X"
        print(" Asiento reservado con éxito.\n")


def liberar_asiento():
    f = int(input("Fila del asiento a liberar: ")) - 1
    c = int(input("Columna del asiento a liberar: ")) - 1

    if f < 0 or f >= filas or c < 0 or c >= columnas:
        print(" Ese asiento no existe.\n")
        return

    if sala[f][c] == "L":
        print(" Ese asiento ya está libre.\n")
    else:
        sala[f][c] = "L"
        print(" Asiento liberado con éxito.\n")


def estadisticas():
    ocupados = sum(fila.count("X") for fila in sala)
    libres = sum(fila.count("L") for fila in sala)

    print("\n--- Estadísticas ---")
    print(f"Asientos ocupados: {ocupados}")
    print(f"Asientos libres: {libres}\n")


while True:
    print(" Menú principal")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_sala()
    elif opcion == "2":
        reservar_asiento()
    elif opcion == "3":
        liberar_asiento()
    elif opcion == "4":
        estadisticas()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print(" Opción inválida, intenta nuevamente.\n")

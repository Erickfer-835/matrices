def crear_sala(filas, columnas):
    return [["L" for _ in range(columnas)] for _ in range(filas)]


def mostrar_sala(sala):
    print("\nEstado actual de la sala:\n")
    for fila in sala:
        print(" ".join(fila))
    print()


def reservar_asiento(sala, fila, columna):
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("Ese asiento no existe.")
        return

    if sala[fila][columna] == "X":
        print("El asiento ya está ocupado.")
    else:
        sala[fila][columna] = "X"
        print("Asiento reservado correctamente.")


def liberar_asiento(sala, fila, columna):
    if fila < 0 or fila >= len(sala) or columna < 0 or columna >= len(sala[0]):
        print("Ese asiento no existe.")
        return

    if sala[fila][columna] == "L":
        print("El asiento ya está libre.")
    else:
        sala[fila][columna] = "L"
        print("Asiento liberado correctamente.")


def contar_asientos(sala):
    libres = 0
    ocupados = 0
    for fila in sala:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            else:
                ocupados += 1

    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}")


filas = int(input("Número de filas del cine: "))
columnas = int(input("Número de columnas por fila: "))

sala = crear_sala(filas, columnas)

while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar sala")
    print("2. Reservar asiento")
    print("3. Liberar asiento")
    print("4. Contar asientos ocupados y libres")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mostrar_sala(sala)

    elif opcion == "2":
        fila = int(input("Ingrese número de fila: "))
        columna = int(input("Ingrese número de columna: "))
        reservar_asiento(sala, fila, columna)

    elif opcion == "3":
        fila = int(input("Ingrese número de fila: "))
        columna = int(input("Ingrese número de columna: "))
        liberar_asiento(sala, fila, columna)

    elif opcion == "4":
        contar_asientos(sala)

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
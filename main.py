import time
import random
from pathlib import Path
from src.dataloader import verificar_o_generar_archivo
from src.decision_tree import clasificar_lista


DATA_PATH = Path("data/numeros_1000.txt")


def regenerar_numeros(cantidad):

    semilla = random.randint(10000, 99999)
    random.seed(semilla)

    print(f"Regenerando archivo...")
    print(f"Semilla usada: {semilla}")
    print(f"Cantidad: {cantidad}")

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

    numeros = [random.randint(1, 100) for _ in range(cantidad)]

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        for numero in numeros:
            f.write(f"{numero}\n")

    print("Archivo regenerado correctamente.")


def menu_interactivo():
    umbral = 50
    cantidad = 1000

    while True:
        print("\nMENÚ PRINCIPAL")
        print("1. Regenerar números aleatorios")
        print(f"2. Cambiar umbral (Actual: {umbral})")
        print(f"3. Cambiar cantidad de números (Actual: {cantidad})")
        print("4. Iniciar programa")


        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            regenerar_numeros(cantidad)

        elif opcion == "2":
            try:
                nuevo_umbral = int(input("Ingrese nuevo umbral: "))
                umbral = nuevo_umbral
                print(f"Umbral actualizado a {umbral}")
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == "3":
            try:
                nueva_cantidad = int(input("Ingrese nueva cantidad de números a generar: "))
                if nueva_cantidad <= 0:
                    print("Debe ser mayor que cero.")
                else:
                    cantidad = nueva_cantidad
                    print(f"Cantidad actualizada a {cantidad}")
            except ValueError:
                print("Debe ingresar un número entero.")

        elif opcion == "4":
            print(f"\nIniciando programa con:")
            print(f"- UMBRAL = {umbral}")
            print(f"- CANTIDAD = {cantidad}\n")
            return umbral, cantidad

        else:
            print("Opción inválida. Intente de nuevo.")


def main():
    umbral, cantidad = menu_interactivo()

    inicio = time.time()

    if not DATA_PATH.exists():
        regenerar_numeros(cantidad)

    numeros = verificar_o_generar_archivo()

    if len(numeros) != cantidad:
        print("El archivo no tiene la cantidad correcta, regenerando...")
        regenerar_numeros(cantidad)
        numeros = verificar_o_generar_archivo()

    clasificaciones = clasificar_lista(numeros, umbral)

    print("\nEjemplos de clasificación (primeros 10):")
    for n, c in zip(numeros[:10], clasificaciones[:10]):
        print(f"{n} → {c}")

    total_altos = clasificaciones.count("Alto")
    total_bajos = clasificaciones.count("Bajo")

    print("\nConteos:")
    print(f"Altos: {total_altos}")
    print(f"Bajos: {total_bajos}")

    fin = time.time()
    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")


if __name__ == "__main__":
    main()


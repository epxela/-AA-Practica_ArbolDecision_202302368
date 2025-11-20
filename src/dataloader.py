import os
import random
from pathlib import Path

DATA_PATH = Path("data/numeros_1000.txt")


def verificar_o_generar_archivo():
    if not DATA_PATH.exists():

        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)

        semilla = random.randint(10000, 99999)
        random.seed(semilla)

        print(f"[INFO] Archivo no encontrado. Generando nuevo archivo...")
        print(f"[INFO] Semilla usada: {semilla}")

        numeros = [random.randint(1, 100) for _ in range(1000)]

        with open(DATA_PATH, "w", encoding="utf-8") as f:
            for numero in numeros:
                f.write(f"{numero}\n")
    else:
        print("[INFO] Archivo encontrado. Cargando números...")

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        numeros = [int(line.strip()) for line in f.readlines()]

    return numeros

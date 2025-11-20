import time
from pathlib import Path
from src.dataloader import verificar_o_generar_archivo
from src.decision_tree import clasificar_lista

DATA_PATH = Path("data/numeros_1000.txt")

def main():
    umbral = 50 
    inicio = time.time()

    numeros = verificar_o_generar_archivo()

    clasificaciones = clasificar_lista(numeros, umbral)

    print("\nClasificación (primeros 10):")
    for numero, clase in zip(numeros[:10], clasificaciones[:10]):
        print(f"{numero} → {clase}")

    total_altos = clasificaciones.count("Alto")
    total_bajos = clasificaciones.count("Bajo")

    print("\nConteos:")
    print(f"Altos: {total_altos}")
    print(f"Bajos: {total_bajos}")

    fin = time.time()
    print(f"\nTiempo total de ejecución: {fin - inicio:.4f} segundos")

if __name__ == "__main__":
    main()

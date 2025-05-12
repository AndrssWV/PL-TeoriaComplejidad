import matplotlib.pyplot as plt
from sort_methods import SortMethods
from benchmarking import BenchMarking
import random

def build_arreglo(tamano):
    arreglo = []
    for i in range(tamano):
        numeroAletorio = random.randint(0,999)
        arreglo.append(numeroAletorio)
    return arreglo

if __name__ == "__main__":

    methods = SortMethods()
    bench = BenchMarking()
    tamanos = [5000, 10000, 30000, 50000, 100000]
    max_tamano = tamanos[-1]
    arreglo_base = []
    resultados = []

    algoritmos = {
        "bubble" : methods.sort_bubble,
        "bubbleOptimized" : methods.sort_bubble_optimized,
        "selection" : methods.sort_selection,
        "insertion" : methods.sort_insertion,
        "shell" : methods.sort_shell
    }

    for tam in tamanos:

        if len(arreglo_base) < tam:
            arreglo_base += build_arreglo(tam-len(arreglo_base))

        for name, method in algoritmos.items():
            time = bench.medir_tiempo(method, arreglo_base)
            result = (tam, name, time)
            resultados.append(result)

    for tam, method, time in resultados:
            print(f"Tamano: {tam}, Algoritmo: {method}, Tiempo: {time:.6f} segundos")

    datos_grafico = {
        "bubble" : [],
        "bubbleOptimized" : [],
        "selection" : [],
        "insertion" : [],
        "shell" : []
    }

    for tam, method, time in resultados:
        datos_grafico[method].append(time)
    
    plt.figure(figsize=(10,6))
    for name, times in datos_grafico.items():
        plt.plot(tamanos, times, label=name, marker="o")

    plt.title("Comparación de algoritmos de ordenamiento")
    plt.xlabel("Tamaño arreglo")
    plt.ylabel("Tiempo de ejecucion (seg)")
    plt.legend()
    plt.show()

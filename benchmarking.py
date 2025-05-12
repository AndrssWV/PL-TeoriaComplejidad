import time

class BenchMarking:

    def medir_tiempo(self, func, array):
        inicio = time.perf_counter()
        func(array)
        return time.perf_counter() - inicio
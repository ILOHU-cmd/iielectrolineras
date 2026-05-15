import time

try:
    import networkx as nx
    NX_AVAILABLE = True
except ImportError:
    print("La biblioteca 'networkx' no está instalada.")
    NX_AVAILABLE = False


def dijkstra(graph, start, end):
    """Calcula la ruta más corta entre dos nodos."""
    if not NX_AVAILABLE:
        print("Dijkstra no disponible sin 'networkx'.")
        return None, float('inf'), 0

    inicio = time.perf_counter()


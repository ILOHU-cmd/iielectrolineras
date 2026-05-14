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

    try:
        ruta = nx.shortest_path(graph, start, end, weight="length")
        distancia = nx.shortest_path_length(graph, start, end, weight="length")

    except nx.NetworkXNoPath:
        print(f"No hay camino entre {start} y {end}.")
        return None, float('inf'), 0

    except nx.NodeNotFound:
        print(f"El nodo {start} o {end} no existe en el grafo.")
        return None, float('inf'), 0

    fin = time.perf_counter()
    tiempo_ms = (fin - inicio) * 1000

    return ruta, distancia, tiempo_ms


# ─── PRUEBA ───

# 1. Crear un grafo de prueba
grafo_prueba = nx.Graph()

# 2. Agregar nodos (pueden ser números o texto)
grafo_prueba.add_node(1)
grafo_prueba.add_node(2)
grafo_prueba.add_node(3)

# 3. Agregar aristas con peso (distancia)
grafo_prueba.add_edge(1, 2, length=100)   # de 1 a 2 hay 100 metros
grafo_prueba.add_edge(2, 3, length=200)   # de 2 a 3 hay 200 metros
grafo_prueba.add_edge(1, 3, length=500)  # de 1 a 3 hay 500 metros (más largo)

# 4. Probar la función
print("=" * 50)
print("PRUEBA 1: De 1 a 3")
ruta, distancia, tiempo = dijkstra(grafo_prueba, 1, 3)
print(f"Ruta:      {ruta}")
print(f"Distancia: {distancia} metros")
print(f"Tiempo:    {tiempo:.3f} ms")

print()
print("=" * 50)
print("PRUEBA 2: De 1 a 2")
ruta, distancia, tiempo = dijkstra(grafo_prueba, 1, 2)
print(f"Ruta:      {ruta}")
print(f"Distancia: {distancia} metros")
print(f"Tiempo:    {tiempo:.3f} ms")

print()
print("=" * 50)
print("PRUEBA 3: Nodo que no existe (error)")
ruta, distancia, tiempo = dijkstra(grafo_prueba, 1, 99)


def electrolinera_mas_cercana(grafo, nodo_actual, nodos_electrolineras):
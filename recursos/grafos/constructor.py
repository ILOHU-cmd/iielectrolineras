# construccion del grafo vial
# primero se intenta usar el archivo guardado de openstreetmap
# si no se puede, se crea un grafo sencillo con los puntos del proyecto

import math
import os

from datos.data import ELECTROLINERAS, PUNTOS_REFERENCIA


try:
    import osmnx as ox

    OSMNX_DISPONIBLE = True
except ImportError:
    OSMNX_DISPONIBLE = False


try:
    import networkx as nx

    NETWORKX_DISPONIBLE = True
except ImportError:
    NETWORKX_DISPONIBLE = False


NOMBRE_CIUDAD = "Bucaramanga, Santander, Colombia"
CARPETA_RAW = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "datos", "raw")
)
RUTA_CACHE = os.path.join(CARPETA_RAW, "grafo_bga.graphml")


def construir_grafo(desde_cache=True):
    # esta funcion carga el grafo real o construye uno sencillo si falta alguna libreria
    if not os.path.exists(CARPETA_RAW):
        os.makedirs(CARPETA_RAW)

    if OSMNX_DISPONIBLE:
        try:
            if desde_cache and os.path.exists(RUTA_CACHE):
                print("cargando grafo desde el archivo guardado...")
                grafo = ox.load_graphml(RUTA_CACHE)
                print("grafo cargado correctamente desde cache.")
                return etiquetar_nodos_especiales(grafo)
            else:
                print("descargando red vial desde openstreetmap...")
                print("esta parte puede tardar varios minutos.")
                grafo = ox.graph_from_place(NOMBRE_CIUDAD, network_type="drive")
                ox.save_graphml(grafo, RUTA_CACHE)
                print("grafo guardado en: " + RUTA_CACHE)
                return etiquetar_nodos_especiales(grafo)
        except Exception as error:
            print("no se pudo cargar el grafo real.")
            print("detalle:", error)
            print("se usara un grafo sencillo para poder continuar.")
            return construir_grafo_sencillo()
    else:
        print("osmnx no esta instalado. se usara un grafo sencillo.")
        return construir_grafo_sencillo()


def construir_grafo_sencillo():
    # este grafo sencillo permite probar el programa sin internet ni osmnx
    if not NETWORKX_DISPONIBLE:
        print("networkx no esta instalado. no se puede crear el grafo.")
        return None

    grafo = nx.DiGraph()
    lugares = ELECTROLINERAS + PUNTOS_REFERENCIA

    i = 0
    while i < len(lugares):
        lugar = lugares[i]
        grafo.add_node(
            lugar["id"],
            y=lugar["lat"],
            x=lugar["lon"],
            tipo_especial=lugar["tipo"],
            id_especial=lugar["id"],
            nombre_especial=lugar["nombre"],
        )
        i = i + 1

    i = 0
    while i < len(lugares):
        j = 0
        while j < len(lugares):
            if i != j:
                origen = lugares[i]
                destino = lugares[j]
                distancia = distancia_aproximada_metros(
                    origen["lat"],
                    origen["lon"],
                    destino["lat"],
                    destino["lon"],
                )
                grafo.add_edge(origen["id"], destino["id"], length=distancia)
            j = j + 1
        i = i + 1

    print("grafo sencillo creado con", grafo.number_of_nodes(), "nodos y", grafo.number_of_edges(), "aristas.")
    return grafo


def distancia_aproximada_metros(lat1, lon1, lat2, lon2):
    # se usa una formula simple para estimar distancia entre coordenadas
    radio_tierra = 6371000
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    diferencia_lat = math.radians(lat2 - lat1)
    diferencia_lon = math.radians(lon2 - lon1)

    a = (
        math.sin(diferencia_lat / 2) * math.sin(diferencia_lat / 2)
        + math.cos(lat1_rad)
        * math.cos(lat2_rad)
        * math.sin(diferencia_lon / 2)
        * math.sin(diferencia_lon / 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # se multiplica por 1.25 para simular que las vias no son lineas rectas
    return (radio_tierra * c) * 1.25


def etiquetar_nodos_especiales(grafo):
    # esta funcion busca el nodo vial mas cercano para cada electrolinera y punto fijo
    for nodo in grafo.nodes:
        grafo.nodes[nodo]["tipo_especial"] = None
        grafo.nodes[nodo]["id_especial"] = None
        grafo.nodes[nodo]["nombre_especial"] = None

    nodos_usados = []
    lugares = ELECTROLINERAS + PUNTOS_REFERENCIA

    i = 0
    while i < len(lugares):
        lugar = lugares[i]
        nodo_cercano = buscar_nodo_mas_cercano(
            grafo,
            lugar["lat"],
            lugar["lon"],
            nodos_usados,
        )

        if nodo_cercano is not None:
            grafo.nodes[nodo_cercano]["tipo_especial"] = lugar["tipo"]
            grafo.nodes[nodo_cercano]["id_especial"] = lugar["id"]
            grafo.nodes[nodo_cercano]["nombre_especial"] = lugar["nombre"]
            nodos_usados.append(nodo_cercano)

        i = i + 1

    print("electrolineras mapeadas:", contar_tipo(grafo, "electrolinera"))
    print("puntos de referencia mapeados:", contar_tipo(grafo, "referencia"))
    return grafo


def buscar_nodo_mas_cercano(grafo, latitud, longitud, nodos_usados):
    # se recorre el grafo para encontrar el nodo libre mas cercano
    mejor_nodo = None
    mejor_distancia = None

    for nodo, datos in grafo.nodes(data=True):
        if nodo in nodos_usados:
            continue

        lat_nodo = datos.get("y")
        lon_nodo = datos.get("x")

        if lat_nodo is None or lon_nodo is None:
            continue

        lat_nodo = float(lat_nodo)
        lon_nodo = float(lon_nodo)
        distancia = ((latitud - lat_nodo) ** 2) + ((longitud - lon_nodo) ** 2)

        if mejor_nodo is None:
            mejor_nodo = nodo
            mejor_distancia = distancia
        elif distancia < mejor_distancia:
            mejor_nodo = nodo
            mejor_distancia = distancia

    return mejor_nodo


def contar_tipo(grafo, tipo_buscado):
    # se cuenta cuantos nodos especiales quedaron marcados
    contador = 0

    for nodo, datos in grafo.nodes(data=True):
        if datos.get("tipo_especial") == tipo_buscado:
            contador = contador + 1

    return contador


def obtener_nodos_electrolineras(grafo):
    # devuelve un diccionario con id de electrolinera y nodo del grafo
    resultado = {}

    for nodo, datos in grafo.nodes(data=True):
        if datos.get("tipo_especial") == "electrolinera":
            resultado[datos.get("id_especial")] = nodo

    return resultado


def obtener_nodos_referencia(grafo):
    # devuelve un diccionario con id de punto fijo y nodo del grafo
    resultado = {}

    for nodo, datos in grafo.nodes(data=True):
        if datos.get("tipo_especial") == "referencia":
            resultado[datos.get("id_especial")] = nodo

    return resultado


def obtener_nombre_nodo(grafo, nodo):
    # devuelve el nombre de un nodo especial o el id del nodo si no tiene nombre
    if grafo is None:
        return ""

    nombre = grafo.nodes[nodo].get("nombre_especial")

    if nombre is None:
        return str(nodo)
    elif nombre == "":
        return str(nodo)
    else:
        return nombre

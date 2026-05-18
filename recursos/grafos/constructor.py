# construccion y carga del grafo vial de Bucaramanga

import os
import osmnx as ox

from datos.data import ELECTROLINERAS, PUNTOS_REFERENCIA


# =========================================================
# CONFIGURACION GENERAL
# =========================================================

CIUDADES = [
    "Bucaramanga, Santander, Colombia",
    "Floridablanca, Santander, Colombia",
    "Girón, Santander, Colombia",
    "Piedecuesta, Santander, Colombia"
]

carpeta_raw = os.path.join(os.path.dirname(__file__), "..", "..", "datos", "raw")
if not os.path.exists(carpeta_raw):
    os.makedirs(carpeta_raw)
RUTA_CACHE = os.path.join(
    os.path.dirname(__file__), "..", "..", "datos", "raw", "grafo_bga.graphml"
)


def construir_grafo():
    """
    Carga el grafo desde cache si ya existe.
    Si no existe, descarga la red vial de Bucaramanga y área metropolitana.
    """

    if os.path.exists(RUTA_CACHE):

        print("Cargando grafo desde cache...")

        grafo = ox.load_graphml(RUTA_CACHE)

        print("Grafo cargado exitosamente.")

        return marcar_nodos_especiales(grafo)

    else:

        print("Descargando red vial desde OpenStreetMap...")
        print("Ciudades: Bucaramanga, Floridablanca, Girón, Piedecuesta")
        print("Esto puede tardar varios minutos la primera vez.")
        print()

        # Descargar primera ciudad
        print("Descargando Bucaramanga...")
        grafo = ox.graph_from_place(
            CIUDADES[0],
            network_type="drive"
        )
        print("  Nodos:", len(list(grafo.nodes)), "Aristas:", len(list(grafo.edges)))

        # Unir las demás ciudades
        i = 1
        while i < len(CIUDADES):
            ciudad = CIUDADES[i]
            print("Descargando", ciudad, "...")
            
            try:
                grafo_extra = ox.graph_from_place(
                    ciudad,
                    network_type="drive"
                )
                print("  Nodos:", len(list(grafo_extra.nodes)), "Aristas:", len(list(grafo_extra.edges)))
                
                # Unir con el grafo principal
                grafo = nx.compose(grafo, grafo_extra)
                print("  Grafo unido. Total nodos:", len(list(grafo.nodes)))
                
            except Exception as error:
                print("  ERROR:", str(error))
                print("  Continuando sin esta ciudad...")
            
            i = i + 1

        print()
        print("Grafo completo descargado.")
        print("Total nodos:", len(list(grafo.nodes)))
        print("Total aristas:", len(list(grafo.edges)))

        ox.save_graphml(grafo, RUTA_CACHE)

        print("Grafo guardado en disco para usos futuros.")

        return marcar_nodos_especiales(grafo)


# =========================================================
# MARCAR ELECTROLINERAS Y PUNTOS
# =========================================================

def marcar_nodos_especiales(grafo):
    """
    Busca el nodo OSM mas cercano a cada electrolinera y punto
    de referencia y los marca dentro del grafo.
    """

    # inicializar todos los nodos
    for nodo in grafo.nodes:

        grafo.nodes[nodo]["tipo"] = None
        grafo.nodes[nodo]["id_lugar"] = None
        grafo.nodes[nodo]["nombre_lugar"] = None

    # =====================================================
    # MARCAR ELECTROLINERAS
    # =====================================================

    for lugar in ELECTROLINERAS:

        nodo_cercano = ox.distance.nearest_nodes(
            grafo,
            lugar["lon"],
            lugar["lat"]
        )

        grafo.nodes[nodo_cercano]["tipo"] = "electrolinera"
        grafo.nodes[nodo_cercano]["id_lugar"] = lugar["id"]
        grafo.nodes[nodo_cercano]["nombre_lugar"] = lugar["nombre"]

    # =====================================================
    # MARCAR PUNTOS DE REFERENCIA
    # =====================================================

    for lugar in PUNTOS_REFERENCIA:

        nodo_cercano = ox.distance.nearest_nodes(
            grafo,
            lugar["lon"],
            lugar["lat"]
        )

        grafo.nodes[nodo_cercano]["tipo"] = "referencia"
        grafo.nodes[nodo_cercano]["id_lugar"] = lugar["id"]
        grafo.nodes[nodo_cercano]["nombre_lugar"] = lugar["nombre"]

    # =====================================================
    # CONTAR RESULTADOS
    # =====================================================

    total_electro = 0
    total_ref = 0

    for nodo, datos in grafo.nodes(data=True):

        if datos.get("tipo") == "electrolinera":
            total_electro = total_electro + 1

        elif datos.get("tipo") == "referencia":
            total_ref = total_ref + 1

    print("Electrolineras marcadas:", total_electro)
    print("Puntos de referencia marcados:", total_ref)

    return grafo


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================

def obtener_nodos_electrolineras(grafo):
    """
    Devuelve un diccionario:
    id_electrolinera -> nodo_osm
    """

    resultado = {}

    for nodo, datos in grafo.nodes(data=True):

        if datos.get("tipo") == "electrolinera":

            resultado[datos.get("id_lugar")] = nodo

    return resultado


def obtener_nodos_referencia(grafo):
    """
    Devuelve un diccionario:
    id_referencia -> nodo_osm
    """

    resultado = {}

    for nodo, datos in grafo.nodes(data=True):

        if datos.get("tipo") == "referencia":

            resultado[datos.get("id_lugar")] = nodo

    return resultado


def obtener_nombre_nodo(grafo, nodo):
    """
    Devuelve el nombre asociado al nodo.
    """

    if grafo is None:
        return ""

    nombre = grafo.nodes[nodo].get("nombre_lugar")

    if nombre is None:
        return str(nodo)

    elif nombre == "":
        return str(nodo)

    else:
        return nombre

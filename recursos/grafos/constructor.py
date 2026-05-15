import osmnx as ox
import os    
NOMBRE_CIUDAD = "Bucaramanga, Santander, Colombia"
carpeta_raw = os.path.join(os.path.dirname(__file__), "..", "..", "datos", "raw")
if not os.path.exists(carpeta_raw):
    os.makedirs(carpeta_raw)
RUTA_CACHE = os.path.join(
    os.path.dirname(__file__), "..", "..", "datos", "raw", "grafo_bga.graphml"
)
def construir_grafo():
        if os.path.exists(RUTA_CACHE):
            print("Cargando grafo desde cache...")
            grafo = ox.load_graphml(RUTA_CACHE)
            print("Grafo cargado exitosamente.")
            return grafo
        else:
            print("Descargando red vial desde OpenStreetMap...")
            print("Esto puede tardar unos minutos la primera vez.")
            grafo = ox.graph_from_place(NOMBRE_CIUDAD, network_type="drive")
            ox.save_graphml(grafo, RUTA_CACHE)
            print("Grafo guardado en disco para usos futuros.")
            return grafo
            

    
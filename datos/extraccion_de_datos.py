import osmnx as ox
import networkx as nx


# Descargar mapa
G = ox.graph_from_place(
    "Bucaramanga, Santander, Colombia",
    network_type="drive"
)

# Coordenadas
uis = ox.geocode(
    "Universidad Industrial de Santander Bucaramanga"
)

cacique = ox.geocode(
    "Centro Comercial Cacique Bucaramanga"
)

print(uis)

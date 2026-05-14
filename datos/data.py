# import osmnx as ox
# import networkx as nx


# # Descargar mapa
# G = ox.graph_from_place(
#     "Bucaramanga, Santander, Colombia",
#     network_type="drive"
# )

# # Coordenadas
# uis = ox.geocode(
#     "Universidad Industrial de Santander Bucaramanga"
# )

# cacique = ox.geocode(
#     "Centro Comercial Cacique Bucaramanga"
# )

# print(uis)



ELECTROLINERAS = [
    {
        "id": "E1",
        "nombre": "Homecenter Bucaramanga",
        "lat": 7.1218,
        "lon": -73.1198,
        "potencia_kw": 50},
    {
        "id": "E2",
        "nombre": "Centro Comercial Quinta Etapa",
        "lat": 7.1050,
        "lon": -73.1100,
        "potencia_kw": 22},
    {
        "id": "E3",
        "nombre": "Centro Comercial Cacique",
        "lat": 7.1157,
        "lon": -73.1068,
        "potencia_kw": 50},
    {
        "id": "E4",
        "nombre": "Centro Comercial Canaveral",
        "lat": 7.0948,
        "lon": -73.1098,
        "potencia_kw": 22},
    {
        "id": "E5",
        "nombre": "Estacion Terpel Piedecuesta",
        "lat": 6.9900,
        "lon": -73.0500,
        "potencia_kw": 50},
    {
        "id": "E6",
        "nombre": "Exito de La Rosita",
        "lat": 7.0759,
        "lon": -73.1238,
        "potencia_kw": 22},
    {
        "id": "E7",
        "nombre": "Centro Comercial La Florida",
        "lat": 7.1380,
        "lon": -73.1248,
        "potencia_kw": 22},
    {
        "id": "E8",
        "nombre": "Promotores del Oriente (via a Giron)",
        "lat": 7.0720,
        "lon": -73.1650,
        "potencia_kw": 50}
]



PUNTOS_REFERENCIA = [
    {"id": "P1",  "nombre": "UIS Campus Central",               "lat": 7.1398, "lon": -73.1227},
    {"id": "P2",  "nombre": "UIS Campus Florida",               "lat": 7.1372, "lon": -73.1261},
    {"id": "P3",  "nombre": "UIS Parque Tecnologico Guatiguara","lat": 6.9935, "lon": -73.0540},
    {"id": "P4",  "nombre": "UIS Campus Bucarica (Centro)",     "lat": 7.1186, "lon": -73.1228},
    {"id": "P5",  "nombre": "CENFER",                           "lat": 7.1290, "lon": -73.1250},
    {"id": "P6",  "nombre": "UNAB",                             "lat": 7.1189, "lon": -73.1060},
    {"id": "P7",  "nombre": "UTS",                              "lat": 7.1208, "lon": -73.1219},
    {"id": "P8",  "nombre": "UPB",                              "lat": 7.1075, "lon": -73.1119},
    {"id": "P9",  "nombre": "PTAR Rio Frio",                    "lat": 7.1500, "lon": -73.1280},
    {"id": "P10", "nombre": "Sede Recreacional Catay",          "lat": 7.0850, "lon": -73.1050}
]




VEHICULOS = {
    "tesla_modely": {
        "id": "V1",
        "nombre": "Tesla Model Y Long Range",
        "gama": "alta",
        "bateria_kwh": 79.0,
        "autonomia_km": 475.0,
        "consumo_kwh_100km": 16.6
    },
    "byd_dolphin_surf": {
        "id": "V2",
        "nombre": "BYD Dolphin Surf", #se tomo el dolphn por el seagull porque en la pagina no se encontro informacion de este, y su version europea era lo mas cercano
        "gama": "baja",
        "bateria_kwh": 43.2,
        "autonomia_km": 265.0,
        "consumo_kwh_100km": 16.3
    }
}

print (PUNTOS_REFERENCIA)
print (VEHICULOS)
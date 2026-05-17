import osmnx as ox


G = ox.graph_from_place("Bucaramanga, Santander, Colombia",network_type="drive")



lugares_busqueda = [
    {
        "id": "E1",
        "nombre": "Homecenter Bucaramanga",
        "potencia_kw": 50
    },
    {
        "id": "E2",
        "nombre": "Centro Comercial Quinta Etapa",
        "lat": 7.1050,
        "lon": -73.1100,
        "potencia_kw": 22
    },
    {
        "id": "E3",
        "nombre": "Centro Comercial Cacique",
        "potencia_kw": 50
    },
    {
        "id": "E4",
        "nombre": "Centro Comercial Canaveral",
        "lat": 7.0948,
        "lon": -73.1098,
        "potencia_kw": 22
    },
    {
        "id": "E5",
        "nombre": "Estacion Terpel Piedecuesta",
        "lat": 6.9900,
        "lon": -73.0500,
        "potencia_kw": 50
    },
    {
        "id": "E6",
        "nombre": "La rosita exito",
        "potencia_kw": 22
    },
    {
        "id": "E7",
        "nombre": "Centro Comercial La Florida",
        "potencia_kw": 22
    },
    {
        "id": "E8",
        "nombre": "Promotores del Oriente (via a Giron)",
        "potencia_kw": 50
    }
]


ELECTROLINERAS = []

for lugar in lugares_busqueda:
    try:
        if "lat" in lugar and "lon" in lugar:
            lat, lon = lugar["lat"], lugar["lon"]
            metodo = "Manual"
        else:
            coords = ox.geocode(lugar["nombre"] + " Bucaramanga")
            lat, lon = coords[0], coords[1]
            metodo = "Automático"
        
        
        ELECTROLINERAS.append({
            "id": lugar["id"],
            "nombre": lugar["nombre"],
            "lat": lat,
            "lon": lon,
            "potencia_kw": lugar["potencia_kw"],
            "tipo": "electrolinera"
        })

        print(f"{lugar['nombre']} agregado ({metodo})")

    except Exception as e:

        print(f"Error con {lugar['nombre']}: {e}")


referencia = [
    {"id": "P1",  "nombre": "Universidad Industrial de Santander"},
    {"id": "P2",  "nombre": "UIS Sede Floridablanca",               "lat": 7.1372, "lon": -73.1261},
    {"id": "P3",  "nombre": "UIS Parque Tecnologico Guatiguara", "lat": 6.9935, "lon": -73.0540},
    {"id": "P4",  "nombre": "Sede Bucarica UIS ",    "lat": 7.1186, "lon": -73.1228},
    {"id": "P5",  "nombre": "CENFER"},
    {"id": "P6",  "nombre": "UNAB"},
    {"id": "P7",  "nombre": "UTS"},
    {"id": "P8",  "nombre": "Universidad Pontificia Bolivariana Seccional", "lat": 7.1500, "lon": -73.1280},
    {"id": "P9",  "nombre": "PTAR Rio Frio", "lat": 7.1500, "lon": -73.1280},
    {"id": "P10", "nombre": "Hacienda Catay, Piedecuesta, Santander", "lat": 7.0850, "lon": -73.1050}
]

PUNTOS_REFERENCIA = []

for punto in referencia:
    try:
        if "lat" in punto and "lon" in punto:
            lat, lon = punto["lat"], punto["lon"]
            metodo = "Manual"
        else:
            coords = ox.geocode(punto["nombre"] + " Bucaramanga")
            lat, lon = coords[0], coords[1]
            metodo = "Automático"
        
        
        PUNTOS_REFERENCIA.append({
            "id": punto["id"],
            "nombre": punto["nombre"],
            "lat": lat,
            "lon": lon,
            "tipo": "referencia"
        })

        print(f"{punto['nombre']} agregado")

    except Exception as e:

        print(f"Error con {punto['nombre']}: {e}")



VEHICULOS = {
    "tesla_modely": {
        "id": "V1",
        "nombre": "Tesla Model Y Long Range",
        "gama": "alta",
        "bateria_kwh": 79.0,
        "autonomia_km": 475.0,
        "consumo_kwh_100km": 16.6,
    },
    "byd_dolphin_surf": {
        "id": "V2",
        "nombre": "BYD Dolphin Surf",
        "gama": "baja",
        "bateria_kwh": 43.2,
        "autonomia_km": 265.0,
        "consumo_kwh_100km": 16.3,
    },
}


print("\nElectrolineras:")
print(ELECTROLINERAS)

print("\nPuntos de referencia:")
print(PUNTOS_REFERENCIA)

print("\nVehiculos:")
print(VEHICULOS)
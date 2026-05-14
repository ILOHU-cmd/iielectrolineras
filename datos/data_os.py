import osmnx as ox


G = ox.graph_from_place("Bucaramanga, Santander, Colombia", network_type="drive")


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

        "potencia_kw": 22
    },
    {
        "id": "E5",
        "nombre": "Estacion Terpel Piedecuesta",

        "potencia_kw": 50
    },
    {
        "id": "E6",
        "nombre": "Exito de La Rosita",
   
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
            "potencia_kw": lugar["potencia_kw"]
        })
        print(f" {lugar['nombre']} agregado ({metodo})")
        
    except Exception as e:
        print(f" Error con {lugar['nombre']}: {e}")

# Resultado final
print("\nDiccionario final con tus coordenadas preservadas:")
print(ELECTROLINERAS)
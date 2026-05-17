# datos base del proyecto de electrolineras
# aqui se guardan las electrolineras, los puntos fijos y los vehiculos usados


# lista de electrolineras solicitadas en el documento del proyecto
ELECTROLINERAS = [
    {
        "id": "E1",
        "nombre": "Homecenter Bucaramanga",
        "lat": 7.1155902,
        "lon": -73.1211027,
        "potencia_kw": 50,
        "tipo": "electrolinera",
    },
    {
        "id": "E2",
        "nombre": "Centro Comercial Quinta Etapa",
        "lat": 7.1153472,
        "lon": -73.1080126,
        "potencia_kw": 22,
        "tipo": "electrolinera",
    },
    {
        "id": "E3",
        "nombre": "Centro Comercial Cacique",
        "lat": 7.0992729,
        "lon": -73.1072592,
        "potencia_kw": 50,
        "tipo": "electrolinera",
    },
    {
        "id": "E4",
        "nombre": "Centro Comercial Canaveral",
        "lat": 7.0708250,
        "lon": -73.1069520,
        "potencia_kw": 22,
        "tipo": "electrolinera",
    },
    {
        "id": "E5",
        "nombre": "Estacion Terpel Piedecuesta",
        "lat": 6.9981311,
        "lon": -73.0526692,
        "potencia_kw": 50,
        "tipo": "electrolinera",
    },
    {
        "id": "E6",
        "nombre": "Exito de La Rosita",
        "lat": 7.1138712,
        "lon": -73.1229578,
        "potencia_kw": 22,
        "tipo": "electrolinera",
    },
    {
        "id": "E7",
        "nombre": "Centro Comercial La Florida",
        "lat": 7.0705248,
        "lon": -73.1054792,
        "potencia_kw": 22,
        "tipo": "electrolinera",
    },
    {
        "id": "E8",
        "nombre": "Promotores del Oriente (via a Giron)",
        "lat": 7.0856685,
        "lon": -73.1645364,
        "potencia_kw": 50,
        "tipo": "electrolinera",
    },
]


# lista de puntos fijos pedidos para los recorridos
PUNTOS_REFERENCIA = [
    {
        "id": "P1",
        "nombre": "UIS Campus Central",
        "lat": 7.1409311,
        "lon": -73.1198652,
        "tipo": "referencia",
    },
    {
        "id": "P2",
        "nombre": "UIS Campus Florida",
        "lat": 7.0612720,
        "lon": -73.0895969,
        "tipo": "referencia",
    },
    {
        "id": "P3",
        "nombre": "UIS Parque Tecnologico Guatiguara",
        "lat": 6.9946516,
        "lon": -73.0666837,
        "tipo": "referencia",
    },
    {
        "id": "P4",
        "nombre": "UIS Campus Bucarica (Centro)",
        "lat": 7.1193460,
        "lon": -73.1235143,
        "tipo": "referencia",
    },
    {
        "id": "P5",
        "nombre": "CENFER",
        "lat": 7.0822971,
        "lon": -73.1543598,
        "tipo": "referencia",
    },
    {
        "id": "P6",
        "nombre": "UNAB",
        "lat": 7.1168332,
        "lon": -73.1055173,
        "tipo": "referencia",
    },
    {
        "id": "P7",
        "nombre": "UTS",
        "lat": 7.1051164,
        "lon": -73.1235240,
        "tipo": "referencia",
    },
    {
        "id": "P8",
        "nombre": "UPB",
        "lat": 7.0377507,
        "lon": -73.0722590,
        "tipo": "referencia",
    },
    {
        "id": "P9",
        "nombre": "PTAR Rio Frio",
        "lat": 7.0636700,
        "lon": -73.1303400,
        "tipo": "referencia",
    },
    {
        "id": "P10",
        "nombre": "Sede Recreacional Catay",
        "lat": 6.9772129,
        "lon": -73.0411162,
        "tipo": "referencia",
    },
]


# vehiculos actualizados desde la carpeta iielectrolineras
# se usan dos gamas: una alta y una baja
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


def formatear_nombre_vehiculo(nombre, gama):
    # esta funcion agrega la gama al nombre del vehiculo para mostrarlo en pantalla
    nombre_limpio = str(nombre).strip()
    gama_limpia = str(gama).strip().lower()

    if gama_limpia == "":
        return nombre_limpio

    texto_gama = gama_limpia + " gama"

    if texto_gama in nombre_limpio.lower():
        return nombre_limpio
    else:
        return nombre_limpio + " (" + texto_gama + ")"

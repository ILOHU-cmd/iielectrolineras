# visualizacion de mapas y graficos del proyecto
# folium genera el mapa html y matplotlib genera el grafico de barras

import os

from datos.data import ELECTROLINERAS, PUNTOS_REFERENCIA, VEHICULOS
from recursos.utilidades.archivos import ruta_salida


try:
    import folium

    FOLIUM_DISPONIBLE = True
except ImportError:
    FOLIUM_DISPONIBLE = False


try:
    import matplotlib.pyplot as plt

    MATPLOTLIB_DISPONIBLE = True
except ImportError:
    MATPLOTLIB_DISPONIBLE = False


def generar_mapa():
    # crea un mapa con electrolineras y puntos de referencia
    if not FOLIUM_DISPONIBLE:
        print("folium no esta instalado. no se pudo generar el mapa.")
        return ""

    mapa = folium.Map(location=[7.0800, -73.1050], zoom_start=11)
    puntos_mapa = []

    i = 0
    while i < len(ELECTROLINERAS):
        estacion = ELECTROLINERAS[i]
        puntos_mapa.append([estacion["lat"], estacion["lon"]])
        texto = (
            "<b>"
            + estacion["nombre"]
            + "</b><br>id: "
            + estacion["id"]
            + "<br>potencia: "
            + str(estacion["potencia_kw"])
            + " kw"
        )
        folium.Marker(
            location=[estacion["lat"], estacion["lon"]],
            popup=folium.Popup(texto, max_width=250),
            tooltip=estacion["nombre"],
            icon=folium.Icon(color="red", icon="bolt", prefix="fa"),
        ).add_to(mapa)
        i = i + 1

    i = 0
    while i < len(PUNTOS_REFERENCIA):
        punto = PUNTOS_REFERENCIA[i]
        puntos_mapa.append([punto["lat"], punto["lon"]])
        texto = "<b>" + punto["nombre"] + "</b><br>id: " + punto["id"]
        folium.Marker(
            location=[punto["lat"], punto["lon"]],
            popup=folium.Popup(texto, max_width=250),
            tooltip=punto["nombre"],
            icon=folium.Icon(color="blue", icon="university", prefix="fa"),
        ).add_to(mapa)
        i = i + 1

    leyenda = """
    <div style="position: fixed; bottom: 30px; left: 30px; z-index: 1000;
                background: white; padding: 10px; border: 2px solid #cccccc;
                font-size: 13px;">
      <b>leyenda</b><br>
      <span style="display:inline-block; width:10px; height:10px; background:red;
                   border-radius:50%; margin-right:6px;"></span>electrolinera<br>
      <span style="display:inline-block; width:10px; height:10px; background:blue;
                   border-radius:50%; margin-right:6px;"></span>punto de referencia
    </div>
    """
    mapa.get_root().html.add_child(folium.Element(leyenda))

    if len(puntos_mapa) > 0:
        mapa.fit_bounds(puntos_mapa, padding=[30, 30])

    ruta = ruta_salida("mapa_electrolineras.html")
    mapa.save(ruta)
    print("mapa guardado en:", ruta)
    return ruta


def generar_grafico_uso(estadisticas):
    # crea un grafico de barras con el uso de las electrolineras
    if not MATPLOTLIB_DISPONIBLE:
        print("matplotlib no esta instalado. no se pudo generar el grafico.")
        return ""

    if not estadisticas:
        print("no hay estadisticas para graficar.")
        return ""

    uso = estadisticas.get("uso_electrolineras", {})

    if len(uso) == 0:
        print("no hay recargas para graficar.")
        return ""

    nombres = []
    valores = []

    for nombre, cantidad in uso.items():
        if len(nombre) > 18:
            nombres.append(nombre[:18] + "...")
        else:
            nombres.append(nombre)
        valores.append(cantidad)

    posiciones = list(range(len(nombres)))
    plt.figure(figsize=(12, 6))
    barras = plt.bar(posiciones, valores, color="#2f80ed")
    plt.bar_label(barras)
    plt.xticks(posiciones, nombres, rotation=25, ha="right")
    plt.xlabel("electrolinera")
    plt.ylabel("numero de recargas")
    plt.title("uso de electrolineras")
    plt.tight_layout()

    ruta = ruta_salida("uso_electrolineras.png")
    plt.savefig(ruta, dpi=150)
    plt.close()
    print("grafico guardado en:", ruta)
    return ruta


def mostrar_vehiculos_en_mapa():
    # esta funcion devuelve un texto sencillo con los vehiculos usados
    texto = []
    claves = list(VEHICULOS.keys())

    i = 0
    while i < len(claves):
        vehiculo = VEHICULOS[claves[i]]
        texto.append(f"{vehiculo['nombre']} - {vehiculo['gama']}")
        i = i + 1

    return ", ".join(texto)

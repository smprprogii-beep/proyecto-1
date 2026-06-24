informe_dataset = dict[str, dict[str, any]]

def extraer_muestras_por_ciudad(informe: informe_dataset) -> dict[str, int]:
    """
    La función extrae en forma de diccionario los nombres de las ciudades y el número de mediciones.
    Asociado a este.
    """
    respuesta = {}
    for ciudad, data in informe.items():
        respuesta[ciudad] = data["n_muestras"]
    
    return respuesta

def adaptador_temporal(informe: informe_dataset) -> dict[str, dict[str, float]]:
    """
    Extra los datos del infome de manera conveniente para dic_filtrado
    """
    out = {}
    for k, v in informe.items():
        out[k] = {"PM2_5_ug_m3":v["PM2_5_ug_m3"], "PM10_ug_m3":v["PM10_ug_m3"]}
    
    return out


def dic_filtrado(dicc, minimo_pm25, maximo_pm25, minimo_pm10, maximo_pm10 ):
    """
    Dado un diccionario de la forma:
        key: nombre de una ciudad.
        value: diccionario con los promedios de PM2_5_ug_m3 y PM10_ug_m3.
    y dos rangos (uno para PM2_5_ug_m3 y otro para PM10_ug_m3),
    la función devuelve un nuevo diccionario únicamente con las
    ciudades cuyos promedios pertenecen a ambos rangos.
        - dicc tiene la forma:
            {
                ciudad:{
                    PM2_5_ug_m3:float,
                    PM10_ug_m3:float
                }
            }
        - minimo_pm25 <= maximo_pm25
        - minimo_pm10 <= maximo_pm10
    Ejemplo:
        dicc = {
            "Rosario":{PM25:24.0,PM10:41.5},
            "Córdoba":{PM25:38.0,PM10:55.2},
            "Mendoza":{PM25:15.0,PM10:27.8}
        }
        dic_filtrado(dicc,20,30,35,50)
        devuelve:
        {
            "Rosario":{PM25:24.0,PM10:41.5}
        }
    """
    PM25 = "PM2_5_ug_m3"
    PM10 = "PM10_ug_m3"

    dentro_slider = {}#Diccionario donde se almacenarán únicamente las ciudades cuyo promedio esté dentro de ambos rangos.

    for ciudad, mediciones in dicc.items():#Recorre todas las ciudades junto con sus mediciones.
        if minimo_pm25 <= mediciones[PM25] <= maximo_pm25 and minimo_pm10 <= mediciones[PM10] <= maximo_pm10:#Verifica que ambas mediciones pertenezcan a sus respectivos intervalos.
            dentro_slider[ciudad] = mediciones#Agrega la ciudad al diccionario resultado.

    return dentro_slider#Devuelve el diccionario filtrado.

def informe_a_mapa(informe: informe_dataset) -> list[dict]:
    """
    Convierte el informe en una lista de diccionarios compatible con st.map().
    """
    datos = []
    for info in informe.values():
        datos.append({
            "lat": info["latitud"],
            "lon": info["longitud"],
            "color": [255, 0, 0], #color rojo, aunque lo cambie no cambia el color
            "tam": 100#aunque lo cambie no cambia el tamaño
        })
    return datos



def adaptador_dioxido(informe: informe_dataset) -> dict[str, float]:
    """
    Dado un informe completo.
    La función construye un nuevo diccionario formado únicamente por el
    promedio de dióxido de nitrógeno de cada ciudad.
    
    informe: informe_dataset
        Informe generado luego del análisis del dataset.
    Retorna

    dict[str,float]
        key:
            nombre de la ciudad.
        value:
            promedio de dióxido de nitrógeno.

    Ejemplo
        adaptador_dioxido({
        "Rosario":{"Nitrogen_Dioxide_ug_m3":20.5},
        "Córdoba":{"Nitrogen_Dioxide_ug_m3":35.2}
        })

    {
        "Rosario":20.5,
        "Córdoba":35.2
    }
    """

    salida = {}
    for ciudad, datos in informe.items():
        salida[ciudad] = datos["Nitrogen_Dioxide_ug_m3"]
    return salida


def ciudades_superiores_a(diccionario: dict[str,float],minimo: float):
    """
    Dado un diccionario cuyos valores representan el promedio de
    dióxido de nitrógeno por ciudad.
    La función devuelve únicamente aquellas ciudades cuyo promedio
    sea mayor o igual al valor indicado.

    diccionario:
        key:
            nombre de la ciudad.
        value:
            promedio de dióxido de nitrógeno.
    minimo:
        valor mínimo permitido.

    Retorna
    dict[str,float]

    Ejemplo
        ciudades_superiores_a(
        {
        "A":15,
        "B":40,
        "C":12
        },20)
    {
        "B":40
    }
    """
    salida = {}
    for ciudad, promedio in diccionario.items():
        if promedio >= minimo:
            salida[ciudad] = promedio
    return salida


    def adaptador_fecha_y_aqi(estructura, ciudad_ingresada):
        # dada la nueva estructura dicc de la forma 
        # key: <ciudad>
        # value: {"n_ciudades": <int>,
        #         "datos_historicos": [((fecha), aqi, ev), ((fecha), aqi, ev), ...]
        # y dada la ciudad elegida por el usuario la funcion retorna las listas: fechas y valores_aqi que se 
        # necesitan para construir el gráfico correspondiente a la pregunta5 en forma de tupla
        fechas = []
        valores_aqi = []

        for ciudad in estructura:  #creo que puedo hacerlo con while y seria mejor
            if ciudad == ciudad_ingresada:
                datos = estructura[ciudad_ingresada]["datos historicos"]
        for i in datos:
            fecha = i[0]
            fechas = fechas + fecha
            aqi = i[2]
            valores_aqi = valores_aqi + aqi
        return (fechas, valores_aqi)
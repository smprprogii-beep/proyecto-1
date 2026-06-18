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


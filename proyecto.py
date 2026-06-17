import csv
import vistas

informe_dataset = dict[str, dict[str, any]]


def test_obtener_campos():
    registro = ["2026-02-15T13:00","Mexico City",19.4326,-99.1332,25.3,25.0,271.0,4.5,184.0,0.0,9.25,70,0]
    
    assert obtener_campos(registro, ["City", "Latitude", "Longitude"]) == ["Mexico City",19.4326,-99.1332]
    assert obtener_campos(registro, ["City", "Latitude", "Timestamp", "Longitude"]) == ["Mexico City",19.4326, "2026-02-15T13:00", -99.1332]
    assert obtener_campos(registro, ["City"]) == ["Mexico City"]

def obtener_campos(registro: list, campos: list) -> list:
    """
    Dado un registro y una lista, con los nombres de las columnas del dataset.
    La función retorna los campos del registro en el mismo orden en que se ingresaron
    los nombres de las columnas.

    Estos son:
    - Timestamp
    - City
    - Latitude
    - Longitude
    - PM10_ug_m3
    - PM2_5_ug_m3
    - Carbon_Monoxide_ug_m3
    - Nitrogen_Dioxide_ug_m3
    - Ozone_ug_m3,Dust_ug_m3
    - UV_Index,European_AQI
    - Hazardous_Event

    Ejemplos:
    >>> registro = ["2026-02-15T13:00","Mexico City",19.4326,-99.1332,25.3,25.0,271.0,4.5,184.0,0.0,9.25,70,0]
    >>> obtener_campos(registro, ["City", "Latitude", "Longitude"])
    ["Mexico City",19.4326,-99.1332]
    >>> obtener_campos(registro, ["City", "Latitude", "Timestamp", "Longitude"])
    ["Mexico City",19.4326, "2026-02-15T13:00", -99.1332]
    >>> obtener_campos(registro, ["City"])
    ["Mexico City"]
    """
    nombre_de_columna = {
        "Timestamp":0,
        "City":1,
        "Latitude":2,
        "Longitude":3,
        "PM10_ug_m3":4,
        "PM2_5_ug_m3":5,
        "Carbon_Monoxide_ug_m3":6,
        "Nitrogen_Dioxide_ug_m3":7,
        "Ozone_ug_m3":8,
        "Dust_ug_m3":9,
        "UV_Index":10,
        "European_AQI":11,
        "Hazardous_Event":12
    }
    salida = []
    for campo in campos:
        salida.append(registro[nombre_de_columna[campo]])

    return salida

def contar_apariciones(ciudad: str, referencia: informe_dataset) -> None:
    """
    Dado el nombre de una ciudad y la referencia (un informe del dataset).
    La función incrementa en uno el entero asociado a las apariciones de la ciudad indicada.
    Si esta ciudad no aparece en referencia, la misma es agregada y se le asocian las apariciones a 1.
    **MODIFICA LA REFERENCIA EN CADA LLAMADO**
    """
    if ciudad in referencia.keys():
        referencia[ciudad]["n_muestras"] += 1
    else:
        referencia[ciudad] = {"n_muestras": 1}

def analizar_base_de_datos(ruta: str) -> informe_dataset:
    """
    Dada la ruta del archivo CSV, la función realiza un análisis registro a registro del dataset.
    Retorna un diccionario de la forma:
    key (str): Nombre de ciudad.
    value (dict): datos asociados a la ciudad.
    key (str): Identificador del dato.
    value (any): dato.
        - n_muestras
    """
    VALOR_UNICO = 0
    informe = {}

    archivo_csv = open(ruta)
    reader = csv.reader(archivo_csv)
    reader.__next__() # Saltea la primera linea, la de los titulos.
    for registro in reader:
        contar_apariciones(obtener_campos(registro, ["City"])[VALOR_UNICO], informe)
        # pregunta 2

    return informe

def extraer_muestras_por_ciudad(informe: informe_dataset) -> dict[str, int]:
    """
    La función extrae en forma de diccionario los nombres de las ciudades y el número de mediciones.
    Asociado a este.
    """
    respuesta = {}
    for ciudad, data in informe.items():
        respuesta[ciudad] = data["n_muestras"]
    
    return respuesta

def main():

    data = analizar_base_de_datos("global_urban_smog_pm25_hourly_12k.csv")
    vistas.mostrar_vistas({1: extraer_muestras_por_ciudad(data)})

if __name__=="__main__":
    main()

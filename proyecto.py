import csv
import vistas


#toma lista defilas del excel y devuelve la de la posicion 1
def lista_excel(registro):
    return registro[1]
    
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

def contar_apariciones(ciudad: str, referencia: dict[str, int]) -> None:
    """
    Dado el nombre de una ciudad y un diccionario de la forma:
    key: nombre de ciudad.
    value: número de apariciones.
    La función incrementa en uno el entero asociado a una ciudad si la misma coincide.
    Con la proporcionada.
    Si esta ciudad no aparece en referencia, la misma es agregada y se le asocia un 1.
    **MODIFICA LA REFERENCIA EN CADA LLAMADO**
    """
    if ciudad in referencia.keys():
        referencia[ciudad] += 1
    else:
        referencia[ciudad] = 1

def analizar_base_de_datos(ruta: str) -> dict[int, any]:
    """
    Dada la ruta del archivo CSV, la función realiza un análisis registro a registro del dataset.
    Retorna un diccionario de la forma:
    key (int): identificador de pregunta.
    value (any): Datos de respuesta.
    """
    recuento = {}

    archivo_csv = open(ruta)
    reader = csv.reader(archivo_csv)
    reader.__next__() # Saltea la primera linea, la de los titulos.
    for registro in reader:
        contar_apariciones(lista_excel(registro), recuento)
        # pregunta 2

    return {1:recuento}

def main():

    data = analizar_base_de_datos("global_urban_smog_pm25_hourly_12k.csv")
    vistas.mostrar_vistas(data)

if __name__=="__main__":
    main()

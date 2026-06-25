import csv
import vistas
from consultas_al_informe import informe_dataset

fecha = tuple[int, int, int, int]
datos_historico = tuple[fecha, int, int]


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

def agregar_coordenadas(registro: list[str ,str, str], informe: informe_dataset) -> None:
    """
    Dadas las coordenadas de una ciudad, el nombre de la misma y un informe. la función agregara al informe las
    coordenadas en le diccionario de la ciudad.
    Los agregara:
    {
    "latitud": (float), "longitud", (float)
    }
    """
    CIUDAD = 0
    LATITUD = 1
    LONGITUD = 2
    if informe[registro[CIUDAD]]["n_muestras"] == 1:
        informe[registro[CIUDAD]]["latitud"] = float(registro[LATITUD])
        informe[registro[CIUDAD]]["longitud"] = float(registro[LONGITUD])

def representar_en_milecimos(num: str) -> int:
    """
    Convierte un strig de un número con no más de 3 decimales a un numro entero
    que representa el número de milecimos para formar dicho numero.
    **COON DECIMALES SEPARADOS POR .**
    ejemplo:
    
    >>> representar_en_milecimos("5")
    5
    >>> representar_en_milecimos("5.5")
    55
    >>> representar_en_milecimos("5.55")
    555
    >>> representar_en_milecimos("5.555")
    5555
    """
    return int(num.replace(".", ""))


def incrementar_datos_de_promedio(registro: list[str, str, str, str, str], informe: informe_dataset) -> None:
    """
    Dado el nombre de una ciudad y los datos "PM10_ug_m3", "PM2_5_ug_m3","Carbon_Monoxide_ug_m3", "Nitrogen_Dioxide_ug_m3"
    la función ingrementa en la magnitud indicada los datos del mismo nombre.
    """

    CIUDAD = 0
    PM10 = 1
    PM25 = 2
    CM = 3
    ND = 4

    try:
        informe[registro[CIUDAD]]["PM10_ug_m3"] += float(registro[PM10])
        informe[registro[CIUDAD]]["PM2_5_ug_m3"] += float(registro[PM25])
        informe[registro[CIUDAD]]["Carbon_Monoxide_ug_m3"] += float(registro[CM])
        informe[registro[CIUDAD]]["Nitrogen_Dioxide_ug_m3"] += float(registro[ND])
    except KeyError:
        informe[registro[CIUDAD]]["PM10_ug_m3"] = float(registro[PM10])
        informe[registro[CIUDAD]]["PM2_5_ug_m3"] = float(registro[PM25])
        informe[registro[CIUDAD]]["Carbon_Monoxide_ug_m3"] = float(registro[CM])
        informe[registro[CIUDAD]]["Nitrogen_Dioxide_ug_m3"] = float(registro[ND])

def formular_promedios(info: informe_dataset) -> None:
    """
    realiza la divión respectiva a los valores promediados.
    """
    for data_ciudad in info.values():
        # se usa divición parte entera para mantener el criterio de número de milecimos.
        data_ciudad["PM10_ug_m3"] /= data_ciudad["n_muestras"]
        data_ciudad["PM2_5_ug_m3"] /= data_ciudad["n_muestras"]
        data_ciudad["Carbon_Monoxide_ug_m3"] /= data_ciudad["n_muestras"]
        data_ciudad["Nitrogen_Dioxide_ug_m3"] /= data_ciudad["n_muestras"]

def informe_a_mapa(informe):
    datos = []
    for info in informe.values():
        datos.append({
            "lat": info["latitud"],
            "lon": info["longitud"],
            "color": [255, 0, 0],
            "tam": 100
        })
    return datos

def obtener_fecha(fecha: str) -> fecha:
    """
    Dada una string con una fecha en el formato AAAA-DD-MMTHH:MM, con estos siendo números.
    Retorna una tupla con el número del año, mes, día y el número de minutos que transcurrieron en el día.
    Ejemplo:
    >>> obtener_fecha("2025-09-30T23:00")
    (2025, 9, 30, 1380)
    >>> obtener_fecha("2026-03-24T07:00")
    (2026, 3, 7, 420)
    """
    mes = int(fecha[5:7])
    dia = int(fecha[8:10])
    minutos = int(fecha[11:13])*60 + int(fecha[14:])
    return int(fecha[0:4]), mes, dia, minutos

def carga_ordenada(fecha: fecha, aqi: int, eventos: int, historial: list[datos_historico], n_elementos_historial: int) -> list[datos_historico]:
    """
    La función carga_ordenada espera la fecha, valor aqi, valor, eventos, el historial y
    el numero de registros hasta el momento.
    La función agrega al historial los datos historicos manteniendo el orden por por fecha.

    Ejemplo:
    >>> historial = []
    >>> carga_ordenada((2025, 9, 30, 1380), 5, 0, historial)
    [((2025, 9, 30, 1380), 5, 0)]
    >>> carga_ordenada((2026, 3, 7, 420), 2, 1, historial)
    [((2025, 9, 30, 1380), 5, 0), ((2026, 3, 7, 420), 2, 1)]
    >>> carga_ordenada((2025 ,10 ,1 ,1 ), 1, 1, historial)
    [((2025, 9, 30, 1380), 5, 0), ((2025 ,10 ,1 ,1 ), 1, 1), ((2026, 3, 7, 420), 2, 1)]
    """
    no_ubicado = True
    i = 0
    if historial == []: historial.append((fecha, aqi, eventos))
    else:
        while i < n_elementos_historial and historial[i][0] <= fecha:
            i += 1
        historial.insert(i, (fecha, aqi, eventos))
    
    return historial

    


def cargar_datos_temporales(registro: list[str, str, str, str], informe: informe_dataset) -> None:
    """
    Dado un registros con Nombre de la ciudad, Timestamp, European_AQI y Hazardous_Event, junto con el informe
    la funcíon completa el campo "Datos_cronologicos" de la ciudad indicada. Con una lista ordenada por fecha 
    formada por tuplas (ternas) formadas por Timestamp, European_AQI y Hazardous_Event
    
    Ejemplo:
    >>> informe = {"Mexico City": ... }
    >>> cargar_datos_temporales(["Mexico City", "2025-09-30T23:00", "5", "0"], informe)
    >>> informe
    {
    "Mexico City": 
        ... 
        datos_temporales: [((2025, 9, 30, 1380), 5, 0)],
        ...
    }
    >>> cargar_datos_temporales(["Mexico City", "2026-03-24T07:00", "2", "1"], informe)
    {
    "Mexico City": 
        ... 
        datos_temporales: [((2025, 9, 30, 1380), 5, 0), ((2026, 3, 24, 420), 2, 1)],
        ...
    }
    """
    NOMBRE = 0
    FECHA = 1
    R_AQI = 2
    EV = 3
    fecha_registro = obtener_fecha(registro[FECHA])
    aqi = int(registro[R_AQI])
    ev = int(registro[EV])
    ciudad = registro[NOMBRE]

    if not("datos_temporales" in informe[ciudad]):
        # Agregamos el parametro si este no se encuentra en la estructura.
        informe[ciudad]["datos_temporales"] = []
    # Agregamos en cada ocación los datos
    carga_ordenada(fecha_registro, aqi, ev, informe[ciudad]["datos_temporales"], informe[ciudad]["n_muestras"]-1)




def analizar_base_de_datos(ruta: str) -> informe_dataset:
    """
    Dada la ruta del archivo CSV, la función realiza un análisis registro a registro del dataset.
    Retorna un diccionario de la forma:
    key (str): Nombre de ciudad.
    value (dict): datos asociados a la ciudad.
    key (str): Identificador del dato.
    value (any): dato.
        - n_muestras
        - latitud
        - longitud
        - PM10_ug_m3
        - PM2_5_ug_m3
        - Carbon_Monoxide_ug_m3
        - Nitrogen_Dioxide_ug_m3
    """
    VALOR_UNICO = 0
    informe = {}

    archivo_csv = open(ruta)
    reader = csv.reader(archivo_csv)
    reader.__next__() # Saltea la primera linea, la de los titulos.
    for registro in reader:
        contar_apariciones(obtener_campos(registro, ["City"])[VALOR_UNICO], informe)
        agregar_coordenadas(obtener_campos(registro, ["City", "Latitude", "Longitude"]), informe)
        incrementar_datos_de_promedio(obtener_campos(registro, ["City", "PM10_ug_m3", "PM2_5_ug_m3","Carbon_Monoxide_ug_m3", "Nitrogen_Dioxide_ug_m3"]), informe)
        cargar_datos_temporales(obtener_campos(registro, ["City", "Timestamp", "European_AQI", "Hazardous_Event"]),informe)
    formular_promedios(informe)
    return informe


def main():
    data = analizar_base_de_datos("global_urban_smog_pm25_hourly_12k.csv")
    vistas.mostrar_vistas(data)

if __name__=="__main__":
    main()

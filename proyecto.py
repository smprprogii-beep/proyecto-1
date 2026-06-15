import csv
import vistas


#toma lista defilas del excel y devuelve la de la posicion 1
def lista_excel(registro):
    return registro[1]
    

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

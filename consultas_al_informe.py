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
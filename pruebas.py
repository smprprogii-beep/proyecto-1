import streamlit as st
import matplotlib.pyplot as plt

PM25 = "PM2_5_ug_m3"#para no escribir tanto
PM10 = "PM10_ug_m3"


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
    dentro_slider = {}#Diccionario donde se almacenarán únicamente las ciudades cuyo promedio esté dentro de ambos rangos.

    for ciudad, mediciones in dicc.items():#Recorre todas las ciudades junto con sus mediciones.
        if minimo_pm25 <= mediciones[PM25] <= maximo_pm25 and minimo_pm10 <= mediciones[PM10] <= maximo_pm10:#Verifica que ambas mediciones pertenezcan a sus respectivos intervalos.
            dentro_slider[ciudad] = mediciones#Agrega la ciudad al diccionario resultado.

    return dentro_slider#Devuelve el diccionario filtrado.


#Diccionario de ejemplo utilizado para probar el funcionamiento.
the_dic = {
    "Rosario":{PM25:24.0,PM10:41.5},
    "Córdoba":{PM25:38.0,PM10:55.2},
    "Mendoza":{PM25:15.0,PM10:27.8},
    "Buenos Aires":{PM25:52.4,PM10:73.1},
    "Santa Fe":{PM25:31.8,PM10:46.2},
    "La Plata":{PM25:40.6,PM10:58.3},
    "Salta":{PM25:72.1,PM10:94.0},
    "Neuquén":{PM25:18.4,PM10:33.6},
}


def pregunta2(el_diccionario):
    st.title("Ciudades por rango de PM2.5 y PM10")#Agrega el título principal de la aplicación.
    minimo_pm25,maximo_pm25 = st.slider(   #(nota  a hacer , habria que modulaizar los slider)
        "Seleccione el rango de PM2.5",#Texto mostrado sobre el slider.
        min_value=0.0,#Valor mínimo permitido.
        max_value=300.0,#Valor máximo permitido.
        value=(0.0,300.0),#Rango seleccionado al iniciar la aplicación.
        step=0.5#Incremento del slider.
    )
    minimo_pm10,maximo_pm10 = st.slider(  #(nota  a hacer , habria que modulaizar los slider)
        "Seleccione el rango de PM10",#Texto mostrado sobre el slider.
        min_value=0.0,#Valor mínimo permitido.
        max_value=300.0,#Valor máximo permitido.
        value=(0.0,300.0),#Rango seleccionado al iniciar la aplicación.
        step=0.5#Incremento del slider.
    )
    filtrado = dic_filtrado(el_diccionario,minimo_pm25,maximo_pm25,minimo_pm10,maximo_pm10)#Obtiene únicamente las ciudades comprendidas dentro de ambos rangos.

    fig,ax = plt.subplots(figsize=(9,5))#Crea una figura de Matplotlib.
    ax.axis("off")#Oculta los ejes porque solamente se mostrará una tabla.

    datos = [[ciudad,mediciones[PM25],mediciones[PM10]] for ciudad,mediciones in filtrado.items()]#Convierte el diccionario filtrado en una lista de filas.

    if len(datos) == 0:#Verifica si existen ciudades dentro del rango.
        ax.text(
            0.5,
            0.5,
            "No hay ciudades en ese rango",
            ha="center",
            va="center",
            fontsize=15
        )#Muestra un mensaje en el centro de la figura.
    else:
        tabla = ax.table(
            cellText=datos,#Filas de la tabla.
            colLabels=["Ciudad","Promedio PM2.5","Promedio PM10"],#Encabezados.
            loc="center"#Ubicación dentro de la figura.
        )

        tabla.auto_set_font_size(False)#Desactiva el tamaño automático de la fuente.
        tabla.set_fontsize(12)#Establece el tamaño de la fuente.
        tabla.scale(1.2,1.8)#Aumenta el tamaño de las celdas para mejorar la lectura.

    st.pyplot(fig)#Muestra la figura dentro de la aplicación Streamlit.
pregunta2(the_dic)
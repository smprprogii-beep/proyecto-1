import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from consultas_al_informe import *

def vista_pregunta_1(tab, data: dict) -> None:
    """
    Dado un objeto TabContainer y un diccionario con los nombres de las ciudades y un número entero.
    Genera el tab correspondiente a la pregunta: ¿En qué ciudades se hicieron más mediciones?
    """
    with tab:
        st.header("Gráfica de mediciones")

        names = list(data.keys())
        values = list(data.values())
        fig, ax = plt.subplots(figsize=(20, 16))
        ax.bar(names, values)
        ax.tick_params(axis = "x",labelcolor='black', rotation= 270, labelsize=20 )     # rota los nombres hacia abajo y agranda la letra de los valores en x
        ax.tick_params(axis = "y", labelsize=20 , labelcolor='black'  ) #cambia el tamaño de los valores en y #agrege labelcolor='black', solo para tener en cuenta el cambio de color
        maximo = max(values) # da el valor maximo de values
        y_lista = list(range(0, maximo + 40, 40))# genera una lista de valores desde 0 hasta el maximo mas 30
        y_lista.append(maximo)# a la lista y_lista le agrega el valor del maximo
        ax.set_yticks(y_lista)#los valores que se muestran en y 
        plt.tight_layout()      # evita que se corten
        st.pyplot(fig)

#def vista_pregunta_2(tab, data):
#    with tab:
#        st.header("Representación")
#        st.image("https://static.streamlit.io/examples/dog.jpg", width=1080)
def mostrar_tabla(datos: list[list], columnas: list[str]) -> None:
    """
    Dada una lista de filas y una lista con los nombres de las columnas.
    La función genera una figura de Matplotlib con una tabla.
    En caso de que no existan datos para mostrar, presenta un mensaje
    indicando que no hubo resultados.
    datos:
        Lista de filas que se mostrarán en la tabla.
    columnas:
        Lista con los nombres de las columnas.
    Retorna
        Figura que contiene la tabla generada.
    """
    fig, ax = plt.subplots(figsize=(9, 5)) #Crea una figura de Matplotlib.
    ax.axis("off") #Oculta los ejes porque solamente se mostrará una tabla.
    if len(datos) == 0: #Verifica si existen datos para mostrar.
        ax.text(
            0.5,
            0.5,
            "No hay datos para mostrar.",
            ha="center",
            va="center",
            fontsize=15
        ) #Muestra un mensaje en el centro de la figura.
    else:
        tabla = ax.table(
            cellText=datos, #Filas de la tabla.
            colLabels=columnas, #Encabezados de la tabla.
            loc="center" #Ubicación dentro de la figura.
        )
        tabla.auto_set_font_size(False) #Desactiva el tamaño automático de la fuente.
        tabla.set_fontsize(12) #Establece el tamaño de la fuente.
        tabla.scale(1.2, 1.8) #Aumenta el tamaño de las celdas para mejorar la lectura.
    return fig #Devuelve la figura generada.

def pregunta2(tab, el_diccionario):
    PM25 = "PM2_5_ug_m3"
    PM10 = "PM10_ug_m3"
    with tab:
        st.header("Ciudades por rango de PM2.5 y PM10")#Agrega el título principal de la aplicación.
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
        datos = [[ciudad, mediciones[PM25], mediciones[PM10]]
         for ciudad, mediciones in filtrado.items()] #Convierte el diccionario filtrado en una lista de filas.
        fig = mostrar_tabla(
            datos,
            ["Ciudad", "Promedio PM2.5", "Promedio PM10"]
        ) #Genera una figura con la tabla correspondiente.
        st.pyplot(fig) #Muestra la figura dentro de la aplicación Streamlit.



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


def vista_mapa(tab, datos_mapa):
    """
    Dado un objeto TabContaines y datos_mapa una lista de diccionarios con las coordenadas de 
    las ciudades y el color y el tamaño de los circulos.
    Genera el tab correspondiente a la pregunta: ¿Cuales son las ciudades con mayor 
    promedio de dioxido de carbono?
    mostrando con circulos más grandes las ciudades con mayor promedio y con 
    circulos mas chicos las ciudades con menor promedio.
    """
    with tab:
        st.header("Mapa de cantidades")
        st.map(
            data=datos_mapa,
            latitude="lat",
            longitude="lon",
            color="color",
            size="tam",
            zoom=4,
            width="stretch",
            height=500
        )

def pregunta4(tab, datos):
    """
    Dado un TabContainer y un diccionario con los promedios de dióxido de nitrógeno
    por ciudad.
    La función genera una tabla con las ciudades cuyo promedio de dióxido de
    nitrógeno es mayor o igual al valor seleccionado mediante un slider.
    tab:
        Pestaña donde se mostrará la vista.
    datos:
        Diccionario cuya clave es el nombre de la ciudad y cuyo valor es el
        promedio de dióxido de nitrógeno.
    """
    with tab:
        st.header("Ciudades con promedio de dióxido de nitrógeno superior a X") #Agrega el título principal de la aplicación.
        valor = st.slider(
            "Seleccione el promedio mínimo", #Texto mostrado sobre el slider.
            min_value=0.0, #Valor mínimo permitido.
            max_value=100.0, #Valor máximo permitido.
            value=0.0, #Valor inicial del slider.
            step=0.5 #Incremento del slider.
        )
        filtrado = ciudades_superiores_a(datos, valor) #Obtiene únicamente las ciudades cuyo promedio supera el valor seleccionado.
        datos_tabla = [] #Lista donde se almacenarán las filas de la tabla.
        for ciudad, promedio in filtrado.items(): #Recorre todas las ciudades filtradas.
            datos_tabla.append([ciudad, promedio]) #Agrega una fila con la ciudad y su promedio.
        fig = mostrar_tabla(
            datos_tabla,
            ["Ciudad", "Promedio NO₂"]
        ) #Genera la figura con la tabla.
        st.pyplot(fig) #Muestra la figura dentro de la aplicación Streamlit.

def pregunta5(tab, data:tuple):
    """
    Dado un TabContainer y una tupla con las listas que necesitamos para graficar,
    la función genera un grafico con las mediciones realizadas en una ciudad seleccionada y sus respectivos
    valores de AQI a lo largo del tiempo
    """
    with tab:
        st.header("Cambios que presenta la cuidad X a lo largo del tiempo en los valores de European AQI") #Agrega el título principal de la aplicación.
        option = st.selectbox(
                ("Bangkok", "Beijing", "Bogota", "Buenos Aires", "Cairo", "Chicago", "Delhi", "Dhaka", 
                "Dubai", "Istanbul", "Jakarta", "Johannesburg", "Karachi", "Lagos", "Lahore", "Lima", 
                "London", "Los Angeles", "Mexico City", "Moscow", "Mumbai", "Nex York", "Paris", "Riyadh", 
                "Sao Paulo", "Seoul", "Shanghai", "Tehran", "Tokyo"),
                index=None,
                placeholder="Seleccione la ciudad deseada",
        )                                                                                                  #Ingreso de ciudad por medio del menu desplegable
        st.write("Ciudad seleccionada:", option)
        #st.pyplot(fig) #Muestra la figura dentro de la aplicación Streamlit.

        fechas = data[0] #datos para el eje x
        valores_aqi = data[1] #datos para el eje y

        fig, ax = plt.subplots(figsize=(12, 4)) #crea el lienzo

        ax.stem(fechas, valores_aqi) #para dibujar el gráfico ax.stem recibe primero las X (fechas) y después las Y (AQI)

        #ax.set_title("¿Qué cambios en los valores de European AQI presenta la ciudad X?", fontsize=12)
        ax.set_xlabel("Fecha (con horario)")
        ax.set_ylabel("Valores de European AQI")

        # Ajustamos los límites de Y para que empiece en 0 y llegue al max valor de la escala
        #ax.set_ylim(0, max) 

        plt.xticks(rotation=30) #rotam las etiquetas del eje X para que no se pisen entre si

        plt.tight_layout() #hace que el gráfico no se corte en los bordes

        plt.show() #muestra el grafico




def mostrar_vistas(datos: informe_dataset) -> None:
    """
    La función define todos los tabs que se mostrarán en la vista web.
    La misma requiere un diccionario formado por:
    key (int): Número de pregunta.
    value (any): Los datos que deben mostrarse (según el contrato de cada vista).
    """
    tab1, tab2, tab3, tab4 = st.tabs([
                                        "¿En qué ciudades se hicieron más mediciones?",
                                        "¿Qué ciudades tienen un rango de X de partículas de tamaño particular?",
                                        "¿Cuales son las ciudades con mayor promedio de dioxido de carbono?",
                                        "¿Qué ciudades tienen un promedio de dióxido de nitrógeno superior a X?"])
    vista_pregunta_1(tab1, extraer_muestras_por_ciudad(datos))
    pregunta2(tab2, adaptador_temporal(datos))
    datos_mapa = informe_a_mapa(datos)
    vista_mapa(tab3, datos_mapa)
    pregunta4(tab4, adaptador_dioxido(datos))

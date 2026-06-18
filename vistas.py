import streamlit as st
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
    st.map(data=datos_mapa,
    latitude="lat",
    longitude="lon",
    color="color",
    size="tam",
    zoom=4,
    width="stretch",
    height=500)

def mostrar_vistas(datos: informe_dataset) -> None:
    """
    La función define todos los tabs que se mostrarán en la vista web.
    La misma requiere un diccionario formado por:
    key (int): Número de pregunta.
    value (any): Los datos que deben mostrarse (según el contrato de cada vista).
    """
    tab1, tab2, tab3 = st.tabs(["¿En qué ciudades se hicieron más mediciones?", "MAPA", "¿Cuales son las ciudades con mayor promedio de dioxido de carbono?"])
    vista_pregunta_1(tab1, extraer_muestras_por_ciudad(datos))
    pregunta2(tab2, adaptador_temporal(datos))
    vista_mapa(tab3, datos_mapa)

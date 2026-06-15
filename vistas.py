import streamlit as st
import matplotlib.pyplot as plt

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

def mostrar_vistas(respuestas: dict) -> None:
    """
    La función define todos los tabs que se mostrarán en la vista web.
    La misma requiere un diccionario formado por:
    key (int): Número de pregunta.
    value (any): Los datos que deben mostrarse (según el contrato de cada vista).
    """
    tab1, tab2, tab3 = st.tabs(["¿En qué ciudades se hicieron más mediciones?", "Pregunta siguiente", "Pregunta siguiente"])
    vista_pregunta_1(tab1, respuestas[1])
    #vista_pregunta_2(tab2, None)
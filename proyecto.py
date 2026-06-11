import csv
import streamlit as st
import matplotlib.pyplot as plt


#toma lista defilas del excel y devuelve la de la posicion 1
def lista_excel(registro):
    return registro[1]
    



#toma lista de ciudade y las devuelve en libreria id=ciudad dato= cantidad de apariciones
def mas_apariciones(listass):
    dato_ciudades = {}

    for ciudad in listass:     #ciudad toma el valor de cada elemento de listass
        if ciudad in dato_ciudades:   #aca pregunta si ciudad ya esta en dato_ciudades
            dato_ciudades[ciudad] += 1 #en caso que este agrega uno al dato asignado a "ciudad"
        else:
            dato_ciudades[ciudad] = 1  #en caso de no estar crea la clave con el calor de ciudad y le asigna 1(por que aparecio por primera vez)

    return(dato_ciudades)

#mas_apariciones(lista_excel(VALOR QUE DADO DEL EXCEL))




def main():

    archivo_csv = open("global_urban_smog_pm25_hourly_12k.csv")
    reader = csv.reader(archivo_csv)
    reader.__next__() # Saltea la primera linea, la de los titulos.
    ciudades = [] # variable para inicializar lista
    for registro in reader:
        ciudades.append(lista_excel(registro)) #crea la lista de solo las ciudades
        #pregunta2
        #pregunta3
        #pregunta4
        #pregunta5
        #pregunta6
    var1 = mas_apariciones(ciudades)  # var1 usa la funcion mas_apariciones con la lista ciudades y 
                                      #devuelve libreria con ciudad:apariciones
    tab1, tab2, tab3 = st.tabs(["¿En qué ciudades se hicieron más mediciones?", "Pregunta siguiente", "Pregunta siguiente"])
    with tab1:
        st.header("Gráfica de mediciones")

        data = var1
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
    with tab2:
        st.header("Representación")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=1080)
    with tab3:
        st.header("Representacion")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=1080)

if __name__=="__main__":
    main()

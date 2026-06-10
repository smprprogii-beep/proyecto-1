import csv
import streamlit as st
import matplotlib.pyplot as plt
#agarra la lista de la linea de datos del excel y crea la lista de solo las ciudades

"""
listaa= type(lista)
funcion lista_excel que toma una lista de datos y agrega a listaa el segundo valor de la lista dada, devuelve el resultado de la lista
lista-excel(lista_datos==lista)-> lista
ejemplos:
    lista_excel(['2025-12-25T16:00','Los Angeles','34.0522','-118.2437' ]) -> ['Los Angeles']
    lista_excel(['2025-11-10T10:30','Rosario','-32.9442','-60.6505'])-> ['Los Angeles', 'Rosario']
    lista_excel(['2025-01-01T08:00','Cordoba']), -> ['Los Angeles', 'Rosario', 'Cordoba']
    

"""

def lista_excel(lista_datos, listaa=[]):
    listaa.append(lista_datos[1])
    return listaa


"""dato_ciudades = type(diccionario)

funcion mas_apariciones que toma una lista 
de ciudades y guarda en dato_ciudades
cada ciudad como clave y la cantidad de apariciones como valor, devuelve el diccionario resultante

mas_apariciones(listass==lista) -> diccionario

ejemplos:
    mas_apariciones(['Rosario','Cordoba','Rosario']) -> {'Rosario': 2, 'Cordoba': 1}

    mas_apariciones(['Buenos Aires','Rosario','Cordoba','Rosario']) 
    -> {'Buenos Aires': 1, 'Rosario': 2, 'Cordoba': 1}

    mas_apariciones(['Mendoza','Mendoza','Mendoza']) 
    -> {'Mendoza': 3}


chequeos:
    type(listass) == list
    len(listass) > 0
    type(ciudad) == str"""

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
    for registro in reader:
        var1 = mas_apariciones(lista_excel(registro))  
    print(var1)

    

    tab1, tab2, tab3 = st.tabs(["¿En qué ciudades se hicieron más mediciones?", "Pregunta siguiente", "Pregunta siguiente"])

    with tab1:
        st.header("Gráfica de mediciones")
    
        data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
        names = list(data.keys())
        values = list(data.values())

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(names, values)
        st.pyplot(fig)
    with tab2:
        st.header("Representación")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
    with tab3:
        st.header("Representacion")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

if __name__=="__main__":
    main()

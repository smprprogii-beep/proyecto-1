import csv
import vistas


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
    vistas.mostrar_vistas({1:var1})
if __name__=="__main__":
    main()

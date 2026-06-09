import csv

def main():

    archivo_csv = open("global_urban_smog_pm25_hourly_12k.csv")
    reader = csv.reader(archivo_csv)
    reader.__next__() # Saltea la primera linea, la de los titulos.

    for registro in reader:
        # Funciones a realizar en cada registro.
        print(registro)
        


if __name__=="__main__":
    main()

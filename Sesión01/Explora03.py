import pandas as pd

#cargar datos de un archivo csv

data = pd.read_csv("ventas_televisores.csv")

#Muestra las primeras 5 filas
print("Los primeros registros son:\n", data.head())

print('La informacion general es:\n')
data.info() #Muestra la informacion general

#Muestra estadisticas basicas del archivo
print('Las estadisticas básicas del archivo son: ', data.describe())
#Creacion de otra serie

import pandas as pd

#creamos la serie
datos=[10, 20, 30, 40, 50]
indices=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

#indicamos la serie (La serie siempre debe estar acompañada con su index)
#Sino solo estaria manejadon una lista, para manejar la potencialidad de la serie es la lista con sus datos y sus indices
serie=pd.Series(datos, index=indices)
print(f'La serie de datos es: \n{serie}')

#Convertiremos esta serie en un dataframe
#Es decir, un formato especial tabular

input('Presiona enter para continuar...')

df=serie.to_frame(name='Ventas') #Le damos mas poder a las series
print(f"El dataframe es:\n{df}")

#Añadiremos una nueva columna llamada 'Porcentaje'
#Porcentaje calcula la proporcion de cada valor respecto al total
df['Porcentaje %']=round(((df['Ventas']/df['Ventas'].sum())*100), 2)
print(f"Dataframe con porcentajes:\n{df}")
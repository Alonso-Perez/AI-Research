#Registraremos los datos de tiempo dedicado al ejercicio
import pandas as pd


ejercicios=[50, 60, 45, 30, 40]
dias=['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
#creamos la serie

series=pd.Series(ejercicios, index=dias)

#convertimos a dataframe
df=series.to_frame(name='Ejercicio (min)')

print('El dataframe es:\n', df)
#calculamos el porcentaje
df['Porcentaje %']=(df[])
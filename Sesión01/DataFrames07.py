import pandas as pd

ventas_df=pd.DataFrame({
    'Lunes':[250, 300, 200],
    'Martes':[300,350,180],
    'Miercoles':[400,420,250],
    'Jueves':[150,200,100],
    'Viernes':[100,550,300]
}, index=['Empleado 1', 'Empleado 2', 'Empleado 3'])

#mostramps el dataframe
print(ventas_df)

#Obtendremos las ventas totales
print('\nVentas totales por dia:\n', ventas_df.sum())

#Obtendremos el promedio de ventas de cada empleado
print('Promedio de ventas por empleados:\n', ventas_df.mean(axis=1))

#Obtendremos el promedio de ventas por dia
print('Promedio de ventas por empleados:\n', ventas_df.mean(axis=0))

#Obtendremos el dia con mas ventas de cada empleado
print('Dia con mas ventas por empleado:\n', ventas_df.idxmax(axis=1))

#El empleado que realizo mas ventas por dia
print('El empleado que realizo mas ventas por cada dia es:\n', ventas_df.idxmax(axis=0))
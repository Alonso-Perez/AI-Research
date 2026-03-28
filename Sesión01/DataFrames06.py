#crearemos un dataframe y exploraremos sus propiedades

import pandas as pd

#crearemos el dataframe

data={
    'Producto': ['Arroz', 'Leche', 'Cereal', 'Jamon', 'Huevos'],
    'Ventas':[250, 300, 400, 150, 500],
    'Stock':[20,30,15,50,10],
    'Precio':[10,15,20,5,25]
}
df=pd.DataFrame(data)

#Mostramos el Dataframe
print('El DataFrame es:\n', df)

#Seleccionar una columna
print('\nVentas:\n',df['Ventas'])

#Filtrar productos con ventas mayores a 300
productos_destacados=df[df['Ventas']>300]
print('\nProductos con ventas mayores a 300:\n', productos_destacados)
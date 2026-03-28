#Serie en pandas para explorar sus propiedades y realizar operaciones basicas

import pandas as pd

#Ejemplo de crear series
ventas=pd.Series([250, 300, 400, 150, 500],
                 index = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])

#mostrar la serie

print(f'Series de ventas:\n{ventas}')

#operaciones basicas
print('\nTotal de Ventas:', ventas.sum())
print('\nPromedio de Ventas:', ventas.mean())
print('\nDia con mayor numero de ventas:', ventas.idxmax())
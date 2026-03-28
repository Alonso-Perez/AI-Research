import pandas as pd

ventas_df=pd.DataFrame({
    'Lunes':[120, 250, 300, 180],
    'Martes':[150, 300, 350, 200],
    'Miercoles':[200,400,420,250],
    'Jueves':[100,150,200,120],
    'Viernes':[300,500,550,280]
}, index=['Producto A', 'Producto B', 'Producto C', 'Producto D'])

print("Mostrar el Dataframe de Ventas:\n", ventas_df)

#Cremos un metodo para buscar ventas de un prod. especifico
def buscar_producto(nombre_producto):
    if nombre_producto in ventas_df.index:
        print(f"\nVentas del producto {nombre_producto}\n {ventas_df.loc[nombre_producto]}")
    else:
        print("Producto no encontrado")

#ejemplo de busqueda
buscar_producto('Producto A')

def ordenar_por_dia(dia):
    if dia in ventas_df.columns:
        print(f'\nProductos ordenados por ventas el {dia}: \n{ventas_df[dia].sort_values(ascending=False)}')
    else:
        print('Dia no encontrado en el Dataframe')

ordenar_por_dia('Miercoles')
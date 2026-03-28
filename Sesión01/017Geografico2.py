import pandas as pd
import folium as fl
from folium.plugins import HeatMap

ventas_zonas=pd.read_csv('ventas_zonas.csv')
mapa=fl.Map(location=[19.4326, -99.1332], zoom_start=12)

heat_data=[[row['Latitud'], row['Longitud'], row['Ventas']] for index, row in ventas_zonas.iterrows()]

HeatMap(heat_data).add_to(mapa)
for index, row in ventas_zonas.iterrows():
    fl.Marker([row['Latitud'], row['Longitud']], 
              popup=f'{row['Zona']} ventas: {row['Ventas']}').add_to(mapa)
    
mapa.save("mapa_calor_ventas.html")
mapa
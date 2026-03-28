import pandas as pd
import folium as fl

#cargar los datos
ventas_ciudades=pd.read_csv("ventas_ciudades.csv")
#creamos el mapa
mapa=fl.Map(location=[19.4326, -99.1332], zoom_start=5)
for index, row in ventas_ciudades.iterrows():
    fl.Marker([row['Latitud'], row['Longitud']],
              popup=f"{row['Ciudad']} ventas: {row['Ventas']}").add_to(mapa)
    
#Guardamos el mapa en un archivo html
mapa.save("mapa_ventas.html")
mapa
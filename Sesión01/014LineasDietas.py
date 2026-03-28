import pandas as pd
import matplotlib.pyplot as plt


#leer archivo en csv
archivo_csv='reto_dieta.csv'
datos=pd.read_csv(archivo_csv)

#mostrar el contenido del archivo csv
print(datos)
#crearemos un grafico de lineas
plt.figure(figsize=(10,6))
#graficaremos los datos de Ana
plt.plot(datos['Mes'], datos['Ana'],marker='d', linestyle='--', label='Ana', color='y')
#graficaremos los datos de Mario
plt.plot(datos['Mes'], datos['Mario'], marker='D', linestyle='-', label='Mario', color='r')
#graficaremos los datos de Luis
plt.plot(datos['Mes'], datos['Luis'], marker='o', linestyle=':', label='Luis', color='g')

#añadir titulos y etiquetas(label)
plt.title("Evolucion del peso durante la dieta") #añade titulo

#añadir las leyendas
plt.legend()

#etiquetas a los ejes
plt.xlabel("Meses") 
plt.ylabel("Pesos (Kg)")

#añadimos una cuadrilla
plt.grid(True)

#guardaremos la grafica como un archivo de imagen
plt.savefig("EvolucionDieta.png")

#Mostramos el grafico
plt.show()

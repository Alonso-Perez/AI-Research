import pandas as pd
import matplotlib.pyplot as plt

archivo_csv="ventas_televisores.csv"

datos=pd.read_csv(archivo_csv)
print(datos)

plt.figure(figsize=(10,6)) #crearemos la tabla con sus respectivas dimensiones

#Crearemos las barras para cada mes y marca
ancho_barra=0.25
meses=datos['Mes']
indices=range(len(meses)) #rango que corresponda al arreglo de meses

#Crearemos las barras para la marca samsung (la barra central)
samsung_bars=plt.bar(indices, datos['Samsung'], width=ancho_barra, label='Samsung', color='g')

#Para LG
lg_bars=plt.bar([i-ancho_barra for i in indices], datos['LG'], width=ancho_barra, label='LG', color='r') #[i-ancho_barra for i in indices] esto hace que la barra los ponga antes de la barra central

#Para Sony
sony_bars=plt.bar([i+ancho_barra for i in indices],datos['Sony'], width=ancho_barra, label='Sony', color='b')#[i+ancho_barra for i in indices] esto hace que la barra los ponga despues de la barra central

#Tituulos y leyendas
plt.title("Ventas de televisores")
plt.legend()

#Añadir los meses en el eje x
plt.xticks(indices, meses)

#Etiquetas
plt.xlabel("Meses")
plt.ylabel("Cantidad vendida")

#Añadir la cuadricula
plt.grid(True, axis='y')


#Añadiremos los valores en la aprte superior de cada barr
def agregar_valores(barras):
    for bar in barras:
        yval=bar.get_height() #Obtenemos l altura de la barra
        plt.text(
            bar.get_x()+bar.get_width()/2, #posicion en el eje x
            yval+.5, #ponemos ligeramente arriba de la barra
            f'{yval:.0f}', #Esto para formatear en entero el texto que pongamos
            ha='center', va='bottom', fontsize=10 #Alineacion y tamaño del texto
        )


agregar_valores(lg_bars)
agregar_valores(samsung_bars)
agregar_valores(sony_bars)

#Mostrar las barras
plt.show()

#Guarda la figura
plt.savefig("Ventas de Televisores.png")
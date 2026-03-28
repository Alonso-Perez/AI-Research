#programa para predecir ingresos diarios en dólares para un negocio
#de helados
#Entrada: x=Temperatura exterior
#salida:  y=Ingresos diarios en dólares

import tensorflow as tf
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

#importaremos el set de datos
sales_df=pd.read_csv('datos_de_ventas.csv')
sns.scatterplot(data=sales_df,x='Temperature',y='Revenue')
plt.show()
#buscaremos la correlación entre la temperatura y la ganancia
#entrenando una red neuronal
#creamos el set de entrenamiento
X_train=sales_df['Temperature']
y_train=sales_df['Revenue']
#ahora crearemos el modelo, lo haremos de forma secuencial
model=tf.keras.Sequential()
#crearemos una capa de la red neuronal para encontrar la correlación
model.add(tf.keras.layers.Dense(units=1,input_shape=[1]))
#veamos el resumen del modelo
model.summary()
input('presiona enter para continuar...')
#compilaremos nuestro modelo, el valor optimizador de Adam será 0.1
model.compile(optimizer=tf.keras.optimizers.Adam(0.1),
              loss='mean_squared_error')
#vamos a entrenar nuestro modelo
epochs_hist=model.fit(X_train,y_train,epochs=1000)
#ahora veremos las llaves (parámetros) en pantalla
keys=epochs_hist.history.keys()
print(keys)
#crearemos un gráfico que muestre el entrenamiento del modelo
plt.plot(epochs_hist.history['loss'])
plt.title('Progreso de la pérdida durante el entrenamiento')
plt.xlabel('Epochs')
plt.ylabel('Pérdida del entrenamiento')
plt.legend('Pérdida del entrenamiento')
plt.show()
#ahora haremos predicciones sobre cuanto ganaremos con ciertas temperaturas
Temp=5
Revenue=model.predict(np.array([Temp]))
print('Con 5 grados, la ganancia según la red neuronal será de:',Revenue)
Temp=30
Revenue=model.predict(np.array([Temp]))
print('Con 30 grados, la ganancia según la red neuronal será de:',Revenue)
Temp=35
Revenue=model.predict(np.array([Temp]))
print('Con 35 grados, la ganancia según la red neuronal será de:',Revenue)
Temp=40
Revenue=model.predict(np.array([Temp]))
print('Con 40 grados, la ganancia según la red neuronal será de:',Revenue)
Temp=50
Revenue=model.predict(np.array([Temp]))
print('Con 50 grados, la ganancia según la red neuronal será de:',Revenue)
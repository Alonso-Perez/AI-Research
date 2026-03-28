import tensorflow as tf 
#para construir y entrenar modelos de aprendizaje 
# automático y redes neuronales
import pandas as pd #para cargar nuestro set de datos
import numpy as np# para el manejo de matrices
import seaborn as sns#para hacer visualizaciones de nuestro modelo
import matplotlib.pyplot as plt #para hacer plots de nuestro modelo
#controla el uso de las optimizaciones de rendimiento en TensorFlow 
TF_ENABLE_ONEDNN_OPTS=0
#Importando Dato
temperature_df = pd.read_csv("celsius_a_fahrenheit.csv")
#Visualizacion de los datos 
sns.scatterplot(data=temperature_df, x='Celsius', y='Fahrenheit')
plt.show()
#puedes ejecutar aquí
#Cargando Set de Datos
X_train = temperature_df['Celsius']
y_train = temperature_df['Fahrenheit']
# crea un modelo de red neuronal secuencial
#Keras es una API de alto nivel que proporciona una manera sencilla 
# de construir y entrenar redes neuronales.
model = tf.keras.Sequential()
#Por qué "secuencial"?
#Se utiliza cuando los datos fluyen directamente desde la entrada hacia 
# la salida en un orden definido.
#agregamos una capa de input solo crearemos una neurona
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
#el modelo tendrá una capa densa con 1 neurona y una entrada de 1 dimensión.
model.summary()
input('Presiona enter para continuar...')
#Compilado llamamos al optimizador adam (cambiarás luego a 1)
#Adaptive Moment Estimation usa dos algoritmos
#RMSProp: Mantiene una tasa de aprendizaje ajustada automáticamente
#  para cada parámetro.
#Momentum: Acelera la convergencia acumulando información de 
# gradientes anteriores.
#El número 0.5 es la tasa de aprendizaje (learning rate)
#Pequeño (e.g., 0.001): Aprendizaje más lento pero más estable.
#Grande (e.g., 0.5): Aprendizaje rápido, pero con riesgo de no 
# converger o saltar el óptimo.
#Controla qué tan grandes serán los pasos al actualizar los parámetros.
#Adam Este método compila el modelo
#loss='mean_squared_error' Define cómo medir el error entre las 
# predicciones del modelo y los valores reales durante el entrenamiento.
model.compile(optimizer=tf.keras.optimizers.Adam(0.5), 
              loss='mean_squared_error')

#Entrenando el modelo
#fit es el método que entrena el modelo.
#En cada época, el modelo realiza:
#Un pase hacia adelante (forward pass) para calcular las predicciones.
#Un pase hacia atrás (backward pass) para ajustar los pesos usando 
# el optimizador. Una época es un pase completo por todo el conjunto 
# de entrenamiento. Cada vez que el modelo recorre los datos, ajusta 
# sus pesos con base en los errores calculados
epochs_hist = model.fit(X_train, y_train, epochs = 100)
#imprime la pérdida cada vez
print(epochs_hist.history['loss'])
input('estas aqui')
#Evaluando modelo un epoch es una pasada por todo el set de entrenamiento
epochs_hist.history.keys()
#puedes compilar
#Graficamos el modelo
plt.plot(epochs_hist.history['loss'])
#ponemos titulo al gráfico
plt.title('Progreso de Pérdida durante Entrenamiento del Modelo')
#titulo del eje x
plt.xlabel('Epoch')
#titulo del eje y
plt.ylabel('Training Loss')
#leyenda del gráfico
plt.legend('Training Loss')
plt.show()
#Para ver los pesos

#Predicciones que hace nuestro modelo
#le damos una temperatura en Centigrados
Temp_C = 0
print('si la temperatura en grados centígrados es:',Temp_C)
#nos debe mostrar una temperatura de salida  convertida a fahrenheit
Temp_F = model.predict(np.array([Temp_C]))
#mostramos al usuario la temperatura que predice el sistema
print("Temperatura de Predicción: " + str(Temp_F))
#ahora aplicaremos la formula correcta para ver si coincide con la
#predicción del modelo
Temp_F = 9/5 * Temp_C + 32
print("Temperatura de Ecuación: " + str(Temp_F))
tempUser=int(input('Escribe una temperatura en grados centígrados: '))
Temp_F = model.predict(np.array([tempUser]))
print('La temperatura en grados Fahrenheit según el modelo es:',Temp_F)
Temp_F = 9/5 * tempUser + 32
print('La temperatura en grados Fahrenheit según el la fórmula es:',Temp_F)


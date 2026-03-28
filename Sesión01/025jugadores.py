#predicción con regresion logistica
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
#con esto dividiremos datos en datos de entrenamiento y datos de prueba
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
#para hacer regresión logistica
from sklearn.metrics import accuracy_score,classification_report
#se utiliza para medir los parámetros que indiquemos

#creamos el dataset sintético
np.random.seed(42)
num_players=200 #cantidad de jugadores
#trataremos de predecir la posición de un jugador de futbol soccer
#de acuerdo a sus carácteristicas atleticas
#generaremos características aleatorias
height=np.random.normal(180,10,num_players)#altura (cm)
#180 (media) : representa la media de la distribución normal
# 10 (scale o desviación estandar) de la distribución normal
#num_players la cantidad de datos a generar (por jugador)
weigth=np.random.normal(75,10,num_players) #peso (kg)
speed=np.random.normal(7,1.5,num_players)# Velocidad (m/s)
passing=np.random.uniform(50,100,num_players)#presicion de los pases (%)
stamina=np.random.uniform(30,100,num_players)#resistencia(%)
#30 es el limite inferior del rango (low)
#100 es el límite superior del rango (high)
#num_players (size) cantidad de números que se desea generar

#asignando etiquetas (posicion del jugador: 0 defensa, 1 mediocampista
#2 delantero)
positions=np.random.choice([0,1,2], size=num_players,p=[0.3,0.4,0.3])
#p=[0.3,0.4,0.3] probabilidades de cada uno de las posiciones

#crearemos el dataframe
data=pd.DataFrame({
    'Altura':height,
    'Peso':weigth,
    'Velocidad':speed,
    'Pases':passing,
    'Resistencia':stamina,
    'Posición':positions
})
print('El contenido del dataframe es:\n',data)
input('Presione enter para continuar...')
#separaremos características y etiquetas
X=data[['Altura','Peso','Velocidad','Pases','Resistencia']]
y=data['Posición']

#escalar las características con StandarScaler, se crea un objeto escalador
scaler= StandardScaler()
#estandariza para que los datos esté dentro del rango del 0 al 1 
#y tengan 'pesos' similares
X_scaled=scaler.fit_transform(X)
#fit calcula la media y la desviación estandar de cada columna en X
#y transform aplica la transformación 

#dividir los datos en conjuntos de entrenamiento y de prueba
X_train, X_test, y_train, y_test=train_test_split(X_scaled,y,test_size=0.2,
                                                  random_state=42)
#X_scaled son las características (variables independientes) escaladas
#y son las etiquetas o valores que queremos predecir (variable independiente)
#test_size=.02 define el tamaño del conjunto de prueba como un 20%
#dejando el 80% para entrenamiento
#random_state=42 establece una semilla para el generador aleatorio

#entrenamos el modelo
model=LogisticRegression(random_state=42,max_iter=200)
model.fit(X_train,y_train)
#entrena el modelo usando los datos de entrenamiento 

#evaluaremos el modelo
y_pred=model.predict(X_test)
#esta función utiliza el modelo ya entrenado para realizar predicciones
#basandose en el conjunto de características de prueba (X_test)
accuracy=accuracy_score(y_test,y_pred)
#accuracy_score es una metrica que calcula la exactitud del modelo
#en porcentaje utilizando como entrada y_test
#y como salida y_pred las etiquetas predichas por el modelo para X_test
#como resultado se obtiene un valor entre 0 y 1 que representa la 
#proporcion de ejemplos correctamente clasificados

#mostrar resultados

print(f'Presición del modelo: {accuracy:.2f}')
print('\nReporte de clasificación:')
print(classification_report(y_test,y_pred,target_names=['Defensa',
                                                        'Mediocampista',
                                                        'Delantero']))
#determinaremos si acertamos en la predicción sobre si el jugador tiene 
# características para ser titular o suplente
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

#crearemos el dataset
data = {
    "MinutosJugados": [90, 85, 30, 15, 70, 45, 80, 10, 60, 90, 20, 75, 50, 5, 85, 40, 95, 25, 10, 70],
    "Goles": [1, 2, 0, 0, 0, 1, 1, 0, 0, 2, 0, 0, 1, 0, 1, 0, 2, 0, 0, 1],
    "Asistencias": [0, 1, 0, 0, 1, 1, 1, 0, 0, 2, 0, 1, 0, 0, 1, 0, 2, 0, 0, 1],
    "Titular": [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1]
}

df=pd.DataFrame(data)
print('El contenido del dataframe es:\n',df)
input('Presiona enter para continuar')
#dividiremos en características (X) y etiquetas (y)
X=df[['MinutosJugados','Goles','Asistencias']]
y=df['Titular']

#escalado de las características
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

#dividiremos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test=train_test_split(X_scaled,y,test_size=0.25,
                                                  random_state=42)
#entramos el modelo
model=LogisticRegression(random_state=42,max_iter=200)
model.fit(X_train,y_train)

#predecir y evaluar el modelo
y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
input('Presiona enter para continuar...')
print(f'Exactitud del modelo: {accuracy:.2f}')

#reporte de clasificación
print('Reporte de clasificación')
print(classification_report(y_test,y_pred,target_names=['Suplente','Titular']))
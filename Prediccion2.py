import numpy as np
import matplotlib as mp
from sklearn.linear_model import LinearRegression as lr
from sklearn.preprocessing import StandardScaler as ss

X = np.array([
    [1, 1], [2, 1], [3, 2], [4, 2], [5, 2], 
    [6, 3], [7, 3], [8, 3], [9, 3], [10, 3]
])

y = np.array([1500, 1800, 2400, 2700, 3000, 3800, 4200, 4600, 5000, 5500])

#Escalado
#Esto permite que los años y el nivel de estudio permitan tener un mismo idioma numérico
scaler = ss()
X_escalado = scaler.fit_transform(X)

#Entrenamos al modelo
modelo = lr()
modelo.fit(X_escalado, y)


#Prediccion
nueva_persona = np.array([[5, 2]])
nueva_persona_escalada = scaler.transform(nueva_persona)

prediccion=modelo.predict(nueva_persona_escalada)

print(f"Salario estimado para una persona de 5.5 años y nivel 2: ${prediccion[0]:.2f}")
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression as lr
from sklearn.preprocessing import StandardScaler as ss

df = pd.read_csv('datos_salario.csv')

X = df[['Anos_Experiencia', 'Nivel_Educativo']]
y = df['Salario']

scaler = ss()
X_escalado = scaler.fit_transform(X)

modelo = lr()
modelo.fit(X_escalado, y)

nuevo_empleado = np.array([[7.2, 3]])
nuevo_empleado_escalado = scaler.transform(nuevo_empleado)

prediccion = modelo.predict(nuevo_empleado_escalado)

print(f"El sueldo del empleado con {nuevo_empleado[0][0]} anos y {nuevo_empleado[0][1]} de nivel educativo, le corresponde: ${prediccion[0]:.2f}")

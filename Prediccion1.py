import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LR

# Introduciremos datos de ejemplo (Entradas: Años de experiencia)
# Reorganizamos los datos con .reshape(-1, 1), por que el modelo espera una matriz
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)

# Datos de salida (salario real observado)
y = np.array([1500, 1800, 2100, 2500, 2800, 3200, 3500, 4000, 4300, 4800])

# Crear el modelo y entrenarlo

modelo = LR()
modelo.fit(X, y)


# Realizar predicción para alguien con 5.5 años de experiencia
nueva_entrada = np.array([[5.5]])
prediccion = modelo.predict(nueva_entrada)

print(f"Para 5.5 años de experiencia, el salario estimado es: ${prediccion[0]:.2f}")

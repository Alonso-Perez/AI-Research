import pandas as pd
import numpy as np

np.random.seed(42)

n_datos = 100

years = np.round(np.random.uniform(1, 15, n_datos), 1)
level = np.random.randint(1, 4, n_datos)

ruido = np.random.normal(0, 150, n_datos)
salario = (1200 + (years*350) + (level*600) + ruido).astype(int)


df = pd.DataFrame({
    'Anos_Experiencia': years,
    'Nivel_Educativo': level,
    'Salario': salario
})

df.to_csv('datos_salario.csv', index=False)

print("¡Archivo 'datos_salarios.csv' creado con éxito!")
print(df.head())
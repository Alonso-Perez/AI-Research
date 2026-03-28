import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('correos.csv')

X = df[['Palabras_Sospechosas', 'Errores_Ortograficas']]
encoder = LabelEncoder()
y = encoder.fit_transform(df['Categoria'])

modelo = LogisticRegression()
modelo.fit(X, y)

nuevo_correo = [[9, 6]]
prediccion = modelo.predict(nuevo_correo)
probabilidad = modelo.predict_proba(nuevo_correo)

resultado_literal = encoder.inverse_transform(prediccion)

print(f"Resultado del análisis: {resultado_literal[0]}")
print(f"La probabilidad de que el correo sea Spam es de {probabilidad[0][1]*100:.2f}%")
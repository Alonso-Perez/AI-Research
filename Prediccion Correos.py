import pandas as pd
from sklearn.linear_model import LogisticRegression

X = [
    [1, 0], [0, 1], [1, 2],   # Ejemplos de correos normales (Clase 0)
    [10, 5], [8, 7], [12, 4]  # Ejemplos de Spam (Clase 1)
]

y = [0,0,0,1,1,1]

modelo = LogisticRegression()
modelo.fit(X, y)

nuevo_correo = [[9, 6]]
prediccion = modelo.predict(nuevo_correo)
probabilidad = modelo.predict_proba(nuevo_correo)

clase = 'SPAM' if prediccion[0] == 1 else 'Normal'
print(f"El sistema clasifica al correo como {clase}")
print(f"La probabilidad de que el correo sea Spam es de {probabilidad[0][1]*100:.2f}%")
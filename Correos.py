import pandas as pd
import numpy as np

#COnfiguracion de semilla random
np.random.seed(42)
n_correos = 100


#Generador de datos numéricos aleatorios
palabras_sospechosas = np.random.randint(0, 15, n_correos)
errores_ortograficos = np.random.randint(0, 10, n_correos)

#Generar etiqueta literal basada en regla lógica con ruido
#Si (palabras > 7) y (errores>3) entonces es probable que sea spam

etiquetas = []

for i in range(n_correos):
    score = palabras_sospechosas[i] + errores_ortograficos[i]
    if score > 10:
        etiquetas.append('Spam')
    else:
        etiquetas.append('Normal')

df_correos = pd.DataFrame({
    'Palabras_Sospechosas': palabras_sospechosas,
    'Errores_Ortograficas': errores_ortograficos,
    'Categoria': etiquetas
})

df_correos.to_csv('correos.csv', index='False')
print("¡Archivo 'correos.csv' creado con etiquetas literales!")
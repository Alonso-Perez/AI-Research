#dividiremos los datos de entrenamiento (80%) y prueba (20%)
#y visualizaremos como se distribuyen las características en ambos conjuntos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split

#crearemos un dataset simulando ventas deportivas
np.random.seed(42)

#simular los datos
n_samples=500
data = {
    "Producto": np.random.choice(["Balón", "Raqueta", "Zapatillas", "Pesas"], size=n_samples),
#np.random.choice: Es una función de la biblioteca numpy que permite elegir elementos 
# aleatoriamente de un conjunto o arreglo.
#size=n_samples: Indica cuántos productos se deben generar.
    "Categoría": np.random.choice(["Fútbol", "Tenis", "Correr", "Gimnasio"], size=n_samples),
    "Precio": np.random.randint(10, 500, size=n_samples),
    "Cantidad_Vendida": np.random.randint(1, 50, size=n_samples),
    "Región": np.random.choice(["Norte", "Sur", "Este", "Oeste"], size=n_samples),
    "Ingresos": lambda df: df["Precio"] * df["Cantidad_Vendida"],
    #El cálculo de esta columna se realiza mediante una función lambda 
    #En esta etapa, data es simplemente un diccionario que incluye instrucciones
    #  para calcular la columna "Ingresos". el cálculo real se realiza más adelante
}
#creamos el dataframe
df=pd.DataFrame(data)
df['Ingresos']=df['Precio']*df['Cantidad_Vendida']
#aqui se realiza el cálculo

print('DataFrame de ventas deportivas (Encabezado):')
print(df.head())
input('presiona enter para continuar...')
#Separamos caracteristicas (X) y los objetivos (y)
X=df.drop(columns=['Ingresos'])
y=df['Ingresos']
X_train, X_test,y_train, y_test=train_test_split(X,y,test_size=0.2,
                                                 random_state=42)

#visualizaremos las distribuciones de las caracteristicas con
#los datos de la columna que se envía como parámetro
def plot_distributions(df_train,df_test,column):
    plt.figure(figsize=(10,6))
    sns.kdeplot(df_train[column],label='Entrenamiento',fill=True,alpha=0.5)
    sns.kdeplot(df_test[column], label='Prueba',fill=True,alpha=0.5)
    plt.title(f'Distribución de {column} (Conjunto de Entrenamiento y Prueba)')
    plt.legend()
    plt.show()

#llamamos a la función
numerical_column=['Precio','Cantidad_Vendida']
for col in numerical_column:
    plot_distributions(X_train,X_test,col)
#numerical_column es la lista que contiene los nombres de las columnas
# que son numéricas en el conjunto de datos
#col es una variable que en cada iteración toma los valores de cada lista
#orimero de la lista precio y despues de la lista cantidad_vendida
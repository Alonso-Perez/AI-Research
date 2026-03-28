import pandas as pd

#URL de Internet
url="https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"

df=pd.read_csv(url)

promedio_gdp=df.groupby('continent')['gdpPercap'].mean().reset_index()
#El resultado de roupby es una serie, para volver  convertirla en dataframe, usamos resent_index

promedio_gdp=promedio_gdp.sort_values(by='gdpPercap')
#ordena las filas en funcion de la columna gdpPercap (por defecto es de menor a mayor)


print('El ingreso per capita por continent ordenado de menor a mayor es:')
print(promedio_gdp)


#Ahora ordenamos de mayor a menor
promedio_gdp=promedio_gdp.sort_values(by='gdpPercap', ascending=False)
print('\n El ingreso per capita por continent ordenado de mayor a menor es:')
print(promedio_gdp)

#Ordenar la esperanza de vida promedio (lifeExp) por continente de menor a mayor
promedio_lif_exp=df.groupby('continent')['lifeExp'].mean().reset_index()

#Ordenamos
promedio_lif_exp=promedio_lif_exp.sort_values(by='continent')

print('El promedio de esperanza de vida por continente de menor a mayor es:')
print(promedio_lif_exp)


#Mostrar el total de población (pop) por pais, de mayor a menor 
total_poblacion=df.groupby('country')['pop'].sum().reset_index()
total_poblacion=total_poblacion.sort_values(by='pop', ascending=False)
print('El total de población por país de mayor a menor es:')
print(total_poblacion, '\n')

#Ordenar el promedo de ingresos perfapita (gdp) en el año 2007
#de menor a mayor, agrupamos por continent

df_2007=df[df['year']==2007] #Filtramos los datos cuyo año sean solo de 2007
promedio_gdp_2007=df_2007.groupby('continent')['gdpPercap'].mean().reset_index()
print('Promedio de ingresos per capita del año 2007 por continente de menor a mayor')
print(promedio_gdp_2007)

#filtraremos datos del año 2007 y paises de Asia, luego calcularemos la esperanza de vida (lifeExp) por pais, ordenado
#de mayor a menor

#Filtrar solo los datos de 2007 y continente Asia

df_2007_Asia=df[(df['year']==2007) & (df['continent']=='Asia')]

#calcular el promedio de esperanzas de vida por pais

promedio_life_exp_asia_2007=df_2007_Asia.groupby('country')['lifeExp'].mean().reset_index()

#ordenamos de mayor a menor
promedio_life_exp_asia_2007=promedio_life_exp_asia_2007.sort_values(by='lifeExp', ascending=False)
print('Promedio de esperanza de vida en Asia (2007) ordenado de mayor a menor:')
print(promedio_life_exp_asia_2007,'\n')


#Filtrar los datos del continente de Africa con ingresos per-capita mayora a 1000 y calcular el total de poblacion por pais, ordenado de menor a mayor

#filtrar datos de africa con ingreso percapta mayor a 1000
df_africa_gdp_1000=df[(df['continent']=='Africa')&(df['gdpPercap']>1000)]

#calculamos el total de poblacion por pais
total_pob_africa=df_africa_gdp_1000.groupby('country')['pop'].sum().reset_index()
total_pob_africa=total_pob_africa.sort_values(by='pop')
print('El total de poblacion en Africa con ingresos per capita > 1000 de menor a mayor es:')
print(total_pob_africa)
# Project 2. Storytelling

![Screenshot](input/Airbnb-Madrid-01.png)

Este proyecto parte de un dataset de Airbnb en Madrid (https://www.kaggle.com/rusiano/madrid-airbnb-data?select=listings.csv). 

Hay una reunión con un posible comprador de tu producto/servicio y debes convencerle para que compre.

Partiendo del dataset hay que limpiarlo, analizarlo, aplicar gráficos y mediante la técnica del storytelling convencer al usuario.

## 1. Data Cleansing
Se han importado dos archivos .csv conectados por un mismo id. Uno de los archivos es el mismo que el otro pero ya está limpio, se puede decir que es el mismo pero con menos columnas y con algunos cambios. Por ejemplo, la columna 'price' en el archivo limpio aparece en valor y sin el signo $. 

Lo que se ha hecho es coger el máximo de columnas que se consideran necesarias del archivo limpio y por otro lado las de interés del archivo sin limpiar y mediante la funcion merge() se han fusionado en un único dataset para su análisis.

Para terminar se han eliminado elementos nulos y se ha exportado a un .csv limpio.

## 2. Análisis y segunda limpieza
Se ha realizado un análisis más detallado del dataset, agrupando y visualizando con gráficas los datos considerados de interés para un usuario a la hora de buscar alojamiento.

Durante este primer análisis se ha reducido el dataset eliminando datos con valores raros que se salían d ela media y se ha exportado el nuevo dataset a otro .csv definitivo.

## 3. Storytelling
Esta es la carta de presentación para el posible comprador.

### 3.1. Análisis Airbnb Madrid
Existe un total de 19.305 diferentes alojamientos distribuidos por la Comunidad de Madrid. Airbnb agrupa estas ofertas en 21 zonas o vecindarios.

A través de diferentes gráficas enseñamos al usuario las conclusiones del análisis:
- La mayoría de los alojamientos que ofrece Airbnb estan ubicados en la zona centro.
- El 60.8% de los alojamientos son del tipo 'apartamento', seguido de las habitaciones privadas con un 35.8%, suponen el 96.6% del mercado de Airbnb.
- El precio medio en Airbnb es de 72€/noche, siendo el menor 8€ y el mayor 299€.
- El precio varía en función de las zonas, siendo la zona más cara el barrio de Salamanca con un precio medio por alojamiento de 88€/noche, y la más barata Villaverde con un precio medio de 39€/noche.
- Por otro lado, en cuanto al tipo de alojamiento, el más caro son los apartamentos y el más bajo las habitaciones compartidas.

### 3.2. Búsqueda de alojamiento
Con el análisis previo, el usuario ya conoce más o menos las condiciones de los alojamientos en Madrid, contando con ese conocimiento vamos a ayudarle a encontrar su sitio ideal.

El sistema le pide al usuario los siguientes datos (mostrando las opciones disponibles):
- Tipo de alojamiento
- Número de personas
- Precio mínimo y máximo que está dispuesto a pagar
- Lugares que va a visitar durante su estancia

Los tres primeros datos son considerados los filtros mínimos requeridos por el usuario para su búsqueda. Con estos datos se reduce el dataframe a las opciones que cumplen con los requisitos indicados.

Con las zonas que quiere visitar el usuario, se calcula la media de las distancias a esos lugares desde cada alojamiento y se muestra una lista definitiva de recomendaciones con las opciones más óptimas para el usuario.

Por último se pide al usuario que escoja una de las opciones e introduzca el id del alojamiento para mostrarle la información más ordenada y detallada del mismo, así como el link directo a la página de la oferta en Airbnb.

## 4. Extracción de datos por funciones

Este último archivo contiene la importación y la documentación de 4 de las funciones utilizadas a lo largo del proyecto, de manera que permiten a una persona eligir parametros de los datos y recibir datos relevantes (tablas, graficas, etc)

Funciones accesibles:
- Mapa de distribución de alojamientos por el parámetro que indique el usuario
- Gráfico de barras que muestra los alojamientos en función de un parámetro
- Función que imprime los valores únicos de una columna
- Función que calcula las distancias de cada alojamiento a una ubicación dada y lo incluye en una nueva columna en el dataset







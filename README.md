# Project 2. Storytelling
![Screenshot](input/Airbnb-Madrid-01.png)

Este proyecto parte de un dataset de Airbnb en Madrid. Hay una reunión con un posible comprador de tu producto/servicio y debes convencerle para que compre.
Partiendo del dataset hay que limpiarlo, analizarlo, aplicar gráficos y mediante la técnica del storytelling convencer al usuario.

# 1. Data Cleansing
Se han importado dos archivos .csv conectados por un mismo id. Uno de los archivos es el mismo que el otro pero ya está limpio, se puede decir que es el mismo pero con menos columnas y con algunos cambios. Por ejemplo, la columna 'price' en el archivo limpio aparece en valor y sin el signo $. 
Lo que se ha hecho es coger el máximo de columnas que se consideran necesarias del archivo limpio y por otro lado las de interés del archivo sin limpiar y mediante la funcion merge() se han fusionado en un único dataset para su análisis.
Para terminar se han eliminado elementos nulos y se ha exportado a un .csv limpio.

# Análisis y segunda limpieza


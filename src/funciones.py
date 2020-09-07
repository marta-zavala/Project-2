import pandas as pd
import numpy as np
from math import sin, cos, sqrt, atan2,radians
import matplotlib.pyplot as plt
import seaborn as sns

# Calcular distancias

def dist(df,lonM,latM):
    madrid_lat,madrid_long = radians(lonM), radians(latM)
    R = 6373.0
    lon = radians(df['longitude'])
    lat = radians(df['latitude'])
    
    dlon = lon - madrid_long
    dlat = lat - madrid_lat
    a = sin(dlat / 2)**2 + cos(lat) * cos(madrid_lat) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return round(R * c,2)


# Mapa distribución por columnas
def mapa(lon,lat,col):
    plt.figure(figsize=(10,6))
    sns.scatterplot(lon, lat ,hue=np.asarray(col))
    return plt.ioff()

# Imprime los valores únicos de una columna
def imprime_opciones(col):
    for i in range(len(col.unique())):
        print(f' {i+1}. {col.unique()[i]}')

# Extraer información
def ext_info(col1,ap_id,aloj):
    dev=col1[ap_id==aloj].to_string(index=False)
    return dev

# Gráfica alojamientos/parámetro
def recnt(columna):
    f,ax = plt.subplots(figsize=(30,5))
    ax = sns.countplot(columna,palette="muted")
    return(plt.show())
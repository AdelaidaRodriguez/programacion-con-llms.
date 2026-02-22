import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
import random

def generar_caso_de_uso_imputar_datos():
    # Generamos datos aleatorios para la prueba
    n_filas = random.randint(10, 15)
    datos = np.random.rand(n_filas, 3) * 100
    X = pd.DataFrame(datos, columns=['feat_1', 'feat_2', 'feat_3'])
    
    # Forzamos algunos nulos para que la función tenga qué limpiar
    X.iloc[1, 0] = np.nan
    X.iloc[3, 2] = np.nan
    
    input_data = {'X': X.copy()}
    
    # Calculamos lo que debería dar
    imputer = SimpleImputer(strategy='median')
    X_esperado = imputer.fit_transform(X)
    
    return input_data, X_esperado

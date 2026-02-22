import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import random

def generar_caso_de_uso_estandarizar_datos():
    # Generamos una matriz de datos con escalas muy diferentes
    n_filas = 10
    datos = {
        'edad': [random.randint(18, 80) for _ in range(n_filas)],
        'salario': [random.randint(1000000, 5000000) for _ in range(n_filas)]
    }
    X = pd.DataFrame(datos)
    
    input_data = {'X': X.copy()}
    
    # Respuesta esperada usando StandardScaler
    scaler = StandardScaler()
    X_escalado = scaler.fit_transform(X)
    
    return input_data, X_escalado

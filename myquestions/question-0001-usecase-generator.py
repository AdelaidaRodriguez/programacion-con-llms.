import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_limpiar_nulos():
    # Creamos datos de prueba
    n = random.randint(10, 15)
    df = pd.DataFrame({
        'sensor_id': range(n),
        'lectura': [random.choice([10.5, 20.1, np.nan]) for _ in range(n)]
    })
    
    # Preparamos la entrada para el compañero
    input_data = {'df': df.copy(), 'columna': 'lectura'}
    
    # Resultado esperado (lo que la función del compañero DEBE devolver)
    output_expected = df.dropna(subset=['lectura']).reset_index(drop=True)
    
    return input_data, output_expected

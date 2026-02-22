import pandas as pd
import random

def generar_caso_de_uso_filtrar_criticos():
    # Creamos un inventario aleatorio
    n = 20
    data = {
        'producto': [f'Prod_{i}' for i in range(n)],
        'stock': [random.randint(5, 30) for _ in range(n)],
        'precio': [random.uniform(10, 100) for _ in range(n)]
    }
    df = pd.DataFrame(data)
    
    input_data = {'df': df.copy()}
    
    # Respuesta esperada: stock < 15 Y precio > 50
    output_expected = df[(df['stock'] < 15) & (df['precio'] > 50.0)]
    
    return input_data, output_expected

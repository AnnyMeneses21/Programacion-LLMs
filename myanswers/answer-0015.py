import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler

def preparar_datos_masas_agua(df: pd.DataFrame, target_col: str) -> tuple[np.ndarray, np.ndarray]:
    """
    Recibe un DataFrame oceanográfico con valores nulos y outliers,
    separa las características de la variable objetivo, imputa usando
    la media de la columna y escala usando RobustScaler.
    
    Args:
        df: DataFrame de pandas con las variables físicas y la columna objetivo.
        target_col: Nombre de la columna que actúa como variable objetivo.
        
    Returns:
        X_scaled: Matriz bidimensional de numpy con las características procesadas.
        y: Array unidimensional de numpy con las etiquetas de la masa de agua.
    """
    # 1. Separar variables independientes (X) de la variable objetivo (y)
    X_raw = df.drop(columns=[target_col])
    y = df[target_col].to_numpy()  # .values también sirve, pero .to_numpy() es más moderno
    
    # 2. Instanciar y aplicar el Imputador (Estrategia: Media)
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X_raw)
    
    # 3. Instanciar y aplicar el Escalador Robusto
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X_imputed)
    
    return X_scaled, y

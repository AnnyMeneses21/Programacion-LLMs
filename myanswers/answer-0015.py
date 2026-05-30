import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from typing import Tuple
 
 
def masas_agua(df: pd.DataFrame, target_col: str) -> Tuple[np.ndarray, np.ndarray]:
    """
    Prepara datos de sensores oceanográficos para un modelo de ML.
 
    Args:
        df: DataFrame con variables oceanográficas y una columna objetivo.
        target_col: Nombre de la columna objetivo (variable a predecir).
 
    Returns:
        Tupla (X, y) donde:
            X: Matriz de características imputada y escalada (numpy array).
            y: Vector objetivo (numpy array).
    """
    # 1. Separar características (X) y variable objetivo (y)
    X_raw = df.drop(columns=[target_col])
    y = df[target_col].values
 
    # 2. Imputar valores faltantes con la media de cada columna
    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X_raw)
 
    # 3. Escalar con RobustScaler (robusto ante outliers)
    scaler = RobustScaler()
    X = scaler.fit_transform(X_imputed)
 
    return X, y

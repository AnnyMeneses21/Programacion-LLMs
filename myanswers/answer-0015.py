import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler

def preparar_datos(df, target_col):
    X = df.drop(columns=[target_col])

    # ndarray de strings, pero forzado a dtype=str
    y = np.array(df[target_col].astype(str).tolist(), dtype=str)

    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    return X_scaled, y

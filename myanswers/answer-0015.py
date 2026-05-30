import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler

def preparar_datos(df, target_col):
    X = df.drop(columns=[target_col])

    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    # versión de prueba
    y = pd.Series(df[target_col].values)

    return X_scaled, y

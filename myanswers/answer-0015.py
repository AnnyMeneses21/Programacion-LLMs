import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler

def preparar_datos(df, target_col):

    X = df.drop(columns=[target_col]).to_numpy()
    y = df[target_col].to_numpy()

    imputer = SimpleImputer(strategy="mean")
    X = imputer.fit_transform(X)

    scaler = RobustScaler()
    X = scaler.fit_transform(X)

    return X, y

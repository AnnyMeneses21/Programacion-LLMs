import numpy as np
import pandas as pd
from sklearn.decomposition import NMF

def extraer_patrones_consumo(df, n_components):
    X = df.to_numpy()

    modelo = NMF(
        n_components=n_components,
        init="random",
        random_state=42,
        max_iter=500
    )

    W = modelo.fit_transform(X)
    H = modelo.components_

    X_reconstruida = np.dot(W, H)
    rmse = float(np.sqrt(np.mean((X - X_reconstruida) ** 2)))

    return W, H, rmse

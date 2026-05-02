import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def seleccionar_features_estables_bootstrap(X, y, n_iter=100, top_k=5, random_state=42):
    rng = np.random.default_rng(random_state)
    n = len(X)
    cols = X.columns.to_list()
    counts = {c: 0 for c in cols}
    y_arr = np.asarray(y)

    for i in range(n_iter):
        idx = rng.integers(0, n, size=n)
        Xb = X.iloc[idx]
        yb = y_arr[idx]

        model = RandomForestClassifier(
            n_estimators=150,
            random_state=random_state + i,
            n_jobs=-1
        )
        model.fit(Xb, yb)

        importances = model.feature_importances_
        top_idx = np.argsort(importances)[::-1][:top_k]
        for j in top_idx:
            counts[cols[j]] += 1

    df_out = pd.DataFrame({
        "feature": cols,
        "conteo_top_k": [counts[c] for c in cols]
    })
    df_out["frecuencia"] = df_out["conteo_top_k"] / n_iter

    return df_out.sort_values("frecuencia", ascending=False).reset_index(drop=True)

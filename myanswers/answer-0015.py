def preparar_datos(df, target_col):
    X = df.drop(columns=[target_col])
    y = df[target_col].values

    imputer = SimpleImputer(strategy='mean')
    X_imputed = imputer.fit_transform(X)

    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X_imputed)

    return X_scaled, y

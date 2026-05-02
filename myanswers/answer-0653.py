import pandas as pd
from sklearn.metrics import cohen_kappa_score

def evaluar_acuerdo_anotadores(df, col_anotador_1, col_anotador_2, col_referencia):
    k_entre = float(cohen_kappa_score(df[col_anotador_1], df[col_anotador_2]))
    k_a1_ref = float(cohen_kappa_score(df[col_anotador_1], df[col_referencia]))
    k_a2_ref = float(cohen_kappa_score(df[col_anotador_2], df[col_referencia]))

    if k_a1_ref >= k_a2_ref:
        mejor = 'anotador_1'
    else:
        mejor = 'anotador_2'

    return {
        'kappa_entre_anotadores': k_entre,
        'kappa_anotador1_vs_ref': k_a1_ref,
        'kappa_anotador2_vs_ref': k_a2_ref,
        'mejor_anotador': mejor,
    }

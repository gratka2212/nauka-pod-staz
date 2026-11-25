import pandas as pd
import numpy as np

# IMPORTING DATA AND DISPLAYING BASIC INFO
oferty = pd.read_csv("oferty_it.csv")
print(f"----------------------------------------\n\nWymiary tablicy: {oferty.shape}\n\n----------------------------------------\n\nINFO:\n{oferty.info}\n\n----------------------------------------\n\nBrakujące wartości:\n{oferty.isna().sum()}")

# CLEANING DATA
oferty.drop_duplicates()
oferty.replace(["Poznan", "data analyst"], ["Poznań", "Data Analyst"], inplace=True)
oferty = oferty.dropna(subset=["stanowisko", "stawka_pln"])
oferty['miasto'] = oferty["miasto"].fillna("Nie podano")
oferty["doswiadczenie_lata"] = oferty["doswiadczenie_lata"].fillna(oferty["doswiadczenie_lata"].median())
oferty = oferty[oferty['stawka_pln'] > 0]

[Q1, Q3] = np.percentile(oferty["stawka_pln"], [25, 75])

iqr = Q3 - Q1

oferty = oferty[oferty['stawka_pln'] <= 1.5*iqr]
oferty["stawka_roczna"] = oferty["stawka_pln"]*12

statystyki = oferty.groupby('stanowisko')['stawka_pln'].agg(
    liczba_ofert="count",
    średnia="mean",
    mediana="median",
    odchylenie="std"
)

oferty.to_csv("oferty_it_czyste.csv", index=False)
import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

dane = {
    "id_oferty": np.arange(1001, 1001 + n),
    "stanowisko": np.random.choice(
        ["Data Analyst", "data analyst", "Python Dev", "AI Engineer", "Data Engineer", None],
        size=n,
        p=[0.25, 0.05, 0.30, 0.15, 0.20, 0.05]
    ),
    "miasto": np.random.choice(
        ["Poznań", "Poznan", "Warszawa", "Wrocław", "Zdalnie", None],
        size=n,
        p=[0.25, 0.05, 0.25, 0.15, 0.25, 0.05]
    ),
    "doswiadczenie_lata": np.random.choice([0, 1, 2, 3, 4, 5, 7, np.nan], size=n),
    "stawka_pln": np.round(np.random.normal(loc=14000, scale=4500, size=n), -2)
}

df = pd.DataFrame(dane)

# Wprowadzenie wartości odstających (błędy wpisu lub skrajne przypadki) i braków
df.loc[5, "stawka_pln"] = 185000.0   # Błąd o jedno zero za dużo
df.loc[42, "stawka_pln"] = -4500.0   # Błędna wartość ujemna
df.loc[10:15, "stawka_pln"] = np.nan # Braki w wynagrodzeniu

# Dodanie 5 zduplikowanych wierszy
df = pd.concat([df, df.iloc[0:5]], ignore_index=True)

df.to_csv("oferty_it.csv", index=False)
print("Plik oferty_it.csv został wygenerowany!")
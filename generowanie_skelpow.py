import pandas as pd
import numpy as np

np.random.seed(101)

klienci = pd.DataFrame({
    "id_klienta": range(1, 51),
    "segment": np.random.choice(["Standard", "Premium", "VIP", "vip", "standard"], size=50),
    "miasto": np.random.choice(["Poznań", "Warszawa", "Kraków", "Gdańsk", None], size=50, p=[0.3, 0.3, 0.2, 0.1, 0.1])
})

n_zam = 300
zamowienia = pd.DataFrame({
    "id_zamowienia": range(5001, 5001 + n_zam),
    "id_klienta": np.random.choice(range(1, 55), size=n_zam), # celowo kilku klientów spoza tabeli klienci
    "data_zamowienia": pd.date_range(start="2026-01-01", periods=n_zam, freq="6h").astype(str),
    "kwota_pln": np.round(np.random.lognormal(mean=5.2, sigma=0.8, size=n_zam), 2),
    "status": np.random.choice(["Zrealizowane", "Anulowane", "Zwrot", "zrealizowane", None], size=n_zam, p=[0.6, 0.15, 0.1, 0.1, 0.05])
})

# Celowe błędy i duplikaty
zamowienia.loc[15:22, "kwota_pln"] = np.nan
zamowienia.loc[88, "kwota_pln"] = -120.0
zamowienia.loc[140, "kwota_pln"] = 0.0
zamowienia.loc[210, "kwota_pln"] = 49999.99
zamowienia = pd.concat([zamowienia, zamowienia.iloc[10:18]], ignore_index=True)

klienci.to_csv("klienci.csv", index=False)
zamowienia.to_csv("zamowienia.csv", index=False)
print("Pliki klienci.csv oraz zamowienia.csv gotowe!")

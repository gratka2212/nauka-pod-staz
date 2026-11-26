import pandas as pd
import numpy as np

klienci = pd.read_csv("klienci.csv")
zamowienia = pd.read_csv("zamowienia.csv")

# print(klienci["segment"].unique())
# klienci = klienci.replace(["vip", "standard"], ["VIP", "Standard"])
klienci.loc[klienci["segment"].str.strip().str.lower() == "vip", "segment"] = "VIP"
klienci.loc[klienci["segment"].str.strip().str.lower() == "standard", "segment"] = "Standard"
klienci.loc[klienci["segment"].str.strip().str.lower() == "premium", "segment"] = "Premium"
# print(klienci["segment"].unique())

klienci["miasto"] = klienci["miasto"].fillna("Brak danych")
klienci = klienci.drop_duplicates()


zamowienia = zamowienia.dropna(subset=["status", "kwota_pln"])
status_map = {
    "zrealizowane":"Zrealizowane",
    "anulowane":"Anulowane",
    "zwrot":"Zwrot"
}
zamowienia["status"] = zamowienia["status"].str.strip().str.lower().replace(status_map)
zamowienia = zamowienia.drop_duplicates()
zamowienia = zamowienia[zamowienia["status"] == "Zrealizowane"]
# print(zamowienia["status"].unique())

Q1, Q3 = np.percentile(zamowienia["kwota_pln"], [25, 75])
iqr = Q3-Q1

zamowienia = zamowienia[zamowienia["kwota_pln"] <= Q3 + 1.5 * iqr]
zamowienia["data_zamowienia"] = pd.to_datetime(zamowienia["data_zamowienia"])

polaczone = pd.merge(zamowienia, klienci, on="id_klienta", how="inner")

polaczone["miesiac"] = polaczone["data_zamowienia"].dt.month

print(polaczone.groupby("segment")["kwota_pln"].agg(
    laczny_przychod="sum",
    srednia_wartosc_koszyka="mean",
    mediana_wartocci_koszyka="median",
    liczba_zrealizowanych_zamowien="count"
))

print(polaczone.groupby("miesiac")["kwota_pln"].sum())

polaczone.to_csv("raport_czysty.csv")
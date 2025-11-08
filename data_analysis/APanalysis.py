import auxFunctions as aux
from config import load_aps
import matplotlib.pyplot as plt
import pandas as pd

apsDF = load_aps()

daily_clients_simple = apsDF.groupby(apsDF["timestamp"].dt.date)["client_count"].sum().reset_index()
daily_clients_simple.rename(columns={"client_count" : "total_clients"}, inplace=True)
daily_clients = apsDF.groupby([apsDF["timestamp"].dt.date, "name"])["client_count"].sum().reset_index()
daily_clients.rename(columns={"client_count" : "clientsPerAp"}, inplace=True)
percentatge = pd.merge(daily_clients_simple, daily_clients, on = "timestamp")
print(daily_clients.nlargest(10, "clientsPerAp"))
percentatge["percentatge"] = (percentatge["clientsPerAp"] / percentatge["total_clients"]) * 100
percentatge["edifici"] = (percentatge["name"].str.split("-").str[1].str[:-2])
percentatge_per_edifici = percentatge.groupby([percentatge["edifici"], "timestamp"])["percentatge"].sum().reset_index()
print(percentatge_per_edifici)
plt.figure(figsize=(12, 6))
plt.bar(daily_clients_simple["timestamp"], daily_clients_simple["total_clients"])
plt.show()

pivot = percentatge_per_edifici.pivot(index="timestamp", columns = "edifici", values="percentatge")
pivot.plot(kind = "bar", stacked = True, figsize=(12,6))
plt.show()

unique_names = percentatge["edifici"].drop_duplicates().tolist()
print(unique_names)

facus = ["CIEN", "ETSE", "CIEN1", "CCOM", "CEDU", "MED", "VET", "DRET", "ESCDOC", "LLET1", "ECON", "LLET", "POL", "FTI"]
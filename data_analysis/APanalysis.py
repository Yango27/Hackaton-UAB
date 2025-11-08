import auxFunctions as aux
apsDF = aux.load_aps(r"anonymized_data\aps")
clientsDF = aux.load_clients(r"anonymized_data\clients")
aux.print_dataset_summary(apsDF)
aux.print_dataset_summary(clientsDF)
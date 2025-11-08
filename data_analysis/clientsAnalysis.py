import auxFunctions as aux
clientsDF = aux.load_clients(r"anonymized_data\clients")
aux.print_dataset_summary(clientsDF)
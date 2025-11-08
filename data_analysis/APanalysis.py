import auxFunctions as aux
from config import load_aps

apsDF = load_aps()
aux.print_dataset_summary(apsDF)

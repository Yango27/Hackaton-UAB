# data_analysis/config.py
from pathlib import Path
import auxFunctions as aux

# Carpeta raíz del proyecto
ROOT_DIR = Path(__file__).resolve().parent.parent

# Rutas de datos
APS_PATH = ROOT_DIR / "anonymized_data" / "aps"
CLIENTS_PATH = ROOT_DIR / "anonymized_data" / "clients"

# Funciones de carga
def load_aps(max_files=None, verbose=True):
    return aux.load_aps(APS_PATH, max_files=max_files, verbose=verbose)

def load_clients(max_files=None, verbose=True):
    return aux.load_clients(CLIENTS_PATH, max_files=max_files, verbose=verbose)
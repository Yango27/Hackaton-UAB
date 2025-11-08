import pandas as pd
import auxFunctions as aux

directDATA = "C:\Users\davad\Documents\UAB\HACKATHON\Hackaton-UAB\data_analysis\DATA"
directCLIENTS =  "C:\Users\davad\Documents\UAB\HACKATHON\Hackaton-UAB\data_analysis\DATA\client-info-2025-04-09T11_47_24+02_00-10487-ANON.json"
directAPS = "data_analysis/DATA/AP-info-v2-2025-06-13T14_45_01+02_00-ANON.json"

regAPS = aux.load_json_file(directAPS)
print(regAPS)

multiples = aux.load_multiple_files(directDATA)

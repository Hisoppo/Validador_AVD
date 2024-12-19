import os
import pandas as pd
import json

def load_data(avd_path, nfe_path, json_path):
    avd_data = pd.read_excel(avd_path)
    nfe_data = pd.read_excel(nfe_path)
    with open(json_path, 'r') as file:
        json_data = json.load(file)
        

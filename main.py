import os
import pandas as pd

import json
from def_load_data import load_data
from def_value_validation import verificar_valores, verificar_xmls_invalidos, verificar_somatorio, verificar_transmissoras_nao_presentes

def main():
    avd_path = input("Qual é o caminho do arquivo AVD? ")
    nfe_path = input("Qual é o caminho do arquivo NFE? ")
    json_path = input("Qual é o caminho do arquivo JSON? ")
    
    lote = input("Qual é o lote (lote1, lote2, lote3)? ")

    avd_data, nfe_data, transmissoras_data = load_data(avd_path, nfe_path, json_path)
    
    resultado_validacao = verificar_valores(avd_data, nfe_data, lote)
    print(resultado_validacao)
    
    xmls_a_remover = verificar_xmls_invalidos(nfe_data)
    print(xmls_a_remover)
    
    verificar_somatorio(nfe_data, avd_data, transmissoras_data)
    
    transmissoras_nao_presentes = verificar_transmissoras_nao_presentes(avd_data, nfe_data)
    print(transmissoras_nao_presentes)

if __name__ == "__main__":
    main()
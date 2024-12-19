import os
import pandas as pd
import json


def verificar_valores(avd_data, nfe_data, lote):
    
    if lote == "lote1":
        check_column = 'Check 1'
    elif lote == "lote2":
        check_column = 'Check 2'
    elif lote == "lote3":
        check_column = 'Check 3'
    else:
        return "Lote não inválido"

    avd_lote = avd_data[avd_data[check_column] == "OK"]
    avd_total = avd_lote['Valor'].sum()
    nfe_total = nfe_data['Valor da NF'].sum()

    if avd_total == nfe_total:
        return "LOTE LIBERADO PARA ENVIO"
    else:
        return f"Valores faltando para fechar: {nfe_total - avd_total}"
    

    
def verificar_xmls_invalidos(nfe_data):
    destinatarios_validos = [
        "VLI MULTIMODAL", "VLI MULTIMODAL S A", "VLI MULTIMODAL S.A.", 
        "VLI MULTIMODAL S.A. VLI MULTIMODAL", "VLI MULTIMODAL SA"
    ]
    xmls_a_remover = nfe_data[
        ~nfe_data['Destinatário'].isin(destinatarios_validos)
    ]['Arquivo']
    
    if not xmls_a_remover.empty:
        return f"Remova esses arquivos: {', '.join(xmls_a_remover)}"
    return ""


def verificar_somatorio(nfe_data, avd_data, transmissoras_data):
    for index, row in nfe_data.iterrows():
        if row['Emitente'] in transmissoras_data:
            transmissoras = transmissoras_data[row['Emitente']]
            avd_sub = avd_data[avd_data['Transmissora'].isin(transmissoras)]
            if abs(avd_sub['Valor'].sum() - row['Valor da NF']) < 1e-2:
                print(f"{row['Arquivo']}: Nota é o somatório dos valores das transmissoras: {', '.join(transmissoras)}")


def verificar_transmissoras_nao_presentes(avd_data, nfe_data):
    nfe_emitentes = nfe_data['Emitente'].unique()
    avd_nao_presentes = avd_data[(avd_data['Check']== 'OK') & (~avd_data['Transmissora'].isin(nfe_emitentes))]['Transmissora']

    if not avd_nao_presentes.empty:
        return f"Estas transmissoras estão marcadas como OK, mas não estão presentes na planilha de NFs: {', '.join(avd_nao_presentes)}"
    return ""
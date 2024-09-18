import time
import pyautogui
import pandas as pd
sample = pd.read_csv("SAMPLE.csv")

def sampleData(noraybanks):
    for linha in sample.index: 
        if not pd.isnull(sample.loc[linha, "DATA"]):
            DATA = sample.loc[linha, "DATA"]
            noraybanks.locator('#TxtFechaEntrada').click()
            noraybanks.fill('#TxtFechaEntrada', DATA)
            noraybanks.locator('#txtFechaObt').click()
            noraybanks.fill('#txtFechaObt', DATA)
        time.sleep(2)
        pyautogui.click(x=985, y=478)
        time.sleep(10)
        noraybanks.wait_for_selector('#TxtCodMuestra')
        codbarras = noraybanks.query_selector('#TxtCodMuestra').input_value() #COPIAR COD DE AMOSTRA
        time.sleep(2)
        noraybanks.wait_for_selector('#txtMicronic')
        noraybanks.locator('#txtMicronic').click()
        noraybanks.query_selector('#txtMicronic').fill(codbarras) #ESCREVER COD DE BARRAS
        time.sleep(1)
        noraybanks.wait_for_selector('#DDListEstadoMuetra')
        noraybanks.locator('#DDListEstadoMuetra"]').select_option('1') #STATUS AMOSTRA
        CASO = str(sample.loc[linha, "CASO"])
        noraybanks.wait_for_selector('#TxtCodEntrada')
        noraybanks.locator('#TxtCodEntrada"]').click()
        noraybanks.fill('#TxtCodEntrada"]', CASO) #COD DE ENTRADA
        noraybanks.wait_for_selector('#TxtVolumen')
        noraybanks.locator('#TxtVolumen"]').click()
        VOLUME = str(float(sample.loc[linha, "VOLUME"])).replace('.', ',')
        noraybanks.fill('#TxtVolumen', VOLUME) #VOLUME
        time.sleep(1)
        noraybanks.locator('#DDListResponsable').select_option('2')
        time.sleep(1)
        pyautogui.scroll(-500)
        time.sleep(5)
        if not pd.isnull(sample.loc[linha, "OBS"]):
            noraybanks.locator('#TxtObs1').click()
            OBS = str(sample.loc[linha, "OBS"])
            noraybanks.fill('#TxtObs1', OBS)
            noraybanks.locator('#btnSave_jqbtn').click() #SALVAR
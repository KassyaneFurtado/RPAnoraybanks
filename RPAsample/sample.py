import time
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import pandas as pd
import pyautogui
load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
sitenoraybanks = os.getenv('NORAYBANKS')
sample = pd.read_csv('SAMPLE.csv')
positions = pd.read_csv('POSITIONS.csv')
print(sample)
print(positions)

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, args=['--ignore-certificate-errors'])
    noraybanks = navegador.new_page()
    noraybanks.goto(sitenoraybanks)
    noraybanks.wait_for_selector('//*[@id="nbCtrlLoginNew1_LoginUser_UserName"]')
    time.sleep(5)
    noraybanks.fill('//*[@id="nbCtrlLoginNew1_LoginUser_UserName"]',login) #LOGIN
    noraybanks.wait_for_selector('//*[@id="nbCtrlLoginNew1_LoginUser_Password"]')
    noraybanks.fill('//*[@id="nbCtrlLoginNew1_LoginUser_Password"]', password) #SENHA
    noraybanks.locator('//*[@id="nbCtrlLoginNew1_LoginUser_LoginButton_jqbtn"]').click()
    time.sleep(2)
    try:
        for linha in sample.index:
            noraybanks.wait_for_selector('//*[@id="wrapper-250"]/ul/li[1]/a')
            noraybanks.locator('//*[@id="wrapper-250"]/ul/li[1]/a').click() #CASOS 
            noraybanks.wait_for_selector('//*[@id="wrapper-250"]/ul/li[1]/ul/li[3]/a/span')
            noraybanks.locator('//*[@id="wrapper-250"]/ul/li[1]/ul/li[3]/a/span').click() #CONSULTA
            time.sleep(5)
            noraybanks.locator('//*[@id="nbConsulta1_NbCtrlBiobancoNodo1_ddListBiobanco"]').select_option('1')
            time.sleep(5)
        
            if not positions.empty:
                number = sample.loc[linha, 'TIPOC']
                position = positions[positions['TIPO'] == number]
                print(f"Processando número: {number}")
                print(position)
            # Obter o XPath do locador
                xpath = position.iloc[0]['LOCADOR']
            # Selecionar a opção no menu suspenso
                print(f"XPath selecionado: {xpath}")
                print(f"Selecionando a opção: {number} com XPath: {xpath}")
                time.sleep(3)
                noraybanks.wait_for_event
                noraybanks.query_selector('#nbConsulta1_NbCtrlBiobancoNodo1_ddListNodo').select_option(str(xpath))
                time.sleep(2)

            if not pd.isnull(sample.loc[linha, "PRONTUARIO"]):
                noraybanks.wait_for_selector('//*[@id="nbConsulta1_TxtCodigoUnico"]')
                noraybanks.locator('//*[@id="nbConsulta1_TxtCodigoUnico"]').click()
                prontuario = str(int(sample.loc[linha, "PRONTUARIO"]))
                noraybanks.fill('//*[@id="nbConsulta1_TxtCodigoUnico"]', prontuario)

            noraybanks.locator('//*[@id="btnFiltro_jqbtn"]').click()
            time.sleep(2)
            pyautogui.scroll(-200)
            noraybanks.wait_for_selector('//*[@id="GridList_ctl02_ImgbtnMod"]')
            noraybanks.locator('//*[@id="GridList_ctl02_ImgbtnMod"]').click()
            time.sleep(2)
            noraybanks.wait_for_selector('//*[@id="GridDonacion_ctl02_ImgbtnMod"]')
            noraybanks.locator('//*[@id="GridDonacion_ctl02_ImgbtnMod"]').click()
            time.sleep(5)
            noraybanks.locator('//*[@id="BtnMuestras_jqbtn"]').click()
            noraybanks.locator('//*[@id="DDListTipoM"]').click()
            if not positions.empty:
                number = sample.loc[linha, 'TIPOA']
                position = positions[positions['TIPO'] == number]
                print(f"Processando número: {number}")
                print(position)
            # Obter o XPath do locador
                xpath = position.iloc[0]['LOCADOR']
            # Selecionar a opção no menu suspenso
                print(f"XPath selecionado: {xpath}")
                print(f"Selecionando a opção: {number} com XPath: {xpath}")
                time.sleep(3)
                noraybanks.wait_for_event
                noraybanks.query_selector('#DDListTipoM').select_option(str(xpath))
            else:
                print(f"Posição não encontrada para o número {number}")
                time.sleep(5) 
            noraybanks.wait_for_selector('//*[@id="BtnNewMuestra_jqbtn"]')        
            noraybanks.locator('//*[@id="BtnNewMuestra_jqbtn"]').click() #ADICIONAR AMOSTRA
            time.sleep(10)
            if not pd.isnull(sample.loc[linha, "DATA"]):
                DATA = sample.loc[linha, "DATA"]
                noraybanks.wait_for_selector('//*[@id="TxtFechaEntrada"]')
                noraybanks.locator('//*[@id="TxtFechaEntrada"]').focus() #DATA DE ENTRADA
                noraybanks.fill('//*[@id="TxtFechaEntrada"]', DATA) #DATA DE ENTRADA
                time.sleep(2)
                pyautogui.click(x=985, y=478)
                time.sleep(5)
                noraybanks.wait_for_selector('//*[@id="txtFechaObt"]')
                noraybanks.locator('//*[@id="txtFechaObt"]')                             
                noraybanks.locator('//*[@id="txtFechaObt"]').focus() #DATA DA AMOSTRA
                noraybanks.locator('//*[@id="txtFechaObt"]').fill(DATA) #DATA DA AMOSTRA
            time.sleep(2)
            pyautogui.click(x=985, y=478)
            time.sleep(2)
            noraybanks.wait_for_selector('//*[@id="TxtCodMuestra"]')
            codbarras = noraybanks.query_selector('//*[@id="TxtCodMuestra"]').input_value() #COPIAR COD DE AMOSTRA
            time.sleep(2)
            noraybanks.wait_for_selector('//*[@id="txtMicronic"]')
            noraybanks.locator('//*[@id="txtMicronic"]').click()
            noraybanks.query_selector('//*[@id="txtMicronic"]').fill(codbarras) #ESCREVER COD DE BARRAS
            time.sleep(1)
            noraybanks.wait_for_selector('//*[@id="DDListEstadoMuetra"]')
            noraybanks.locator('//*[@id="DDListEstadoMuetra"]').select_option('1') #STATUS AMOSTRA
            CASO = str(sample.loc[linha, "CASO"])
            noraybanks.wait_for_selector('//*[@id="TxtCodEntrada"]')
            noraybanks.locator('//*[@id="TxtCodEntrada"]').click()
            noraybanks.fill('//*[@id="TxtCodEntrada"]', CASO) #COD DE ENTRADA
            noraybanks.wait_for_selector('//*[@id="TxtVolumen"]')
            noraybanks.locator('//*[@id="TxtVolumen"]').click()
            VOLUME = str(float(sample.loc[linha, "VOLUME"])).replace('.', ',')
            noraybanks.fill('//*[@id="TxtVolumen"]', VOLUME) #VOLUME
            time.sleep(1)
            noraybanks.locator('#DDListResponsable').select_option('2')
            time.sleep(1)
            pyautogui.scroll(-500)
            time.sleep(5)
            if not pd.isnull(sample.loc[linha, "OBS"]):
                noraybanks.locator('//*[@id="TxtObs1"]').click()
                OBS = str(int(sample.loc[linha, "OBS"]))
                noraybanks.fill('//*[@id="TxtObs1"]', OBS)
            noraybanks.locator('//*[@id="btnSave_jqbtn"]/span[1]').click() #SALVAR
            time.sleep(5)
            noraybanks.wait_for_selector('//*[@id="NbctrlPopup1_ButtonOk_jqbtn"]')
            noraybanks.locator('//*[@id="NbctrlPopup1_ButtonOk_jqbtn"]').click()
            time.sleep(7)
            pyautogui.scroll(2000)
            noraybanks.wait_for_selector('//*[@id="wrapper-250"]/ul/li[1]/a')

    finally:
        noraybanks.query_selector('#Header1_NbCurrentProfile1_ButtonLogOut_jqbtn').click()
        time.sleep(20)
        navegador.close()


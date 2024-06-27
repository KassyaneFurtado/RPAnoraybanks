import time
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import pandas as pd
import pyautogui

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
sample = pd.read_csv("SAMPLE.csv")
positions = pd.read_csv('POSITIONS.csv')
print(sample)
print(positions)

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False, args=['--ignore-certificate-errors'])
    noraybanks = navegador.new_page()
    noraybanks.goto("https://noraybanks.mariopenna.org.br/InternalLoginNew.aspx")
    noraybanks.wait_for_selector('//*[@id="nbCtrlLoginNew1_LoginUser_UserName"]')
    time.sleep(5)
    noraybanks.fill('//*[@id="nbCtrlLoginNew1_LoginUser_UserName"]',login) #LOGIN
    noraybanks.wait_for_selector('//*[@id="nbCtrlLoginNew1_LoginUser_Password"]')
    noraybanks.fill('//*[@id="nbCtrlLoginNew1_LoginUser_Password"]', password ) #SENHA
    noraybanks.locator('//*[@id="nbCtrlLoginNew1_LoginUser_LoginButton_jqbtn"]').click()
    
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
            time.sleep(5)
            print(f"Selecionando a opção: {number} com XPath: {xpath}")
            time.sleep(5)
            noraybanks.locator('//*[@id="nbConsulta1_NbCtrlBiobancoNodo1_ddListNodo"]').click()
            noraybanks.locator('//*[@id="nbConsulta1_NbCtrlBiobancoNodo1_ddListNodo"]').select_option(value=str(number))  # Supondo que a opção seja um valor string
        else:
            print(f"Posição não encontrada para o número {number}")
            time.sleep(2)

        if not pd.isnull(sample.loc[linha, "PRONTUARIO"]):
            noraybanks.wait_for_selector('//*[@id="nbConsulta1_TxtCodigoUnico"]')
            noraybanks.locator('//*[@id="nbConsulta1_TxtCodigoUnico"]').click()
            prontuario = str(int(sample.loc[linha, "PRONTUARIO"]))
            noraybanks.fill('//*[@id="nbConsulta1_TxtCodigoUnico"]', prontuario)

        noraybanks.locator('//*[@id="btnFiltro_jqbtn"]').click()
        noraybanks.wait_for_selector('//*[@id="GridList_ctl02_ImgbtnMod"]')
        noraybanks.locator('//*[@id="GridList_ctl02_ImgbtnMod"]').click()
        noraybanks.wait_for_selector('//*[@id="GridDonacion_ctl02_ImgbtnMod"]')
        noraybanks.locator('//*[@id="GridDonacion_ctl02_ImgbtnMod"]').click()
        noraybanks.locator('//*[@id="BtnMuestras_jqbtn"]').click()
        noraybanks.locator('//*[@id="DDListTipoM"]').click()
        number = sample.loc[linha, 'TIPOA']
        position = positions[positions['TIPO'] == number]
        if not positions.empty:
            number = sample.loc[linha, 'TIPOC']
            position = positions[positions['TIPO'] == number]
            print(f"Processando número: {number}")
            print(position)
        # Obter o XPath do locador
            xpath = position.iloc[0]['LOCADOR']
        # Selecionar a opção no menu suspenso
            print(f"XPath selecionado: {xpath}")
            time.sleep(10)
            print(f"Selecionando a opção: {number} com XPath: {xpath}")
            time.sleep(10)
            noraybanks.locator('//*[@id="DDListTipoM"]').click()
            noraybanks.locator('//*[@id="DDListTipoM"]').select_option(value=str(number))  # Supondo que a opção seja um valor string
        else:
            print(f"Posição não encontrada para o número {number}")
            time.sleep(20)
        noraybanks.wait_for_selector('//*[@id="BtnNewMuestra_jqbtn"]')        
        noraybanks.locator('//*[@id="BtnNewMuestra_jqbtn"]').click() #ADICIONAR AMOSTRA
        time.sleep(5)
        noraybanks.wait_for_selector('//*[@id="TxtCodMuestra"]')
        codbarras = noraybanks.query_selector('//*[@id="TxtCodMuestra"]').input_value() #COPIAR COD DE AMOSTRA
        time.sleep(1)
        noraybanks.wait_for_selector('//*[@id="TxtCodEntrada"]')
        noraybanks.locator('//*[@id="TxtCodEntrada"]').click()
        noraybanks.query_selector('//*[@id="TxtCodEntrada"]').fill(codbarras) #ESCREVER COD DE BARRAS
        time.sleep(1)
        noraybanks.wait_for_selector('//*[@id="TxtFechaEntrada"]')
        noraybanks.locator('//*[@id="TxtFechaEntrada"]').click()
        DATA = str(int(sample.loc[linha, "DATA"])) 
        noraybanks.fill('//*[@id="TxtFechaEntrada"]', DATA) #DATA DE ENTRADA
        time.sleep(1)
        noraybanks.wait_for_selector('//*[@id="TxtVolumen"]')
        noraybanks.locator('//*[@id="TxtVolumen"]').click()
        VOLUME = str(int(sample.loc[linha, "VOLUME"]))
        noraybanks.fill('//*[@id="TxtVolumen"]', VOLUME) #VOLUME
        time.sleep(1)
        noraybanks.wait_for_selector('//*[@id="txtFechaObt"]')
        noraybanks.locator('//*[@id="txtFechaObt"]')                             
        noraybanks.fill('//*[@id="txtFechaObt"]', DATA) #DATA DA AMOSTRA
        time.sleep(10)
        noraybanks.wait_for_selector('//*[@id="DDListEstadoMuetra"]')
        noraybanks.locator('//*[@id="DDListEstadoMuetra"]').select_option('2') #STATUS AMOSTRA
        time.sleep(1)
        CASO = str(int(sample.loc[linha, "CASO"]))
        noraybanks.wait_for_selector('//*[@id="TxtCodEntrada"]')
        noraybanks.locator('//*[@id="TxtCodEntrada"]').click()
        noraybanks.fill('//*[@id="TxtCodEntrada"]', CASO) #COD DE ENTRADA
        time.sleep(1)
        noraybanks.locator('//*[@id="DDListResponsable"]').click()
        noraybanks.locator('//*[@id="DDListResponsable"]/option[3]').click()
        time.sleep(1)
        if not pd.isnull(sample.loc[linha, "OBS"]):
            noraybanks.locator('//*[@id="TxtObs1"]').click()
            OBS = str(int(sample.loc[linha, "OBS"]))
            noraybanks.fill('//*[@id="TxtObs1"]', OBS)
        noraybanks.locator('//*[@id="btnSave_jqbtn"]/span[1]') #SALVAR
        noraybanks.locator('//*[@id="btnImprimirEtiquetasTL_jqbtn"]').click() #IMPRESSÃO DIRETA
        noraybanks.locator('//*[@id="nbctrlImprimirEtiquetas1_ddListLabelDesign"] ').click() #ESCOLHER DESING DA ETIQUETA
        #noraybanks.locator('')
        time.sleep(5)
        #pyautogui.click(x=412, y=653)
        noraybanks.locator('//*[@id="Header1_NbCurrentProfile1_ButtonLogOut_jqbtn"]').click()
        navegador.close()





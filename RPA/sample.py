import time
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import pandas as pd
import pyautogui
import utils
import navegador
from formulario import preencheCampo
import planilha
load_dotenv()

sample = planilha.carregaAmostras()
positions = planilha.carregaPosicoes()

#ABRINDO O NAVEGADOR 
with sync_playwright() as p:
    noraybanks = utils.criaNavegador(p)

    navegador.fazLogin(noraybanks)

    try:
        for linha in sample.index:
            noraybanks.wait_for_selector('#wrapper-250') 
            noraybanks.locator('#wrapper-250').click() #CASOS 
            noraybanks.wait_for_selector('#wrapper-250')
            noraybanks.locator('#wrapper-250').click() #CONSULTA
            time.sleep(5)
            noraybanks.locator('#nbConsulta1_NbCtrlBiobancoNodo1_ddListBiobanco').select_option('1')
            time.sleep(5)
        
            if not positions.empty:
                number = planilha.pegaDado(sample, 'TIPOC', linha)
                position = positions[positions['TIPO'] == number]
                print(f"Processando número: {number}")
                print(position)
            # Obter o XPath do locador
                xpath = position.iloc[0]['LOCADOR']
            # Selecionar a opção no menu suspenso
                print(f"XPath selecionado: {xpath}")
                print(f"Selecionando a opção: {number} com XPat
                      h: {xpath}")
                time.sleep(3)
                noraybanks.wait_for_event
                noraybanks.query_selector('#nbConsulta1_NbCtrlBiobancoNodo1_ddListNodo').select_option(str(xpath))
                time.sleep(2)

            if not pd.isnull(sample.loc[linha, "PRONTUARIO"]):
                noraybanks.wait_for_selector('#nbConsulta1_TxtCodigoUnico')
                noraybanks.locator('#nbConsulta1_TxtCodigoUnico').click()
                prontuario = str(int(sample.loc[linha, "PRONTUARIO"]))
                noraybanks.fill('#nbConsulta1_TxtCodigoUnico', prontuario)

            noraybanks.locator('#btnFiltro_jqbtn').click()
            time.sleep(2)
            pyautogui.scroll(-200)
            noraybanks.wait_for_selector('#GridList_ctl02_ImgbtnMod')
            noraybanks.locator('#GridList_ctl02_ImgbtnMod').click()
            time.sleep(2)
            noraybanks.wait_for_selector('#GridDonacion_ctl02_ImgbtnMod')
            noraybanks.locator('#GridDonacion_ctl02_ImgbtnMod').click()
            time.sleep(5)
            noraybanks.locator('#BtnMuestras_jqbtn').click()
            noraybanks.locator('#DDListTipoM').click()
            if not positions.empty:
                number = int(sample.loc[linha, 'TIPOA'])
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
            noraybanks.wait_for_selector('#BtnNewMuestra_jqbtn')        
            noraybanks.locator('#BtnNewMuestra_jqbtn').click() #ADICIONAR AMOSTRA
            time.sleep(5)
            if not pd.isnull(sample.loc[linha, "DATA"]):
                DATA = sample.loc[linha, "DATA"]

                preencheCampo(noraybanks, '#TxtFechaEntrada', DATA)
                preencheCampo(noraybanks, '#txtFechaObt', DATA)

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
            time.sleep(5)
            noraybanks.wait_for_selector('#NbctrlPopup1_ButtonOk_jqbtn')
            noraybanks.locator('#NbctrlPopup1_ButtonOk_jqbtn').click()
            time.sleep(7)
            pyautogui.scroll(2000)
            noraybanks.wait_for_selector('#wrapper-250')

    finally:
        noraybanks.query_selector('#Header1_NbCurrentProfile1_ButtonLogOut_jqbtn').click()
        time.sleep(20)
        navegador.close()


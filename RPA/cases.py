import pyautogui
import time
import pandas
import pandas as pd
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import utils
import navegador
from formulario import preencheCampo
import planilha

load_dotenv()
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')
sample = planilha.carregaAmostras()
positions = planilha.carregaPosicoes()

#ABRINDO O NAVEGADOR 
with sync_playwright() as p:
    noraybanks = utils.criaNavegador(p)

    navegador.fazLogin(noraybanks)

    try:
        for linha in sample.index:
            noraybanks.wait_for_selector('#wrapper-250')
            noraybanks.locator('#wrapper-250').click()  
            noraybanks.wait_for_selector('#wrapper-250')
            noraybanks.locator('#wrapper-250').click() 
            time.sleep(5)
            noraybanks.locator('#NbCtrlBiobancoNodo1_ddListBiobanco').select_option('1')
            time.sleep(5)
            noraybanks.waint_for_selector('#NbCtrlBiobancoNodo1_ddListNodo')
            noraybanks.locator('#NbCtrlBiobancoNodo1_ddListNodo').click()
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
            #DIGITAR PRONTUÁRIO
            prontuario = planilha.carregaAmostras.loc[linha,"PRONTUARIO"]
            noraybanks.waint_for_selector('#TxtCodDonante')
            noraybanks.locator('#TxtCodDonante').click()
            prontuario = str(int(sample.loc[linha, "PRONTUARIO"]))
            noraybanks.fill('#TxtCodDonante', prontuario)
            #SELECIONAR TIPO DE PACIENTE
            noraybanks.locator('#DDListEspecie').select_option('2') #ADD TIPO DE PACIENTE NA PLANILHA DE CASOS PACIENTE -2 CONTROLE -1
            #SELECIONAR CAMPO DE DADOS PESSOAIS
            noraybanks.locator('#checkBoxDatosFiliacion').click()
            #SALVAR DADOS
            noraybanks.locator('#BtnAceptar_jqbtn').click()
            time.sleep(5)
            #SELECIONAR CENTRO DE ESTUDO
            noraybanks.locator('#DDListCentro').click()
            noraybanks.locator('#DDListCentro').select_option('2')
            #PREENCHER DADOS PESSOAIS DO DOADOR
            noraybanks.locator('#txtNombre').click()
            noraybanks.fill('#txtNombre', 'NOME1')
            noraybanks.locator('##txtApe1').click()
            noraybanks.fill('##txtApe1', 'NOME2')
            noraybanks.locator('#txtApe2').click()
            noraybanks.fill('#txtApe2', 'NOME3')
            noraybanks.locator('#TxtFechaNac').click()
            noraybanks.fill('#TxtFechaNac', 'DATANASCIMENTO')
            noraybanks.locator('#TxtHistoria').click()
            noraybanks.fill('#TxtHistoria', prontuario)
            noraybanks.locator('#DDSexo').click()
            noraybanks.locator('#DDSexo').select_option(str(xpath)) #ADD SEXO MASCULINO E FEMINO NA PLANILHA DE CASOS
            #CADASTRAR DOAÇÃO
            noraybanks.locator('ImgNewDon').click()
            noraybanks.locator('#NbctrlPopup1_ButtonYes_jqbtn').click()
            noraybanks.locator('#NbctrlPopup1_ButtonOk_jqbtn').click()
            #DADOS DOAÇÃO
            noraybanks.locator('#txtReceptionDate').click()
            noraybanks.fill('#txtReceptionDate', 'DATACOLETA')
            noraybanks.locator('#DdListConsentMuestras').select_option('1')
            noraybanks.locator('#DDListTipoCons').click()
            noraybanks.locator('#DDListTipoCons').click().select_option(str(xpath)) #ADD TIPO DE TCLE NA PLANILHA BIOBANCO 1 PROJETO 2
            noraybanks.locator('#DdListConsentFirmado').click()
            noraybanks.locator('#DdListConsentFirmado').select_option('1')
            noraybanks.locator('#TxtFechaConsentFirma').click()
            noraybanks.fill('#TxtFechaConsentFirma','DATACOLETA')
            noraybanks.locator('#BtnInsert_jqbtn').click()

            #SE HOUVER AMOSTRAS COM O MESMO PRONTUÁRIO DO CASO NA PLANILHA SAMPLE PUXAR AS FUNÇÕES DE LANÇAMENTO DE AMOSTRAS
     
     
    finally:
        noraybanks.query_selector('#Header1_NbCurrentProfile1_ButtonLogOut_jqbtn').click()
        time.sleep(20)
        navegador.close()

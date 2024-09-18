import time
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os
import pandas as pd
import pyautogui
import utils
import navegador
from select_study_group import selectStudyGroup
from select_case_type import selectCaseType
from search_record import searchRecord
from select_sample_type import selectSampleType
from data_sample import sampleData
from select_case import caseSelect
import load_data
load_dotenv()

sample = load_data.carregaAmostras()
positions = load_data.carregaPosicoes()

#ABRINDO O NAVEGADOR 
with sync_playwright() as p:
    noraybanks = utils.criaNavegador(p)

    navegador.fazLogin(noraybanks)

    try:
        for linha in sample.index:
            selectStudyGroup(noraybanks)
            selectCaseType(noraybanks, sample, positions, linha)
            searchRecord(noraybanks, sample, linha)
            selectSampleType(noraybanks, sample, positions, linha)
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


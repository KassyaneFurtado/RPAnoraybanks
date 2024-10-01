import time

from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

import pyautogui

import navegador
import utils
import load_data

from select_study_group import selectStudyGroup
from select_case_type import selectCaseType
from search_record import searchRecord
from select_sample_type import selectSampleType

load_dotenv()

samples = load_data.loadSamples()
positions = load_data.loadPositions()

#ABRINDO O NAVEGADOR 
with sync_playwright() as p:
    noraybanks = utils.createBrowser(p)

    navegador.login(noraybanks)

    try:
        for line in samples.index:
            selectStudyGroup(noraybanks)
            selectCaseType(noraybanks, samples, positions, line)
            searchRecord(noraybanks, samples, line)
            selectSampleType(noraybanks, samples, positions, line)
            time.sleep(5)
            noraybanks.wait_for_selector('#NbctrlPopup1_ButtonOk_jqbtn')
            noraybanks.locator('#NbctrlPopup1_ButtonOk_jqbtn').click()
            time.sleep(7)
            pyautogui.scroll(2000)
            noraybanks.wait_for_selector('#wrapper-250')

    except Exception as e:
        print(e)

    finally:
        noraybanks.query_selector('#Header1_NbCurrentProfile1_ButtonLogOut_jqbtn').click()
        time.sleep(20)
        navegador.close()


import time
import pyautogui

def caseSelect(noraybanks):
    # Função de seleção de amostra
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
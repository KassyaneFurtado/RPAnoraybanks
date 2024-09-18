import time

def selectStudyGroup(noraybanks):
    # Selecionar grupo de estudo
    noraybanks.wait_for_selector('//*[@id="wrapper-250"]/ul/li[1]/a') #'#wrapper-250') 
    noraybanks.locator('//*[@id="wrapper-250"]/ul/li[1]/a').click()  # CASOS 
    noraybanks.wait_for_selector('//*[@id="wrapper-250"]/ul/li[1]/ul/li[3]/a')
    noraybanks.locator('//*[@id="wrapper-250"]/ul/li[1]/ul/li[3]/a').click()  # CONSULTA
    time.sleep(5)
    noraybanks.locator('#nbConsulta1_NbCtrlBiobancoNodo1_ddListBiobanco').select_option('1')
    time.sleep(5)

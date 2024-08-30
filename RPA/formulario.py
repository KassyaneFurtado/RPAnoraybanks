def preencheCampo(noraybanks, nomeCampo, valor):
    noraybanks.wait_for_selector(nomeCampo)
    noraybanks.locator(nomeCampo).focus() #DATA DE ENTRADA
    noraybanks.locator(nomeCampo).click()
    noraybanks.locator(nomeCampo).fill(valor)
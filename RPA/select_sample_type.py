import time

def selectSampleType(noraybanks, sample, positions, linha):
        
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
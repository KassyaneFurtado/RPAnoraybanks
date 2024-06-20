# O QUE O CÓDIGO DEVE FAZER:
#LANÇAR AS AMOSTRAS, PARA ISSO SÃO OS SEGUINTES PASSOS:
#PROCURAR PELO CASO
    #ONCOLOGIA
        # TIPO DE CASO
            #PRONTUÁRIO
#EDITAR CASO
#EDITAR DOAÇÃO
#AMOSTRAS
    #TIPO DE AMOSTRA:
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9
        # 10
        # 11
        # 12
            #QUANTIDADE DE AMOSTRA
            #STATUS DA AMOSTRA
            #DATA DA AMOSTRA
            #RESPONSÁVEL
            #CÓDIGO DE ENTRADA (CASO)
            #OBS
            #CÓDIGO DE BARRAS
            #SALVAR 
            #IMPRIMIR ETIQUETA
        # ANEXAR DOCUMENTOS (TECIDO)

import pyautogui
import time
import pandas as pd

time.sleep(5)
pyautogui.PAUSE = 2
pyautogui.click(x=99, y=157) #CLICAR EM CASOS
pyautogui.click(x=78, y=267) #CONSULTA DE CASOS
time.sleep(5)
pyautogui.click(x=501, y=285) #CLICAR EM GRUPO
pyautogui.click(x=505, y=324) #ONCOLOGIA
time.sleep(5)
pyautogui.click(x=1128, y=278) #CLICAR EM COLEÇÃO
sample = pd.read_csv('SAMPLE.csv')
positions = pd.read_csv('POSITIONS.csv')
print("SAMPLE.csv")
print("POSITIONS.csv")

# Verificar se as colunas 'X' e 'Y' existem na planilha POSITIONS.csv
if 'X' not in positions.columns or 'Y' not in positions.columns:
    raise KeyError("A coluna 'X' ou 'Y' não foi encontrada na planilha POSITIONS.csv")

# Iterar sobre os números na coluna 'TIPOC' da planilha SAMPLE.csv
for number in sample['TIPOC']:
    # Procurar o número na coluna 'TIPO' da planilha POSITIONS.csv
    position = positions[positions['TIPO'] == number]
    
    # Verificar se a posição foi encontrada
    if not position.empty:
        x = position['X'].values[0]
        y = position['Y'].values[0]
        
        # Realizar o clique na posição encontrada
        print(f"Clicando em: X = {x}, Y = {y}")
        pyautogui.click(x, y)
    else:
        print(f"Posição não encontrada para o número {number}")
time.sleep(5) #(retirar)
pyautogui.click(x=1491, y=372) #CLICAR EM PRONTUÁRIO (retirar)
pyautogui.write()
pyautogui.click(x=268, y=672) #CLICAR EM BUSCAR
time.sleep(10)
pyautogui.click(x=279, y=751) #CLICAR EM EDITAR CASO
pyautogui.scroll(-20000)
pyautogui.click(x=286, y=592) #EDITAR DOAÇÃO
time.sleep(10)
pyautogui(x=274, y=1000) #CLICAR EM AMOSTRAS
pyautogui.click(x=600, y=482)
#INCLUIR UM FUNÇÃO IF
# SE O TIPO DA AMOSTRAS FOR "1" ENTÃO CLICAR NA POSIÇÃO TAL
#PEGAR AS POSIÇÕES PARA ADIDIONAR NO ARQUIVO POSITIONS.csv
#TIPO DE AMOSTRA:
        # 1 Lavado Peritoneal
        # 2 Leucócitos
        # 3 Líquido Ascítico
        # 4 Líquido Ascítico Biorepositório
        # 5 Plasma Citrato
        # x=600, y=482 - 6 Plasma EDTA 
        # 7 Sangue Citrato
        # 8 Sangue EDTA
        # 9 Tecido Normal Congelado	
        # 10 Tecido Normal Parafina
        # 11 Tecido Tumoral Congelado
        # 12 Tecido Tumoral Parafina
time.sleep(5)
pyautogui.click(x=811, y=359) #CLICAR EM ADICIONAR AMOSTRAS
time.sleep(5)
pyautogui.click(x=460, y=538) #CLICAR EM DATA ENTRADA
pyautogui.write()
pyautogui.click(x=464, y=712) #ML
pyautogui.write()
pyautogui.click(x=460, y=837) #CLICAR EM DATA DA AMOSTRA
pyautogui.write()
time.sleep(5)
pyautogui.click(x=585, y=874) #CLICAR EM RESPONSÁVEL
pyautogui.click(x=597, y=926) #SELECIONA O RESPONSÁVEL
pyautogui.click(x=1545, y=731) #CLICAR EM STATUS DA AMOSTRA
pyautogui.click(x=1536, y=769) #SELECIONA STATUS DISPONÍVEL
pyautogui.click(x=1487, y=807) #CLICAR EM CÓDIGO DE ENTRADA
pyautogui.write()
#INCLUIR FUNÇÃO IF 
# SE O CAMPO NÃO ESTIVER VAZIO CLICAR E ESCREVER
pyautogui.click(x=493, y=910)
pyautogui.write()
pyautogui.scroll(-500)
pyautogui.click(x=559, y=953)
#IMPRIMIR ETIQUETAS
#ANEXAR DOCS A DEPENDER DO TIPO DE AMOSTRA





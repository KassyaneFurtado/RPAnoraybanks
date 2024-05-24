#ENTRAR NO NORAYBANKS
#FAZER LOGIN
#BUSCAR POR CASO
#ESCREVER CÓDIGO DE ENTRADA DE CADA AMOSTRA CADASTRADA NO CASO

import pyautogui
import pandas
import time

#OPCIONAL O RPA PODE FAZER LOGIN NO SISTEMA OU VOCÊ JÁ PODE DEIXAR NA PÁGINA
'''usuario = input("Insira seu usuário: ")
senha = input("Insira sua senha: ")
link = input("Insira o link do sistema: ")'''

pyautogui.PAUSE = 3 #SERVE PARA DEIXAR A AUTOMAÇÃO MAIS LENTA PARA VER O PROCESSO ACONTECER
'''pyautogui.press("win")
pyautogui.write ("microsoft edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep (5)
pyautogui.click(x=642, y=410)
pyautogui.write (usuario)
pyautogui.press("tab") 
pyautogui.write(senha)
pyautogui.press ("enter")'''
time.sleep (5)
# INICIO DAS TAREFAS
pyautogui.click(x=57, y=197) #clicar em amostras
pyautogui.click(x=110, y=226) #clicar em consulta
time.sleep(5)
#importar base de dados
tabela = pandas.read_csv("PCONB.csv")
print(tabela)
for linha in tabela.index:
    codigo = tabela.loc[linha,"CODAMOSTRANB"]
    pyautogui.click(x=985, y=508)#clicar para escrever o código da amostra
    time.sleep(2)
    pyautogui.write(tabela.loc[linha,"CODAMOSTRANB"]) 
    pyautogui.press("enter")
    time.sleep (2)
    pyautogui.scroll(-1000)
    pyautogui.click (x=278, y=450) #clicar para editar amostra
    time.sleep(8)
    pyautogui.scroll(-500)
    pyautogui.click(x=472, y=404) #clicar para escrever codigo de barras
    pyautogui.write(tabela.loc[linha,"CODAMOSTRANB"])
    pyautogui.click(x=482, y=497) #clicar para escrever codigo de entrada
    pyautogui.write(tabela.loc[linha,"PCO"])
    pyautogui.scroll(-500)
    pyautogui.click(x=429, y=622) #clicar para salvar
    time.sleep(5)
    pyautogui.click(x=662, y=450)
    time.sleep(10)
    pyautogui.scroll(1000)
    pyautogui.click(x=127, y=227)
    time.sleep(2)
    pyautogui.click(x=79, y=234)
    time.sleep(4)
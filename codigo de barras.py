#PASSO A PASSO DO PROJETO DE AUTOMAÇÃO DE ETIQUETAS NO NORAYBANKS
#ENTRAR NO NORAYBANKS
#FAZER LOGIN
#BUSCAR POR CASO
#ESCREVER CÓDIGO DE ENTRADA DE CADA AMOSTRA CADASTRADA NO CASO
#IMPRIMIR ETIQUETAS
#RODAR EM SEGUNDO PLANO

import pyautogui
import pandas

usuario = input("Insira seu usuário: ")
senha = input("Insira sua senha: ")
link = input("Insira o link do sistema: ")

pyautogui.PAUSE = 1
#SERVE PARA DEIXAR A AUTOMAÇÃO MAIS LENTA PARA VER O PROCESSO ACONTECER
pyautogui.press("win")
pyautogui.write ("microsoft edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
import time
time.sleep (5)
pyautogui.click(x=642, y=410)
pyautogui.write (usuario)
#pyautogui.click(x=934, y=445)
#pyautogui.click(x=660, y=444)
pyautogui.press("tab") 
pyautogui.write(senha)
pyautogui.press ("enter")
time.sleep (2) 
pyautogui.click(x=57, y=197) #clicar em amostras
pyautogui.click(x=110, y=226) #clicar em consulta
time.sleep(5)
#importar base de dados
tabela = pandas.read_csv("AMOSTRACONTROLEMAMA.csv")
print(tabela)
for linha in tabela.index:
    codigo = tabela.loc[linha,"CODAMOSTRANB"]
    pyautogui.click(x=918, y=501)#clicar para escrever o código da amostra
    time.sleep(2)
    pyautogui.write(tabela.loc[linha,"CODAMOSTRANB"]) 
    pyautogui.press("enter")
    time.sleep (2)
    pyautogui.scroll(-1000)
    pyautogui.click (x=278, y=456) #clicar para editar amostra
    time.sleep(8)
    pyautogui.scroll(-500)
    pyautogui.click(x=472, y=404) #clicar para escrever codigo de barras
    pyautogui.write(tabela.loc[linha,"CODAMOSTRANB"])
    pyautogui.scroll(-500)
    pyautogui.click(x=443, y=627) #clicar para salvar
    time.sleep(5)
    pyautogui.click(x=676, y=442)
    time.sleep(10)
    pyautogui.scroll(1000)
    pyautogui.click(x=127, y=227)
    time.sleep(2)
    pyautogui.click(x=79, y=234)
    time.sleep(4)
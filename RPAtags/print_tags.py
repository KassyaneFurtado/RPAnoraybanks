import pyautogui
import pandas
#OPCIONAL O RPA PODE FAZER LOGIN NO SISTEMA OU VOCÊ JÁ PODE DEIXAR NA PÁGINA
usuario = input("Insira seu usuário: ")
senha = input("Insira sua senha: ")
link = input("Insira o link do sistema: ")

pyautogui.PAUSE = 2
#SERVE PARA DEIXAR A AUTOMAÇÃO MAIS LENTA PARA VER O PROCESSO ACONTECER
pyautogui.press("win")
pyautogui.write ("microsoft edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
import time
time.sleep (5)
pyautogui.click(x=642, y=410) # clicar para realizar login
pyautogui.write (usuario)
#pyautogui.click(x=934, y=445)
#pyautogui.click(x=660, y=444)
pyautogui.press("tab") # digitar senha
pyautogui.write(senha)
pyautogui.press ("enter")
time.sleep (2)
pyautogui.click(x=60, y=197) #amostras
pyautogui.click(x=84, y=237) #consulta
time.sleep(3)
#importar base de dados
tabela = pandas.read_csv("amostras.csv")
print(tabela)
for linha in tabela.index:
    codigo = tabela.loc[linha,"CODCASONB"]
    pyautogui.click(x=505, y=288) #grupo
    time.sleep(5)
    pyautogui.click(x=469, y=322) #oncologia
    time.sleep(1)
    pyautogui.click(x=1013, y=284) #coleção
    # posicoes do click de acordo com o tipo de caso
    # x=918, y=290 controles ginecologia
    # x=960, y=341 controles mastologia
    # x=950, y=360 tumor colo uterino
    # =x=995, y=313 tumor colo retal
    # x=1050, y=387 tumor de mama
    # x=1050, y=404 tumor de ovario
    # x=1046, y=416 tumor de prostata
    # x=1066, y=431 tumores do snc 
    pyautogui.click(x=950, y=360) #selecionar coleção
    pyautogui.click(x=260, y=335) #abrir opções de caso
    pyautogui.click(x=914, y=377) #clicar para digitar código de caso
    pyautogui.write(tabela.loc[linha,"CODCASONB"])
    pyautogui.scroll(-15000)
    pyautogui.click(x=301, y=638)
    pyautogui.scroll(-1000)
    pyautogui.click(x=920, y=496)
    time.sleep (2)
    pyautogui.click(x=1061, y=589)
    pyautogui.click(x=699, y=445)
    time.sleep (10)
    #esperar configurar a impressora e etiquetas para terminar o RPA
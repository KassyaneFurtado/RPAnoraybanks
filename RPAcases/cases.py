import pyautogui
import time
import pandas
import pandas as pd

#OPCIONAL O RPA PODE FAZER LOGIN NO SISTEMA OU VOCÊ JÁ PODE DEIXAR NA PÁGINA
'''usuario = input("Insira seu usuário: ")
senha = input("Insira sua senha: ")
link = input("Insira o link do sistema: ")'''

'''pyautogui.press("win")
pyautogui.write ("microsoft edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
import time
time.sleep (5)
pyautogui.click(x=642, y=410) # clicar para realizar login
pyautogui.write (usuario)
pyautogui.press("tab") # digitar senha
pyautogui.write(senha)
pyautogui.press ("enter")'''

pyautogui.PAUSE = 2
#SERVE PARA DEIXAR A AUTOMAÇÃO MAIS LENTA PARA VER O PROCESSO ACONTECER
time.sleep (2)
pyautogui.click(x=69, y=158) #casos
pyautogui.click(x=87, y=198) #registro de casos
time.sleep(5)
#CONVERTER DATADECOLETA
tabela = pd.read_csv("CASES.csv")  
print(tabela)
# Lista de colunas a serem convertidas
colunas_para_converter = ["DATADECOLETA", "DATANASCIMENTO"]
# Criando novas colunas convertidas no DataFrame
for coluna in colunas_para_converter:
    nova_coluna = f"{coluna}_converted"
    tabela[nova_coluna] = tabela[coluna].apply(lambda x: '{:08}'.format(int(x)) if pd.notna(x) else '')
# Exibindo a tabela após a conversão
print("\nTabela após a Conversão:")
print(tabela)
# Salvar a tabela de volta para um novo arquivo CSV se necessário
tabela.to_csv("CASES_converted.csv", index=False)

for linha in tabela.index:
    pyautogui.click(x=456, y=220) #grupo
    pyautogui.click(x=495, y=263) #selecionar oncologia
    pyautogui.click(x=1106, y=218) #selecionar oncologia
    pyautogui.click(x=1055, y=338) #selecionar coleção
    # posicoes do click de acordo com o tipo de caso
    # x=918, y=290 controles ginecologia #alterar
    # x=960, y=341 controles mastologia #alterar
    # x=1113, y=294tumor colo uterino #alterar
    # x=1000, y=369 tumor colo retal #alterar
    # x=1053, y=326 tumor de mama #alterar
    # x=1055, y=338 tumor de ovario #alterar 
    # x=1046, y=416 tumor de prostata #alterar
    # x=963, y=372 tumores do snc 
    time.sleep(3)
    prontuario = tabela.loc[linha,"PRONTUARIO"]
    pyautogui.click(x=482, y=355)
    if not pandas.isnull("PRONTUARIO"):
     pyautogui.write(str(tabela.loc[linha,"PRONTUARIO"]))
     pyautogui.click(x=515, y=424)
     pyautogui.click(x=482, y=479) #escolher paciente ou controle
    #  posição do click controle x=486, y=466
    #  posição do click paciente x=482, y=479
    time.sleep(5)
    pyautogui.click(x=244, y=482)
    time.sleep(5)
    pyautogui.scroll(-20000)
    time.sleep(2)
    pyautogui.click(x=251, y=951)
    time.sleep(15)
    pyautogui.click(x=922, y=598)
    time.sleep(15)
    pyautogui.scroll(500)
    pyautogui.click(x=595, y=452) # CENTRO
    pyautogui.click(x=600, y=492) #IMP
    time.sleep(3)
    pyautogui.click(x=456, y=640)
    pyautogui.write(tabela.loc[linha,"NOME1"]) #escrever o primeiro nome
    pyautogui.click(x=973, y=639)
    pyautogui.write(tabela.loc[linha,"NOME2"]) #escrever o segundo nome
    pyautogui.click(x=1486, y=643)
    if not pandas.isnull(tabela.loc[linha,"NOME3"]):
            pyautogui.write(tabela.loc[linha,"NOME3"]) #escrever o sobrenome
    pyautogui.click(x=451, y=675)
    if not pandas.isnull(tabela.loc[linha, "DATANASCIMENTO_converted"]):
        pyautogui.write(str(tabela.loc[linha, "DATANASCIMENTO_converted"])) #escrever data de nascimento
    pyautogui.click(x=695, y=753)
    time.sleep(4)
    pyautogui.click(x=454, y=705)
    if not pandas.isnull(tabela.loc[linha, "PRONTUARIO"]):
        pyautogui.write(str(tabela.loc[linha,"PRONTUARIO"]))
    pyautogui.click(x=1530, y=672) # escolher sexo
    pyautogui.click(x=1532, y=729) #feminino
    pyautogui.scroll(-20000)
    pyautogui.click(x=269, y=915) #SALVAR
    time.sleep(15)
    pyautogui.click(x=922, y=595) #OK
    time.sleep(10)
    pyautogui.click(x=251, y=643)  #doações
    time.sleep(15)
    pyautogui.click(x=1436, y=286)
    if not pandas.isnull(tabela.loc[linha, "DATADECOLETA_converted"]):
        time.sleep(2)
        pyautogui.write(str(tabela.loc[linha,"DATADECOLETA_converted"]))
    time.sleep(5)    
    pyautogui.click(x=480, y=403)
    time.sleep(5)
    pyautogui.click(x=480, y=437)
    time.sleep(5)
    pyautogui.click(x=527, y=518)
    time.sleep(5)
    pyautogui.click(x=554, y=559) #escolher tipo de tcle
    # posição do click tcle biobanco x=554, y=559
    # posição do click tcle projeto x=542, y=588 #ALTERAR
    time.sleep(5)
    pyautogui.click(x=998, y=520)
    time.sleep(3)
    pyautogui.click(x=982, y=558)
    time.sleep(10)
    pyautogui.click(x=455, y=554)
    time.sleep(5)
    if not pandas.isnull(tabela.loc[linha, "DATADECOLETA_converted"]):
            pyautogui.write(str(tabela.loc[linha,"DATADECOLETA_converted"]))
    pyautogui.click(x=1048, y=849)
    pyautogui.scroll(-20000)
    pyautogui.click(x=261, y=978)
        # adicionar aqui comandos para lançar amostras
    time.sleep(15)
    pyautogui.click(x=929, y=594)
    time.sleep(10)
    pyautogui.scroll(20000)
    time.sleep(5)   
    pyautogui.click(x=126, y=197)
    time.sleep(5)

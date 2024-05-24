import pyautogui
import time
import pandas
import pandas as pd

#OPCIONAL O RPA PODE FAZER LOGIN NO SISTEMA OU VOCÊ JÁ PODE DEIXAR NA PÁGINA
'''usuario = input("Insira seu usuário: ")
senha = input("Insira sua senha: ")
link = input("Insira o link do sistema: ")'''

pyautogui.PAUSE = 2
#SERVE PARA DEIXAR A AUTOMAÇÃO MAIS LENTA PARA VER O PROCESSO ACONTECER
''' pyautogui.press("win")
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
time.sleep (2)
pyautogui.click(x=69, y=158) #casos
pyautogui.click(x=87, y=198) #registro de casos
time.sleep(5)
#CONVERTER DATADECOLETA"
# Leitura do arquivo CSV
tabela = pd.read_csv("CASOS.csv")  
# Exibindo a tabela original
print("Tabela Original:")
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
tabela.to_csv("CASOS_converted.csv", index=False)

for linha in tabela.index:
    pyautogui.click(x=456, y=220) #grupo
    pyautogui.click(x=495, y=263) #selecionar oncologia
    pyautogui.click(x=1106, y=218) #selecionar oncologia
    pyautogui.click(x=1053, y=326) #selecionar coleção
    # posicoes do click de acordo com o tipo de caso
    # x=918, y=290 controles ginecologia #alterar
    # x=960, y=341 controles mastologia #alterar
    # x=1113, y=294tumor colo uterino #alterar
    # x=1000, y=369 tumor colo retal #alterar
    # x=1053, y=326 tumor de mama #alterar
    # x=1078, y=338 tumor de ovario #alterar 
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
    pyautogui.click(x=285, y=654)
    time.sleep(15)
    pyautogui.click(x=652, y=439)
    time.sleep(15)
    pyautogui.scroll(1050)
    pyautogui.click(x=571, y=251)
    pyautogui.click(x=604, y=286)
    time.sleep(3)
    pyautogui.click(x=474, y=436)
    pyautogui.write(tabela.loc[linha,"NOME1"]) #escrever o primeiro nome
    pyautogui.click(x=982, y=437)
    pyautogui.write(tabela.loc[linha,"NOME2"]) #escrever o segundo nome
    pyautogui.click(x=459, y=474)
    if not pandas.isnull(tabela.loc[linha,"NOME3"]):
            pyautogui.write(tabela.loc[linha,"NOME3"]) #escrever o sobrenome
    pyautogui.click(x=963, y=470)
    if not pandas.isnull(tabela.loc[linha, "DATANASCIMENTO_converted"]):
        pyautogui.write(str(tabela.loc[linha, "DATANASCIMENTO_converted"])) #escrever data de nascimento
    pyautogui.click(x=1251, y=560)
    time.sleep(4)
    pyautogui.click(x=457, y=536)
    if not pandas.isnull(tabela.loc[linha, "PRONTUARIO"]):
        pyautogui.write(str(tabela.loc[linha,"PRONTUARIO"]))
    pyautogui.click(x=1035, y=497) # escolher sexo
    pyautogui.click(x=1022, y=552) #feminino
    pyautogui.scroll(-20000)
    pyautogui.click(x=307, y=598)
    time.sleep(15)
    pyautogui.click(x=688, y=450)
    time.sleep(10)
    pyautogui.click(x=255, y=332)  #doações
    time.sleep(15)
    pyautogui.click(x=1057, y=287)
    if not pandas.isnull(tabela.loc[linha, "DATADECOLETA_converted"]):
        time.sleep(2)
        pyautogui.write(str(tabela.loc[linha,"DATADECOLETA_converted"]))
    time.sleep(5)    
    pyautogui.click(x=467, y=417)
    time.sleep(5)
    pyautogui.click(x=459, y=454)
    time.sleep(5)
    pyautogui.click(x=524, y=530)
    time.sleep(5)
    pyautogui.click(x=542, y=572) #escolher tipo de tcle
    # posição do click tcle biobanco x=542, y=572
    # posição do click tcle projeto x=542, y=588
    time.sleep(5)
    pyautogui.click(x=973, y=536)
    time.sleep(3)
    pyautogui.click(x=1002, y=578)
    time.sleep(10)
    pyautogui.click(x=964, y=567)
    time.sleep(5)
    if not pandas.isnull(tabela.loc[linha, "DATADECOLETA_converted"]):
            pyautogui.write(str(tabela.loc[linha,"DATADECOLETA_converted"]))
    pyautogui.click(x=1261, y=455)
    pyautogui.scroll(-20000)
    pyautogui.click(x=256, y=669)
        # adicionar aqui comandos para lançar amostras
    time.sleep(15)
    pyautogui.click(x=673, y=447)
    time.sleep(10)
    pyautogui.scroll(20000)
    time.sleep(5)   
    pyautogui.click(x=125, y=195)
    time.sleep(5)
    
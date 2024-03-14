import pyautogui
import time
import pandas
import pandas as pd
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
    time.sleep (3) 
    pyautogui.click (x=98, y=159)
    pyautogui.click(x=81, y=196)
    time.sleep(3)

tabela = pandas.read_csv("PCM.csv")
print(tabela)
#CONVERTER DATADECOLETA"

# Leitura do arquivo CSV
tabela = pd.read_csv("PCM.csv")  
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
tabela.to_csv("PCM_converted.csv", index=False)

for linha in tabela.index:
    pyautogui.click(x=456, y=220) #grupo
    pyautogui.click(x=495, y=263) #selecionar oncologia
    pyautogui.click(x=1106, y=218) #selecionar oncologia
    pyautogui.click(x=1019, y=325) #selecionar coleção
    # posicoes do click de acordo com o tipo de caso
    # x=918, y=290 controles ginecologia #alterar
    # x=960, y=341 controles mastologia #alterar
    # x=1043, y=297 tumor colo uterino #alterar
    # x=1000, y=369 tumor colo retal #alterar
    # x=1019, y=325 tumor de mama #alterar
    # x=1050, y=404 tumor de ovario #alterar 
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
    time.sleep(3)
    pyautogui.click(x=242, y=477)
    time.sleep(5)
    pyautogui.scroll(-20000)
    pyautogui.click(x=285, y=654)
    time.sleep(10)
    pyautogui.click(x=652, y=439)
    time.sleep(10)
    pyautogui.scroll(1000)
    pyautogui.click(x=612, y=231)
    pyautogui.click(x=518, y=276)
    time.sleep(3)
    pyautogui.click(x=495, y=420)
    pyautogui.write(tabela.loc[linha,"NOME1"]) #escrever o primeiro nome
    pyautogui.click(x=915, y=417)
    pyautogui.write(tabela.loc[linha,"NOME2"]) #escrever o segundo nome
    pyautogui.click(x=564, y=452)
    if not pandas.isnull(tabela.loc[linha,"NOME3"]):
            pyautogui.write(tabela.loc[linha,"NOME3"]) #escrever o sobrenome
    pyautogui.click(x=900, y=453)
    if not pandas.isnull(tabela.loc[linha, "DATANASCIMENTO_converted"]):
        pyautogui.write(str(tabela.loc[linha, "DATANASCIMENTO_converted"])) #escrever data de nascimento
    pyautogui.click(x=1211, y=450)
    time.sleep(4)
    pyautogui.click(x=974, y=512)
    if not pandas.isnull(tabela.loc[linha, "PRONTUARIO"]):
        pyautogui.write(str(tabela.loc[linha,"PRONTUARIO"]))
    pyautogui.click(x=965, y=483) # escolher sexo
    pyautogui.click(x=931, y=538) #feminino
    pyautogui.scroll(-20000)
    pyautogui.click(x=307, y=598)
    time.sleep(10)
    pyautogui.click(x=688, y=450)
    time.sleep(5)
    pyautogui.click(x=255, y=332)  #doações
    time.sleep(5)
    pyautogui.click(x=1057, y=287)
    if not pandas.isnull(tabela.loc[linha, "DATADECOLETA_converted"]):
        time.sleep(2)
        pyautogui.write(str(tabela.loc[linha,"DATADECOLETA_converted"]))
    pyautogui.click(x=467, y=417)
    pyautogui.click(x=459, y=454)
    pyautogui.click(x=524, y=530)
    pyautogui.click(x=542, y=588) #escolher tipo de tcle
    # posição do click tcle biobanco x=542, y=572
    # posição do click tcle projeto x=542, y=588
    pyautogui.click(x=920, y=530)
    pyautogui.click(x=906, y=567)
    time.sleep(3)
    pyautogui.click(x=900, y=567)
    time.sleep(3)
    if not pandas.isnull(tabela.loc[linha, "DATADECOLETA_converted"]):
            pyautogui.write(str(tabela.loc[linha,"DATADECOLETA_converted"]))
    pyautogui.click(x=1261, y=455)
    pyautogui.scroll(-20000)
    pyautogui.click(x=256, y=669)
        # adicionar aqui comandos para lançar amostras
    time.sleep(3)
    pyautogui.click(x=673, y=447)
    pyautogui.scroll(20000)
    pyautogui.click(x=136, y=196)
    time.sleep(3)
    
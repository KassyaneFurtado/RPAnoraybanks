import pandas
import pandas as pd

# Leitura do arquivo CSV
tabela = pd.read_csv("casosgbmcerta.csv")  # Certifique-se de fornecer a extensão correta do arquivo, como ".csv"

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
tabela.to_csv("casosgbmcerta_converted.csv", index=False)

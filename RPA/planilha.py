from pandas import read_csv

def carregaCasos():
    return read_csv('CASES.csv')
def carregaAmostras():
    return read_csv('SAMPLE.csv')

def carregaPosicoes():
    return read_csv('POSITIONS.csv')

def pegaDado(planilha, nomeColuna, linha):
    return planilha.loc[linha, nomeColuna]

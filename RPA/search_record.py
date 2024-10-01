import pandas as pd

def searchRecord(noraybanks, samples, line):
    # Buscar amostra por prontuário
    if not pd.isnull(samples.loc[line, "PRONTUARIO"]):
        noraybanks.wait_for_selector('#nbConsulta1_TxtCodigoUnico')
        noraybanks.locator('#nbConsulta1_TxtCodigoUnico').click()
        prontuario = str(int(samples.loc[line, "PRONTUARIO"]))
        noraybanks.fill('#nbConsulta1_TxtCodigoUnico', prontuario)
def searchRecord(noraybanks, sample, linha):
    # Buscar amostra por prontuário
    if not pd.isnull(sample.loc[linha, "PRONTUARIO"]):
        noraybanks.wait_for_selector('#nbConsulta1_TxtCodigoUnico')
        noraybanks.locator('#nbConsulta1_TxtCodigoUnico').click()
        prontuario = str(int(sample.loc[linha, "PRONTUARIO"]))
        noraybanks.fill('#nbConsulta1_TxtCodigoUnico', prontuario)
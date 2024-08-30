def criaNavegador(playwright):
    sitenoraybanks = os.getenv('NORAYBANKS')

    navegador = playwright.chromium.launch(headless=False, args=['--ignore-certificate-errors'])
    noraybanks = navegador.new_page()
    noraybanks.goto(sitenoraybanks)

    return noraybanks
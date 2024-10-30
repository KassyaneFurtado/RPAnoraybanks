import os
from os import getenv

def createBrowser(playwright):
    sitenoraybanks = os.getenv('NORAYBANKS_URL')

    navegador = playwright.chromium.launch(headless=False, args=['--ignore-certificate-errors'])
    noraybanks = navegador.new_page()
    noraybanks.goto(sitenoraybanks)

    return noraybanks
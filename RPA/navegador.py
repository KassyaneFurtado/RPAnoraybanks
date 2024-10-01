import time
from os import getenv

def login(noraybanks):
    username = getenv('NORAYBANKS_USERNAME')
    password = getenv('NORAYBANKS_PASSWORD')

    noraybanks.wait_for_selector('#nbCtrlLoginNew1_LoginUser_UserName')
    time.sleep(5)
    noraybanks.fill('#nbCtrlLoginNew1_LoginUser_UserName',username) #LOGIN
    noraybanks.wait_for_selector('#nbCtrlLoginNew1_LoginUser_Password')
    noraybanks.fill('#nbCtrlLoginNew1_LoginUser_Password', password) #SENHA
    noraybanks.locator('#nbCtrlLoginNew1_LoginUser_LoginButton_jqbtn').click()
    time.sleep(5)


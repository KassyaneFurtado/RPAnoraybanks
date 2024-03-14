# RPA NORAYBANKS

Este projeto contém três arquivos com código para realizar diferentes funcionalidades no software Noraybanks para agilizar o lançamento de dados.

## Pré-requisitos
Antes de executar o script, certifique-se de ter instalado os seguintes requisitos:

1. Python 3.x
2. Biblioteca pyautogui
3. Biblioteca pandas
4. Você pode instalar as bibliotecas necessárias através do pip em seu terminal:
* pip install pyautogui
* pip isntall pandas

## Notas
* Estes scripts foram desenvolvidos para uma configuração específica do sistema NorayBanks e pode necessitar de ajustes para funcionar em outras instalações.
* Certifique-se de revisar e testar o script em um ambiente de teste antes de executá-lo em produção.

## Arquivos

## cases.py

### Automação de entrada de casos no NorayBanks

Este projeto consiste em um script Python para automatizar a entrada de casos no sistema NorayBanks de gerenciamento de Biobanco. O script utiliza a biblioteca pyautogui para simular a interação do usuário com a interface gráfica do sistema.

#### Funcionalidades:
- Realizar login no sistema NorayBanks.
- Importar uma base de dados contendo informações sobre as amostras a serem cadastradas.
- Iterar sobre cada amostra na base de dados e inserir seus códigos no sistema NorayBanks.
- Salvar as alterações e finalizar o processo.

#### Como Utilizar:
1. Faça o download do arquivo cases.py para o seu ambiente de trabalho.
2. Certifique-se de ter uma base de dados no formato CSV contendo as informações das casos a serem cadastradas. Certifique-se de alterar o nome do arquivo.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo cases.py está localizado.
4. Execute o script.
5. Siga as instruções fornecidas pelo script para inserir seu nome de usuário, senha e o link do sistema NorayBanks.

O script iniciará o processo de automação, realizando o login no sistema e inserindo os casos conforme os dados fornecidos na base de dados.

## barcode_ecode.py

### Automação de código de barras e código de entrada Noraybanks

Este projeto consiste em um script Python para automatizar a inserção de código de barras e código de entrada nas amostras cadastradas anteriormente no sistema NorayBanks de gerenciamento de Biobanco. O script utiliza a biblioteca pyautogui para simular a interação do usuário com a interface gráfica do sistema.

#### Funcionalidades:
1. Realizar login no sistema.
2. Importar uma base de dados contendo informações sobre as amostras a serem gerenciadas.
3. Inserir os códigos de barra e de entrada das amostras no sistema.

#### Como Utilizar:
1. Faça o download do arquivo barcode_ecode.py para o seu ambiente de trabalho.
2. Certifique-se de ter uma base de dados no formato CSV contendo as informações das amostras a serem gerenciadas.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo está localizado.
4. Execute o script.
5. Siga as instruções fornecidas pelo script para inserir seu nome de usuário, senha e o link do sistema NorayBanks.

## click_position_finder.py

Este é um script Python simples que utiliza a biblioteca pyautogui para realizar ações básicas de controle de mouse, como obter a posição do cursor e realizar um scroll para cima ou para baixo. Serve para configurar os outros arquivos conforme a máquina utilizada.

## leading_zero_converter.py

Este script Python tem como objetivo adicionar zeros à esquerda em números de um arquivo CSV e salvar o resultado em um novo arquivo CSV. Ele utiliza a biblioteca pandas para manipulação de dados.

#### Funcionalidades:
1. Lê um arquivo CSV contendo dados.
2. Adiciona zeros à esquerda em números das colunas especificadas.
3. Salva o resultado em um novo arquivo CSV.

#### Como Utilizar:
1. Faça o download do arquivo leading_zero_converter.py para o seu ambiente de trabalho.
2. Certifique-se de que o arquivo CSV tenha as colunas que deseja converter para números com zeros à esquerda.
3. Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão localizados.
4. Execute o script.
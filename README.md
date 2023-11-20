# Marvel API Repository

Welcome to the **Marvel API** repository! This repository contains a Power BI solution and a Python Flask app that interact with the Marvel Comics API (https://developer.marvel.com/docs) to provide comprehensive data about comics, characters, events, series, stories, and creators from the Marvel universe.  

[![Watch the video](https://miro.medium.com/v2/resize:fit:1358/0*qdHImq1G588SB9Ii.jpg)](https://youtu.be/Sw-Oe47Dxfw)

## Power BI Solution

The root directory of this repository contains a Power BI solution that visualizes the data obtained from the Marvel Comics API. The Power BI solution is designed to give you insights into various aspects of the Marvel universe, utilizing the data pulled from the API. You can access the **dashboard** available [at this link](https://app.powerbi.com/groups/me/reports/b86a5265-c089-495c-b6af-12c00bed6464/ReportSection?experience=power-bi) (for corporate or student accounts) to visually explore the data.

## Python Flask App

In the `app` directory, you'll find a Python Flask app that serves as an intermediary between the Marvel API and the Power BI solution. This app enables you to overcome the limitation of fetching only 100 objects per request from the Marvel API. By making a series of requests, the Python app accumulates a substantial volume of data, enhancing the dataset available for analysis in the Power BI solution.

### App Setup

1. Create a file named `.env` in the `app` directory.

2. Add the following lines to the `.env` file, replacing `YOUR_PUBLIC_KEY` and `YOUR_PRIVATE_KEY` with your actual Marvel API public and private keys, and `YOUR_MARVEL_API_URL` with the base URL of the Marvel API:

   ```plaintext
   PUBLIC_KEY='YOUR_PUBLIC_KEY'
   PRIVATE_KEY='YOUR_PRIVATE_KEY'
   URL='YOUR_MARVEL_API_URL'
   ```

### App Structure

- `app/routes`: This directory contains two files:
  - `routes_api.py`: This file defines routes that return data in JSON format from the Marvel API.
  - `route_json.py`: This file generates a JSON file locally on your machine.

- `app/src`: This directory holds the class files that structure the objects retrieved from the Marvel API.

- `app/data`: Here, you'll find JSON and XLSX files containing the data of various objects retrieved from the Marvel API.

- `app/main.py`: This file serves as the entry point for the Flask app. Running this file initializes the solution and makes it accessible through defined routes.

- `app/requirements.txt`: This file lists the libraries and dependencies required for the Flask app to run smoothly.

- `app/doc_time.txt`: This file records the execution times of the routes along with the final size of the objects.

### Running the Flask App

To run the Python Flask app and start fetching data from the Marvel API, follow these steps:

1. Install the required dependencies using the command:
   ```
   pip install -r app/requirements.txt
   ```

2. Navigate to the `app` directory:
   ```
   cd app
   ```

3. Run the Flask app:
   ```
   python main.py
   ```

The app will start running, and you can access the routes defined in `routes_api.py` to fetch data from the Marvel API. This data will be stored in the `data` directory and can be utilized for further analysis and visualization in the Power BI solution.

Feel free to explore, analyze, and visualize the vast Marvel universe using the data and tools provided in this repository. If you have any questions or need assistance, don't hesitate to reach out.

Enjoy your Marvel data journey! 🚀🦸‍♂️🦸‍♀️

# Repositório Marvel API

Bem-vindo ao repositório **Marvel API**! Este repositório contém uma solução em Power BI e um aplicativo Python Flask que interagem com a API da Marvel Comics (https://developer.marvel.com/docs) para fornecer dados abrangentes sobre quadrinhos, personagens, eventos, séries, histórias e criadores do universo Marvel.

## Solução Power BI

O diretório raiz deste repositório contém uma solução em Power BI que visualiza os dados obtidos da API da Marvel Comics. A solução Power BI foi projetada para fornecer insights sobre diversos aspectos do universo Marvel, utilizando os dados obtidos da API. Você pode acessar o **painel de controle** disponível [neste link](https://app.powerbi.com/groups/me/reports/b86a5265-c089-495c-b6af-12c00bed6464/ReportSection?experience=power-bi) (para contas corporativas ou de estudantes) para explorar visualmente os dados.

## Aplicativo Python Flask

No diretório `app`, você encontrará um aplicativo Python Flask que serve como intermediário entre a API da Marvel e a solução Power BI. Este aplicativo permite superar a limitação de buscar apenas 100 objetos por solicitação da API da Marvel. Ao fazer uma série de solicitações, o aplicativo Python acumula um volume substancial de dados, aprimorando o conjunto de dados disponível para análise na solução Power BI.

### Configuração do Aplicativo

1. Crie um arquivo chamado `.env` no diretório `app`.

2. Adicione as seguintes linhas ao arquivo `.env`, substituindo `SUA_CHAVE_PUBLICA` e `SUA_CHAVE_PRIVADA` pelas suas chaves públicas e privadas reais da API da Marvel, e `URL_API_MARVEL` pela URL base da API da Marvel:

   ```plaintext
   PUBLIC_KEY='SUA_CHAVE_PUBLICA'
   PRIVATE_KEY='SUA_CHAVE_PRIVADA'
   URL='URL_API_MARVEL'
   ```

### Estrutura do Aplicativo

- `app/routes`: Este diretório contém dois arquivos:
  - `routes_api.py`: Este arquivo define rotas que retornam dados no formato JSON da API da Marvel.
  - `route_json.py`: Este arquivo gera um arquivo JSON localmente em sua máquina.

- `app/src`: Este diretório contém os arquivos de classe que estruturam os objetos obtidos da API da Marvel.

- `app/data`: Aqui, você encontrará arquivos JSON e XLSX contendo os dados de vários objetos obtidos da API da Marvel.

- `app/main.py`: Este arquivo serve como ponto de entrada para o aplicativo Flask. Ao executar este arquivo, a solução é inicializada e pode ser acessada por meio das rotas definidas.

- `app/requirements.txt`: Este arquivo lista as bibliotecas e dependências necessárias para a execução tranquila do aplicativo Flask.

- `app/doc_time.txt`: Este arquivo registra os tempos de execução das rotas, juntamente com o tamanho final dos objetos.

### Executando o Aplicativo Flask

Para executar o aplicativo Python Flask e começar a buscar dados da API da Marvel, siga estas etapas:

1. Instale as dependências necessárias usando o comando:
   ```
   pip install -r app/requirements.txt
   ```

2. Navegue até o diretório `app`:
   ```
   cd app
   ```

3. Execute o aplicativo Flask:
   ```
   python main.py
   ```

O aplicativo será iniciado e você poderá acessar as rotas definidas em `routes_api.py` para buscar dados da API da Marvel. Esses dados serão armazenados no diretório `data` e podem ser usados para análises e visualizações adicionais na solução Power BI.

Sinta-se à vontade para explorar, analisar e visualizar o vasto universo Marvel usando os dados e ferramentas fornecidos neste repositório. Se tiver alguma dúvida ou precisar de ajuda, não hesite em entrar em contato.

Aproveite a jornada pelos dados da Marvel! 🚀🦸‍♂️🦸‍♀️
 

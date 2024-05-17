# Receptor de Webhook RD Station

Este repositório contém uma aplicação Flask que implementa um webhook para receber dados do RD Station. A aplicação foi estruturada da seguinte forma:

- `app`: Esta pasta contém o código principal da aplicação Flask.
    - `__init__.py`: Este arquivo inicializa a aplicação Flask e importa as rotas.
    - `routes.py`: Este arquivo define as rotas básicas da aplicação.
    - `rdstation_webhook.py`: Este arquivo define a rota do webhook que recebe os dados do RD Station.

- `.flaskenv`: Este arquivo contém as variáveis de ambiente para a aplicação Flask.

A aplicação foi projetada para receber um JSON do RD Station contendo informações sobre leads. Quando o webhook é acionado, a aplicação extrai o nome, email, telefone e data de criação do lead e retorna esses dados em um JSON.

## Como executar o script

1. **Instale as dependências**: No terminal, navegue até a pasta do projeto e instale as dependências necessárias com o comando `pip install -r requirements.txt`.

2. **Inicie o ambiente virtual**: Ative o ambiente virtual usando o comando `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows).

3. **Execute a aplicação Flask**: Inicie a aplicação Flask com o comando `flask run`. Isso iniciará o servidor de desenvolvimento do Flask e sua aplicação estará disponível em `http://localhost:5000`.

## Modelo JSON do RD Station

A aplicação espera receber um JSON do RD Station no formato especificado na documentação do RD Station. Por favor, consulte a documentação para obter detalhes sobre o formato exato do JSON.

## Iniciando o Flask

Depois de ativar seu ambiente virtual e instalar todas as dependências necessárias, você pode iniciar sua aplicação Flask com o comando `flask run` no terminal. Este comando inicia um servidor web local em sua máquina que é capaz de servir sua aplicação Flask. Por padrão, o servidor será iniciado na porta 5000, e você pode acessar sua aplicação navegando para `http://localhost:5000` em seu navegador web.

## Testando o Webhook

Para testar o webhook, você pode usar uma ferramenta como o Postman. O Postman permite que você envie solicitações HTTP de vários tipos (GET, POST, etc.) para o seu servidor e veja as respostas.

Aqui estão os passos básicos para testar o webhook com o Postman:

1. Abra o Postman e clique em "New Request".
2. Selecione o método "POST" e insira a URL do seu webhook (por exemplo, `http://localhost:5000/rdstation_webhook`).
3. Na seção "Body", selecione "raw" e "JSON" e insira o JSON que você deseja enviar para o webhook.
4. Clique em "Send" para enviar a solicitação.

Você deve ver a resposta do seu servidor no painel abaixo.

Lembre-se de que o JSON que você envia deve estar no formato esperado pelo webhook. Você pode encontrar um exemplo do formato na documentação do RD Station.

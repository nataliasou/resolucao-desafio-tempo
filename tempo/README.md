<h1 align="center"> ☔  Desafio de desenvolvimento  ☔</h1>
<p align="center">Projeto criado para solucionar o desafio da AEVO, 
com a utilização da API Weatherstack </p>

<h4 align="center"> 
	✅  Projeto concluído  ✅
</h4>

### ☀ Funções requeridas

- [x] Elaborar uma página para consultar e exibir as informações da requisição da API na página
- [x] Adicionar um input na página para permitir a busca por diferentes regiões.

### ⛅ Pré-requisitos

Para executar o projeto no seu computador, você vai precisar instalar o [Python](https://www.python.org/downloads/). Além disto, caso não tenha, instale um editor como [Pycharm](https://www.jetbrains.com/pt-br/pycharm/).
Também será preciso colocar o seu token de acesso a API, caso não tenha crie uma conta gratutita no site: https://weatherstack.com/
copie o seu token e siga os seguintes passos:

### ⚙ Rodando o Back End

```bash
# Abra o projeto no editor

# Acesse a pasta api e depois abra o arquivo views.py, coloque seu token na linha 9:
'access_key': 'MEU_TOKEN',

# Migre o banco
py manage.py makemigrations
py manage.py migrate

# Execute o servidor
py manage.py runserver

# Acesse a aplicação
http://127.0.0.1:8000/
```

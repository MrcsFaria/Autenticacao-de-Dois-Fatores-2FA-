# Autenticação de Dois Fatores-2FA
Este projeto implementa um sistema de autenticação de dois fatores usando Python com a utilização da biblioteca 'sqlite3', para cadastro, verificação e login de usuários. Também utiliza a biblioteca 'smtplib', que automatiza o envio de e-mails, neste caso, para enviar o código de verificação para o e-mail cadastrado pelo usuário. Além das bibliotecas Tkinter e CustomTkinter, para construção da interface gráfica.
Fiz este projeto para praticar o uso de bibliotecas de automatização de envio de e-mail, e criação e uso de banco dados utilizando bibliotecas python. 

## Funcionalidades

- Cadastro de Usuários: Permite aos usuários se cadastrarem com nome, e-mail e senha.
- Login: Verifica se o usuário está cadastrado no banco de dados.
- Autenticação de Dois Fatores: Envia um código de verificação para o e-mail do usuário para completar o login.

## Estrutura do Projeto

- 'Banco_de_dados/usuarios.db': Banco de dados SQLite onde os usuários são armazenados.
- 'assets/': Diretório contendo as imagens utilizadas na interface gráfica.
- 'criar_banco.py': Script para criar a tabela no banco de dados.
- 'main.py': Script principal que executa o sistema de autenticação.

## Layout do Sistema

<div style="display: flex; justify-content: space-around;">
    <img src="https://github.com/MrcsFaria/Autenticacao-de-Dois-Fatores-2FA-/blob/main/Prints/1.PNG" width="400">
    <img src="https://github.com/MrcsFaria/Autenticacao-de-Dois-Fatores-2FA-/blob/main/Prints/2.PNG" width="400">
    <img src="https://github.com/MrcsFaria/Autenticacao-de-Dois-Fatores-2FA-/blob/main/Prints/4.PNG" width="400">
    <img src="https://github.com/MrcsFaria/Autenticacao-de-Dois-Fatores-2FA-/blob/main/Prints/5.PNG" width="400">
</div>


# Tecnologias utilizadas
- Python
  
# Bibliotecas Python:
  - sqlite3: Biblioteca para gerenciar o banco de dados SQLite.
  - tkinter: Biblioteca padrão do Python para interfaces gráficas.
  - customtkinter: Utilizada para criar uma interface gráfica com componentes customizáveis.
  - smtplib: Biblioteca para envio de e-mails usando SMTP.
  - PIL: Biblioteca para manipulação de imagens.
  - python-dotenv: Biblioteca para carregar variáveis de ambiente de um arquivo `.env`.

# Como executar o projeto

Pré-requisitos: Python

```bash
# clonar repositório
git clone https://github.com/MrcsFaria/Autenticacao-de-Dois-Fatores-2FA-

# Navegue até o diretório do projeto:
```
cd Autenticacao-de-Dois-Fatores-2FA-
```

# Instale as dependências necessárias
pip install sqlite3 tkinter customtkinter tkinter smtplib pillow python-dotenv

# Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
```
EMAIL=seuemail@exemplo.com
SENHA=suasenha
```

# executar o projeto
python main.py
```


# Autor

Marcos Vinicius Faria

https://br.linkedin.com/in/marcos-vinicius-faria-124266186

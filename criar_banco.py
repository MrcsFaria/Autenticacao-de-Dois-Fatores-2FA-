import os
import sqlite3

diretorio = os.getcwd()
db_path = os.path.join(diretorio, "Banco_de_dados", "usuarios.db")
# Conectar ao banco de dados SQLite (o arquivo será criado se não existir)
conexao = sqlite3.connect(db_path)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()


# Definir o comando SQL para criar a tabela
query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);
"""

# Executar o comando SQL
cursor.execute(query)

# Salvar as alterações
conexao.commit()

# Fechar a conexão
conexao.close()

import mysql.connector


# 1 Código para conectar ao banco de dados MySQL e executar uma consulta:

conexao = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="meu_ecommerce"
        )

# 2 Criação da consulta SQL
cursor = conexao.cursor()

# 3 Definir a consulta SQL que você deseja executar
query = "SELECT * FROM produtos WHERE preco > 100.00"

# 4 Executar a consulta SQL
cursor.execute(query)

# 5 Obter os resultados da consulta
resultado = cursor.fetchall()

 # 6 Exibir os resultados
for linha in resultado:
    print(linha)

       
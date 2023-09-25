import pyodbc

dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-4RH07KQ\SQLEXPRESS;"
                 "Database=PythonSQL;"
                 )

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem Sucedida")

cursor = conexao.cursor()

comando = "INSERT INTO VENDAS(id_venda, cliente, produto, data_venda, preco, quantidade) VALUES (1, 'LIRA', 'PC', '2021-02-01', 8000, 1)"

ou

id = 3
cliente = "Lira Python"
produto = "Carro"
data = "25/08/2021"
preco = 5000
quantidade = 1

comando = f"INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade) VALUES ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"
cursor.execute(comando)
cursor.commit()

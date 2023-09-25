#CREATE
#READ
#UPDATE
#DELETE
#Importações
import mysql.connector
import pyodbc
#Conectando
dados_conexao = ("Driver={SQL Server};"
                 "Server=DESKTOP-4RH07KQ\SQLEXPRESS;"
                 "Database=PythonSQL;"
                 )

conexao = pyodbc.connect(dados_conexao)
print("Conexão bem Sucedida")
cursor = conexao.cursor()

#CREATE
# id = int(input("Insira um ID: "))
# cliente = str(input("Insira um nome: "))
# produto = str(input("Insira um produto: "))
# data = str(input("Insira uma data no formato YYYY-MM-DD: "))
# preco = int(input("Insira um Preço: "))
# quantidade = int(input("Insira a quantidade: "))

# comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade) 
# VALUES ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

# cursor.execute(comando)
# cursor.commit()


#READ
# comando2 = f"""SELECT * FROM Vendas"""
# cursor.execute(comando2)
# resultado = cursor.fetchall()
# print(resultado)


# #UPDATE
# coluna = input("quer mudar que coluna?: ")
# novovalor = input(f"qual o novo valor de {coluna}?: ")
# colunaref = input("Qual será a coluna de referencia?: ")
# valorref = input(f"que informação está na linha de referencia?: ")
# comando2 = f"""UPDATE vendas SET {coluna} = {novovalor} WHERE {colunaref} = '{valorref}'"""
# cursor.execute(comando2)
# cursor.commit()

#DELETE
colunadel = input("quer deletar informação de que coluna?: ")
valordel = input(f"que informação está na linha?: ")
comando2 = f"""DELETE FROM vendas WHERE {colunadel} = '{valordel}'"""
cursor.execute(comando2)
cursor.commit()

cursor.close()
conexao.close()

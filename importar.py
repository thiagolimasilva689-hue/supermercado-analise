import csv
import sqlite3

# Conectar ao banco
conexao = sqlite3.connect('minha_lista_compras.db')
cursor = conexao.cursor()

#criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lista  (
        Produto  TEXT,
        Marca TEXT,
        Preco FLOAT,
        Unidade TEXT
    )
''')
# LER O CSV
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\supermercado.csv'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho

    for linha in leitor:
        cursor.execute("INSERT INTO lista VALUES (?, ?, ?, ?)", 
                     (linha[0], linha[1],float(linha[2]),linha[3]))

""""
Consulta 1 — Produtos baratos
Mostre todos os produtos com preço menor que R$ 10.00, ordenados do mais barato para o mais caro.""
"""
print("-"*8,"OS PRODUTOS MAIS BARATOS QUE 10 REAIS","-"*8)
cursor.execute('''Select*from lista
               where Preco < 10.00
               order by Preco ASC
''')
for Produto,Marca,Preco,Unidade in cursor.fetchall():
    print(f"{Produto}|{Marca}|{Preco}|{Unidade}")


"""
Consulta 2 — Média de preços por marca
Mostre a média de preços dos produtos por marca. Agrupe por Marca.
"""





print("-"*8,"O PREÇOS MEDIOS DE CADA MARCA","-"*8)
#R:
cursor.execute('''Select
               AVG(Preco) as Media_preco,
               Marca
                 from lista
                        GROUP BY Marca        
''')
for media, marca in cursor.fetchall():
    print(f"{marca}: R$ {media:.2f}")



"""
Consulta 3 — Produto mais caro e mais barato
Mostre o produto mais caro (nome e preço) e o produto mais barato (nome e preço).

Dica: use ORDER BY Preco DESC LIMIT 1 e ORDER BY Preco ASC LIMIT 1.
"""


print("-"*8,"O PRODUTO MAIS CARO E MAIS BARATO","-"*8)
cursor.execute('''SELECT Produto, Preco
                  FROM lista
                  ORDER BY Preco DESC
                  LIMIT 1''')
caro = cursor.fetchone()
print(f"Mais caro: {caro[0]} - R$ {caro[1]:.2f}")

# Produto mais barato
cursor.execute('''SELECT Produto, Preco
                  FROM lista
                  ORDER BY Preco ASC
                  LIMIT 1''')
barato = cursor.fetchone()
print(f"Mais barato: {barato[0]} - R$ {barato[1]:.2f}")



"""
Consulta 4 — Buscar por nome
Peça ao usuário o nome de um produto e mostre todas as informações dele.

Dica: use input() e WHERE Produto = ?.
"""
#fazer um input

busca_nome = input("Digite o nome desse produto: ")
cursor.execute('SELECT * FROM lista WHERE Produto = ?',(busca_nome,))
for Produto,Marca,Preco,Unidade in cursor.fetchall():
    print(f"{Produto}|{Marca}|{Preco}|{Unidade}")



"""
Consulta 5 — Relatório final
Mostre:

Quantos produtos no total

Preço médio de todos os produtos

Soma total dos preços

Quantos produtos têm preço acima de R$ 20.00


cursor.execute('''SELECT COUNT(*) FROM LISTA''')
todos = cursor.fetchone()
print(f"O TOTAL DE PRODUTOS É: { todos[0] }")
  

cursor.execute('''SELECT AVG(preco) FROM LISTA''')
media = cursor.fetchone()
print(f"A media de preço dos produtos é : {media[0]:.2f}")


cursor.execute('''SELECT SUM(preco) FROM LISTA''')
total = cursor.fetchone()
print(f"O PREÇO TOTAL DE TUDOS OS PRODUTOS DA LISTA É : {total[0]}")

cursor.execute('''SELECT COUNT(preco) FROM LISTA WHERE preco > 20.00''')
maior_20 = cursor.fetchone()
print(f"QUANTOS SÃO MAIORES QUE 20: {maior_20[0]}")

"""


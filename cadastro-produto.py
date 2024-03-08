from openpyxl import Workbook

workbook = Workbook()

ativar = workbook.active

ativar["A1"] = "Produto"
ativar["B1"] = "Preço"

ultima_row = ativar.max_row

num_produtos = int(input("Quantos produtos você deseja adicionar? "))

for i in range(num_produtos):
    produto_nome = input(f"Digite o nome do produto {ultima_row + i + 1}: ")
    produto_preco = float(input(f"Digite o preço do produto {ultima_row + i + 1}: "))
    

    ativar.append([produto_nome, produto_preco])


workbook.save(filename="produtos.xlsx")

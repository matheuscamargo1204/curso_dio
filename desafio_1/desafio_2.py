# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []
contator = 0
# TODO: Crie um loop para solicita os itens ao usuário:
while contator < 3:
  item = input(str("insira um item"))
  contator +=1
  itens.append(item)


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")
comidas = ["Pao", "Sopa", 'Torta de Frango']
comidas.append("Brigadeiro")  # Adiciona "Brigadeiro" ao final da lista
comidas.remove("Sopa")    # Remove "Sopa" da lista
print(comidas[0])  
print(comidas[1])  
print(comidas[2])  
print(comidas)

for comida in comidas:
    print(f"Eu nao gosto de {comida}")

    maquiagem = ["Gloss", "Sombra", "Po", "Delineador"]

# Exibe os itens com frase
for item in maquiagem:
    print(f"Preciso comprar {item}")

# Remove um item que você decidiu não comprar
maquiagem.remove("Po")

# Exibe lista final
print("Lista atualizada:", maquiagem)

compras = []  # Lista vazia

while True:
    item = input("Digite um item para comprar (ou 'sair' para finalizar): ")
    if item.lower() == "sair":
        break  # Sai do loop
    compras.append(item)  # Adiciona o item na lista

print("\nLista de compras:")
for produto in compras:
    print(f"- {produto}")

compras = []

while True:
    comando = input("Digite um item para adicionar, ou 'remover nome' para excluir, ou 'sair' para finalizar: ")

    if comando.lower() == "sair":
        break

    elif comando.lower().startswith("remover"):
        partes = comando.split(" ", 1)  # divide o comando em ['remover', 'Arroz']
        if len(partes) > 1:
            item_remover = partes[1]
            if item_remover in compras:
                compras.remove(item_remover)
                print(f"{item_remover} removido da lista.")
            else:
                print(f"{item_remover} não está na lista.")
        else:
            print("Escreva o nome do item depois de 'remover'.")

    else:
        compras.append(comando)
        print(f"{comando} adicionado à lista.")

print("\nLista de compras final:")
for item in compras:
    print(f"- {item}")

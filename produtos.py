produtos = [
    {"nome": "Teclado", "preco": 150.00},
    {"nome": "Mouse", "preco": 80.00},
    {"nome": "Monitor", "preco": 1200.00},
    {"nome": "Headset", "preco": 250.00}
]

# Calculando total
total = 0

print("LISTA DE PRODUTOS")
print("-" * 40)

# Mostrar produtos numerados
for i, produto in enumerate(produtos):
    print(f"{i + 1} - {produto['nome']} | R$ {produto['preco']:.2f}")

print("-" * 40)

while True:
    escolha = input(
        "\nDigite o número do produto que deseja adicionar "
        "(ou 0 para finalizar): "
    )

    escolha = int(escolha)

    # Finalizar compra
    if escolha == 0:
        break

    # Verifica se o número é válido
    if 1 <= escolha <= len(produtos):

        produto = produtos[escolha - 1]

        quantidade = int(
            input(f"Quantidade de {produto['nome']}: ")
        )

        subtotal = quantidade * produto['preco']
        total += subtotal

        print(
            f"{produto['nome']} adicionado | "
            f"Subtotal: R$ {subtotal:.2f}"
        )

    else:
        print("Produto inválido!")

print("\n" + "-" * 40)
print(f"TOTAL DA COMPRA: R$ {total:.2f}")
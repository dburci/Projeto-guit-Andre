lista_de_preços = {
    "banana":{"preço": 2.99,},
    "maçã":{"preço": 3.99,},
    "morango": {"preço": 5.99,},
    "manga": {"preço": 7.99,},
    "abacaxi": {"preço": 10.99,},

}
def calcular_total(dicionario_de_produtos):
    total = 0
  
    for produto in dicionario_de_produtos.values():
   
        total = total + produto["preço"] 
    return total

resultado_da_compra = calcular_total(lista_de_preços)
print("O valor total da sua compra de frutas é: R$", resultado_da_compra)
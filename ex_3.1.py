from ex_3 import produtos

def exibir_promocoes(dicionario_generico):

    for produto, preco in dicionario_generico.items():
       
        if preco < 5.00:
            

            print(f"O produto {produto} está na promoção por R$ {preco}")


exibir_promocoes(produtos)
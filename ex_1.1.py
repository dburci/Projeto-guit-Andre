
def calcular_idade_cao(idade_humana):
    return idade_humana * 7
def par_ou_impar(numero):
  
 if numero % 2 == 0:
    print("Este número é PAR!")

 else:
    print("Este número é ÍMPAR!")

print("Qual é a idade do seu cachorro em anos humanos?")
idade_do_pet = int(input())


idade_final = calcular_idade_cao(idade_do_pet)


print("A sua idade em anos de cachorro é:", idade_final)
par_ou_impar( idade_do_pet)
par_ou_impar(idade_final)
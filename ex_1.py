
def calcular_idade_cao(idade_humana):
    return idade_humana * 7


print("Qual é a idade do seu cachorro em anos humanos?")
idade_do_pet = int(input())


idade_final = calcular_idade_cao(idade_do_pet)


print("A sua idade em anos de cachorro é:", idade_final)


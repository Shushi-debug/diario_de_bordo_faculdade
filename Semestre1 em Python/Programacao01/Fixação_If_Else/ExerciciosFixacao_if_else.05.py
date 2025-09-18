preco=float(input("Digite o valor do produto: "))

if preco<=0:
    print("Preço inválido!")
elif preco>=0 and preco<=30:
    print("Preço baixo!")
elif preco>=31 and preco<=50:
    print("Preço médio!")
elif preco>=51:
    print("Preço alto!")
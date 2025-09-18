A=int(input("Digite o primeiro número: "))
B=int(input("Digite o segundo número: "))

if B==0:
    print("O valor de B não pode ser 0!")

if B!=0:
    divisao=(int(A/B))
    print(f"A soma de {A} e {B} é {divisao}!")
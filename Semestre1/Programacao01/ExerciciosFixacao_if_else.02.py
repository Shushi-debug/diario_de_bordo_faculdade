num1=int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))

if num1!=num2:
    if num1>num2:
        print(f"O número {num1} é maior que {num2}")
    else:
        print(f"O número {num2} é maior que {num1}")
else:
    if num1==num2:
        print("Os números são iguais!")
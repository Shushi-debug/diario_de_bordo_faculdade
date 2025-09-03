import math
escolha=1
print("Bem-vindo à calculadora!")

while escolha!=7:
    print("1-Somar dois valores")
    print("2-Subtrair dois valores")
    print("3-Multiplicar dois valores")
    print("4-Dividir dois valores")
    print("5-Potência de dois valores")
    print("6-Radiciação de dois valores")
    print("7-Para sair")
    escolha=int(input(("Insira o número do tópico desejado:")))
    if escolha==1:
        escolha_math_menu=1
        while escolha_math_menu==1:
            print("Digite os números para somar:")
            num1=int(input("Digite o 1º número: "))
            num2=int(input("Digite o 2º número: "))
            saida=num1+num2
            print(f"A soma de {num1}+{num2}={saida}!")
            print("1-Somar novamente")
            print("2-Voltar ao menu")
            escolha_math_menu=int(input("Insira o número do tópico desejado:"))
    elif escolha==2:
        escolha_math_menu=1
        while escolha_math_menu==1:
            print("Digite os números para subtrair:")
            num1=int(input("Digite o 1º número: "))
            num2=int(input("Digite o 2º número: "))
            saida=num1-num2
            print(f"A subtração de {num1}-{num2}={saida}!")
            print("1-Subtrair novamente")
            print("2-Voltar ao menu")
            escolha_math_menu=int(input("Insira o número do tópico desejado:"))
    elif escolha==3:
        escolha_math_menu=1
        while escolha_math_menu==1:
            print("Digite os números para multiplicar:")
            num1=int(input("Digite o 1º número: "))
            num2=int(input("Digite o 2º número: "))
            saida=num1*num2
            print(f"A subtração de {num1}*{num2}={saida}!")
            print("1-Multiplicar novamente")
            print("2-Voltar ao menu")
            escolha_math_menu=int(input("Insira o número do tópico desejado:"))
    elif escolha==4:
        escolha_math_menu=1
        while escolha_math_menu==1:
            print("Digite os números para dividir:")
            num1=int(input("Digite o 1º número: "))
            num2=int(input("Digite o 2º número: "))
            saida=num1/num2
            print(f"A divisão de {num1}/{num2}={saida}!")
            print("1-Dividir novamente")
            print("2-Voltar ao menu")
            escolha_math_menu=int(input("Insira o número do tópico desejado:"))
    elif escolha==5:
        escolha_math_menu=1
        while escolha_math_menu==1:
            print("Digite os números para potenciação:")
            num1=int(input("Digite o 1º número: "))
            num2=int(input("Digite o 2º número: "))
            saida=num1**num2
            print(f"A potencia de {num1} sobre {num2} é {saida}!")
            print("1-Fazer potenciação novamente")
            print("2-Voltar ao menu")
            escolha_math_menu=int(input("Insira o número do tópico desejado:"))
    elif escolha==6:
        escolha_math_menu=1
        while escolha_math_menu==1:
            print("Digite os números para radiciação:")
            num1=int(input("Digite o número: "))
            saida=math.sqrt(num1)
            print(f"A raiz quadrada de {num1} é {saida}!")
            print("1-Fazer raiz quadrada novamente")
            print("2-Voltar ao menu")
            escolha_math_menu=int(input("Insira o número do tópico desejado:"))
    elif escolha==7:
        print("Muito obrigada por participar!")
        print("Volte sempre!")
valor=float(input("Digite o valor: "))

if valor<0:
    print("O valor não pode ser negativo!")

if valor>0 and valor<100:
    valor_final=float(valor+((valor/100)*10))
    print(f"O aumento é de 10%, o valor final ficou em {valor_final}")
elif valor>=101 and valor<=300:
    valor_final=float(valor+((valor/100)*20))
    print(f"O aumento é de 20%, o valor final ficou em {valor_final}")
elif valor>=300 and valor<=1000:
    valor_final=float(valor+((valor/100)*30))
    print(f"O aumento é de 30%, o valor final ficou em {valor_final}")

while True:
    grau_a=int(input("Digite a sua nota do Grau A: "))
    grau_b=int(input("Digite a sua nota do Grau B: "))
    
    if grau_a<0 or grau_b<0:
        print("A nota não pode ser negativa! Tente de novo.")
    else:
        break
    
nota_a=grau_a*0.3
nota_b=grau_b*0.7

if nota_a+nota_b<=6.0:
    print("Você precisará fazer o Grau C.")
else:
    print("Você passou!")
a = int(input("Digite o 1ºn: "))
b = int(input("Digite o 2ºn: "))
c = int(input("Digite o 3ºn: "))

xPrimeiro = ((b*-1)+(b**2-4*a*c)**(1/2))/(2*a)
xSegundo = ((b*-1)-(b**2-4*a*c)**(1/2))/(2*a)

print("x'=",xPrimeiro)
print("x''=",xSegundo)

'''Exercício matemático com base em bhaskara, bem difícil por sinal! :D numeros que funcionam bem para teste: a=1 b=-4 c=-12'''
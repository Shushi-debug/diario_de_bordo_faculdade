A=int(input("Digite o primeiro número: "))
B=int(input("Digite o segundo número: "))
C=int(input("Digite o terceiro número: "))

if A==B==C:
    print("Os números são iguais!")

if A!=B or B!=C:
    if A<B and A<C:
        print(f"O número {A} é o menor.")
    if B<A and B<C:
        print(f"O número {B} é o menor")
    if C<A and C<B:
        print(f"O número {C} é o menor")
public class Teste {
public static void main(String[] args) {

ContaCorrente conta1=new ContaCorrente();
conta1.numero=1234;
conta1.saldo=100.00;
System.out.println("Conta 1 - Número: " + conta1.numero + ", Saldo: " + conta1.saldo);

ContaCorrente conta2=new ContaCorrente();
conta2.numero=8765;
conta2.saldo=-98.00;
System.out.println("Conta 2 - Número: " + conta2.numero + ", Saldo: " + conta2.saldo);

ContaCorrente conta3=new ContaCorrente();
conta3.numero=3342;
conta3.saldo=3445.80;
System.out.println("Conta 3 - Número: " + conta3.numero + ", Saldo: " + conta3.saldo);

}
}

public class Produto {
    String nome;
    double valor;
    String descricao;
    int estoque;
public Produto(){
    this.nome="Vaso de Planta";
    this.valor=5.90;
    this.descricao="Vaso de cerâmica";
    this.estoque=4;
}
public Produto(String nome, double valor, String descricao, int estoque){
    this.nome=nome;
    this.valor=valor;
    this.descricao=descricao;
    this.estoque=estoque;
}
}

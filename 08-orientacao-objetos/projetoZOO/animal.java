public class animal {
    protected String nome;
    protected int idade;

    public animal(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public void emitirSom() {
        System.out.println("O animal faz um som.");
    }

    public void exibirInfo() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade + " anos");
    }
}

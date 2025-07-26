public class mamifero extends animal {
    public mamifero(String nome, int idade) {
        super(nome, idade);
    }

    @Override
    public void emitirSom() {
        System.out.println("Mamífero emite som.");
    }
}

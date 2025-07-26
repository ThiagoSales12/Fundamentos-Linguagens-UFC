public class papagaio extends ave {
    public papagaio(String nome, int idade) {
        super(nome, idade);
    }

    @Override
    public void emitirSom() {
        System.out.println("O papagaio fala: 'Olá!'");
    }
}

public class ave extends animal {
    public ave(String nome, int idade) {
        super(nome, idade);
    }

    @Override
    public void emitirSom() {
        System.out.println("Ave canta.");
    }
}
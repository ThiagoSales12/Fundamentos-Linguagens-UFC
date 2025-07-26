public class leao extends mamifero {
    public leao(String nome, int idade) {
        super(nome, idade);
    }

    @Override
    public void emitirSom() {
        System.out.println("O leão ruge!");
    }
}

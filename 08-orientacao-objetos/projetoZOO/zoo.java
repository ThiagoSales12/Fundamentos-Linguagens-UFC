public class zoo{
    public static void main(String[] args) {
        leao leao = new leao("Simba", 5);
        papagaio papagaio = new papagaio("Loro", 2);

        System.out.println("Informações do Leão:");
        leao.exibirInfo();
        leao.emitirSom();

        System.out.println("\nInformações do Papagaio:");
        papagaio.exibirInfo();
        papagaio.emitirSom();
    }
}

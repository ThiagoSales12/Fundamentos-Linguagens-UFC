# Concorrência em Software: Processos e Threads para Otimização

No mundo real, muitos eventos ocorrem simultaneamente, e o software moderno precisa modelar essa simultaneidade. A concorrência é o paradigma que nos permite gerenciar múltiplas tarefas que progridem ao mesmo tempo, otimizando o uso de processadores multi-núcleo e garantindo a responsividade de aplicações, servidores de alta performance e processamento de dados em larga escala. Este documento explora os fundamentos da concorrência, diferenciando processos e threads, e demonstra como a concorrência pode acelerar tarefas computacionalmente intensivas.

---

## Processos vs. Threads: As Unidades de Execução

Embora ambos permitam a execução paralela de tarefas, processos e threads são conceitualmente distintos e servem a propósitos diferentes.

### Processo: A "Caixa" Isolada

- **Definição:** Um programa em execução. Cada processo é uma "caixa" isolada, com seu próprio espaço de memória, recursos e identificador no sistema operacional.
- **Memória:** Totalmente independente. A comunicação entre processos é segura, mas mais lenta e complexa, exigindo mecanismos de IPC (Inter-Process Communication).
- **Robustez:** Alta. A falha de um processo não afeta os outros. Se o seu navegador travar, seu editor de texto continua funcionando.
- **Custo:** "Pesado". A criação de um processo consome uma quantidade significativa de tempo e recursos do sistema.

### Thread: A Unidade de Execução Leve

- **Definição:** Uma unidade de execução dentro de um processo. Um único processo pode ter múltiplas threads, que são como "mini-programas" rodando em paralelo.
- **Memória:** Compartilham o mesmo espaço de memória do processo pai. Isso torna a comunicação entre elas extremamente rápida, mas também perigosa se não for bem gerenciada (risco de race conditions).
- **Robustez:** Baixa. Uma falha em uma thread (como um acesso indevido à memória) pode derrubar o processo inteiro.
- **Custo:** "Leve". Threads são muito mais rápidas de criar e destruir.

---

## Cenários Práticos de Concorrência

Para demonstrar a concorrência, simulamos dois cenários comuns onde a paralelização pode trazer ganhos significativos.

### 1. Processamento de Imagens em Lote

- **Problema (Abordagem Sequencial):** Processar uma imagem após a outra. Se cada uma levar 1 segundo para processar e houver 8 imagens, o tempo total será de 8 segundos, utilizando apenas um núcleo do processador.
- **Solução (Abordagem Concorrente):** Criar uma thread para cada imagem (ou grupo de imagens). Em um computador com múltiplos núcleos, é poss


# Ambientes de Programação: Como o Código Vira Executável

Ambientes de programação são as estruturas essenciais que transformam o código-fonte que escrevemos em programas que podem ser executados por uma máquina.  
Essa transformação pode ocorrer por meio de **compilação antecipada**, **interpretação passo a passo** ou **execução em uma camada virtual**.

Vamos detalhar o funcionamento interno desses modelos, destacando o percurso do código-fonte até sua execução.

---

## Os Três Modelos Principais de Execução de Programas

A forma como uma linguagem de programação é executada define suas **características de desempenho, portabilidade e flexibilidade**.  
Existem três modelos principais:

---

### 1. Compilação Direta para Código de Máquina

- **Processo:**  
  O compilador (como o GCC para C) traduz o código-fonte (por exemplo, um arquivo `.c`) diretamente para código de máquina executável (como um `.exe` ou `.out`).  
  Todo o código é analisado, otimizado e transformado em um artefato pronto para ser distribuído e executado sem traduções adicionais.  
  O compilador também verifica erros de sintaxe e tipo durante esse processo.

- **Exemplos de Linguagens:**  
  `C`

- **Vantagens:**
  - Execução rápida e eficiente
  - Acesso direto ao hardware
  - Aproveitamento máximo da arquitetura alvo

- **Desvantagens:**
  - Baixa portabilidade: o executável gerado é específico para um sistema operacional e arquitetura
  - Exige recompilação para outras plataformas

---

### 2. Interpretação

- **Processo:**  
  Um interpretador lê o código-font


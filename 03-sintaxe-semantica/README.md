# Sintaxe e Semântica: A Estrutura e o Significado do Código

Em linguagens de programação, a **sintaxe** dita o formato correto das instruções ("como escrever"), enquanto a **semântica** define o significado delas ("o que o código faz"). Para entender esses conceitos fundamentais – **tokens, gramática, análise léxica, parsing e semântica** – vamos usar exemplos de mini-linguagens fictícias.

---

## Análise Léxica: Transformando Código em Tokens

A **análise léxica** é o primeiro passo: o código-fonte é quebrado em unidades mínimas e significativas, chamadas **tokens**. Cada token representa uma categoria (como um número, identificador, operador ou palavra-chave). Espaços em branco e comentários são ignorados nessa fase.

### Exemplo de Tokens (Mini-Linguagens de Orçamento e CT):

* **IDENT** ou **ID**: `base`, `total`, `x`, `y` (variáveis)
* **NUM**: `100.0`, `5`, `10` (números)
* **PRINT**: `print` (comando)
* **Operadores**: `+`, `-`, `*`, `/`, `%`, `=`, `==`, `>`, etc.
* **Funções**: `ceil`, `floor`
* **Estruturas**: `if`, `then`, `end`, `(`, `)`, `;`

---

## Gramática em EBNF: A Receita da Linguagem

A **gramática**, geralmente expressa em **EBNF** (Extended Backus-Naur Form), define as regras de combinação dos tokens para formar construções válidas. Ela é crucial para a **análise sintática (parsing)**, que verifica se o código segue as regras da linguagem.

### Exemplos de Regras Gramaticais:

* `<programa> ::= { <instrucao> }` (Um programa é uma sequência de instruções)
* `<instrucao> ::= <atribuicao> ";" | <print_instr> ";" | <condicional>` (Uma instrução pode ser uma atribuição, um print ou um condicional)
* `<expr> ::= <term> { ("+" | "-" ) <term> }` (Uma expressão envolve termos com adição/subtração)

---

## Semântica: O Significado por Trás da Estrutura

A **semântica** dá vida ao código, explicando o que cada parte faz.

### Semântica Estática (Verificações Antes da Execução):

* **Tipagem**: Define os tipos de dados (ex: todas as variáveis são float ou numéricas/inteiras).
* **Declaração/Atribuição**: Exige que variáveis sejam atribuídas antes de serem usadas.
* **Compatibilidade**: Operadores só aceitam tipos de dados compatíveis (ex: números com números).

### Semântica Dinâmica (Comportamento Durante a Execução):

* **Literais**: Retornam seu próprio valor (ex: `100` é `100`).
* **Identificadores**: Buscam o valor armazenado na memória.
* **Operações**: Avaliam expressões recursivamente.
* **%**: Converte para decimal (ex: `5%` vira `0.05`).
* **ceil/floor**: Arredondam valores.
* **print(expr)**: Exibe o resultado de uma expressão.
* **if**: Avalia uma condição para decidir se executa um bloco de código.

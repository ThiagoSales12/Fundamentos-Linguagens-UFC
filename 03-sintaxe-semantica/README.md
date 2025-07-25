# Sintaxe e Semântica: A Estrutura e o Significado do Código

Em linguagens de programação, a **sintaxe** dita o formato correto das instruções (*"como escrever"*), enquanto a **semântica** define o significado delas (*"o que o código faz"*).  

Para entender esses conceitos fundamentais — **tokens**, **gramática**, **análise léxica**, **parsing** e **semântica** — usaremos exemplos de mini-linguagens fictícias.

---

## 🔍 Análise Léxica: Transformando Código em Tokens

A **análise léxica** é o primeiro passo da compilação/interpretação.  
Nessa etapa, o código-fonte é quebrado em **unidades mínimas e significativas**, chamadas **tokens**.

Cada token representa uma **categoria** como:

- Número
- Identificador (variável)
- Operador
- Palavra-chave

> Comentários e espaços em branco geralmente são **ignorados** nessa fase.

### Exemplo de Tokens (Mini-Linguagens de Orçamento e CT)

| Token        | Exemplos                      | Categoria       |
|--------------|-------------------------------|------------------|
| `IDENT` / `ID` | `base`, `total`, `x`, `y`      | Identificadores |
| `NUM`         | `100.0`, `5`, `10`             | Números         |
| `PRINT`       | `print`                        | Palavra-chave   |
| Operadores    | `+`, `-`, `*`, `/`, `%`, `=`, `==`, `>` | Operadores       |
| Funções       | `ceil`, `floor`                | Funções         |
| Estruturas    | `if`, `then`, `end`, `(`, `)`, `;` | Palavras-chave   |

---

## 📐 Gramática em EBNF: A Receita da Linguagem

A **gramática** define as **regras de combinação dos tokens** para formar construções válidas.  
Geralmente é escrita em **EBNF** (Extended Backus-Naur Form) e usada no processo de **parsing** (análise sintática).

### Exemplos de Regras Gramaticais:

```ebnf
<programa>   ::= { <instrucao> }
<instrucao>  ::= <atribuicao> ";" | <print_instr> ";" | <condicional>
<expr>       ::= <term> { ("+" | "-") <term> }


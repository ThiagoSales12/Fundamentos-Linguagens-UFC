# Passagem de Parâmetros: Valor vs. Referência em Funções

Subprogramas (funções/métodos) são essenciais para organizar o código. A forma como eles recebem dados (parâmetros) define se a função trabalha com uma **cópia dos dados** (passagem por valor) ou com o **acesso direto ao original** (passagem por referência). Isso impacta se as mudanças dentro da função afetam a variável fora dela.

---

## Por Valor vs. Por Referência: A Diferença

### ✅ Por Valor
- A função recebe **uma cópia** do dado.
- Alterações dentro da função **não afetam a variável original**.
- É **mais seguro**, mas pode ser **menos eficiente** para dados grandes (pois exige cópia).

### 🔁 Por Referência
- A função recebe **um acesso direto** à variável original.
- Alterações dentro da função **afetam a variável original**.
- É **mais eficiente**, mas **menos seguro** (pode gerar efeitos colaterais inesperados).

---

## Como as Linguagens Lidam com Isso

Cada linguagem tem sua abordagem, influenciada por como gerencia seus tipos de dados:

---

### 1. 🟦 C: Padrão por Valor, Ponteiros para Referência

- **Por Valor** (padrão): Para tipos básicos (`int`, `float`), a função recebe uma cópia.
- **Por Referência**: Simulado com **ponteiros**. Você passa o endereço de memória da variável original, permitindo que a função a modifique diretamente.

```c
void incrementa(int *x) {
    (*x)++;
}


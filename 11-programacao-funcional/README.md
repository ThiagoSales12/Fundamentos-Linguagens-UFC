# Programação Funcional: Clareza e Robustez no Processamento de Dados

A **Programação Funcional (PF)** oferece um paradigma distinto da Programação Orientada a Objetos, tratando a computação como a avaliação de funções matemáticas e evitando estados mutáveis e dados compartilhados. Isso promove um estilo de código mais declarativo, onde o foco é o que queremos fazer, e não como fazer passo a passo. Este conceito se destaca em cenários de processamento de dados, como a análise de transações financeiras e o cálculo de tempo de tarefas, onde a clareza e a robustez são essenciais.

---

## Conceitos Funcionais em Ação (Implementação em Python)

As soluções apresentadas demonstram os pilares da programação funcional:

### 1. Funções de Alta Ordem (`map`, `filter`, `reduce`)

As **funções de alta ordem** são o coração da PF, pois podem receber outras funções como argumento ou retorná-las como resultado. Elas permitem construir *pipelines* de dados expressivos e fáceis de entender.

* **`filter`:** Usada para selecionar elementos que atendem a um critério específico.
    * **Exemplo:** Filtrar transações do tipo "Crédito" ou tarefas com tempo maior que 30 minutos.
* **`map`:** Aplicada para transformar cada elemento de uma coleção.
    * **Exemplo:** Calcular e adicionar uma taxa de processamento a cada transação, ou formatar transações para um relatório.
* **`reduce`:** Utilizada para "reduzir" uma coleção a um único valor.
    * **Exemplo:** Somar os valores de todas as transações processadas ou calcular o tempo total de tarefas filtradas.

### 2. Funções Puras e Imutabilidade

As **funções puras** são blocos de construção previsíveis. Uma função é pura se:

* Seu resultado depende unicamente de seus argumentos de entrada.
* Não produz efeitos colaterais observáveis (não modifica variáveis globais, não escreve em arquivos, etc.).

O princípio da **imutabilidade** é crucial aqui: em vez de modificar dados originais, as funções puras criam cópias com as alterações desejadas. Isso torna o fluxo de dados mais seguro e fácil de rastrear, prevenindo *bugs* inesperados.

### 3. Recursão

A **recursão** é uma técnica fundamental na programação funcional para percorrer coleções de dados sem usar laços imperativos. Uma função recursiva segue o padrão clássico:

* **Caso Base:** Uma condição de parada que retorna um valor direto (ex: lista vazia retorna 0).
* **Passo Recursivo:** A função chama a si mesma com um argumento modificado (ex: soma o primeiro elemento e chama a função para o restante da lista).

A recursão serve como uma alternativa elegante a `reduce` para agregar valores, reforçando a abordagem funcional.

---

## Exemplos de Aplicação

### Análise de Transações Financeiras

Um *pipeline* funcional pode ser montado para:

* Filtrar transações por tipo (ex: "Crédito").
* Mapear para adicionar taxas de processamento.
* Reduzir para calcular o valor total bruto.
* Mapear novamente para formatar um relatório final.

### Cálculo Funcional de Tempo de Tarefas

É possível calcular o tempo total gasto em tarefas que satisfaçam um critério definido pelo usuário:

* As tarefas são representadas como dicionários (`{"nome": "Estudar", "tempo": 120, "prioridade": 2}`).
* Uma função de alta ordem (`calcular_tempo_total`) recebe uma função filtro (ex: `lambda t: t["tempo"] > 30`) para determinar quais tarefas incluir no cálculo.
* A recursão é utilizada para percorrer a lista e somar os tempos das tarefas que passam no filtro, mantendo a lista original inalterada.

```python
tarefas = [
    {"nome": "Estudar", "tempo": 120, "prioridade": 2},
    {"nome": "Exercícios", "tempo": 45, "prioridade": 3},
    {"nome": "Ler emails", "tempo": 15, "prioridade": 1},
]

# Exemplo de função filtro (função de alta ordem)
filtro_tarefas_longas = lambda t: t["tempo"] > 30

# Exemplo de função recursiva (poderia ser o calcular_tempo_total)
def calcular_total_recursivo(lista_tarefas, filtro):
    if not lista_tarefas:
        return 0
    primeira_tarefa = lista_tarefas[0]
    tempo_atual = primeira_tarefa["tempo"] if filtro(primeira_tarefa) else 0
    return tempo_atual + calcular_total_recursivo(lista_tarefas[1:], filtro)

total = calcular_total_recursivo(tarefas, filtro_tarefas_longas)
print(f"Tempo total de tarefas longas: {total} minutos") # Saída: Tempo total de tarefas longas: 165 minutos

## Conclusão

A **Programação Funcional** oferece uma abordagem poderosa para construir soluções robustas e expressivas, especialmente em problemas de processamento de dados. Ao compor um *pipeline* com **funções puras**, **imutabilidade**, **funções de alta ordem** e **recursão**, criamos um código que é conciso, previsível e mais fácil de manter e testar, formando uma alternativa eficaz aos laços e condicionais do paradigma imperativo.

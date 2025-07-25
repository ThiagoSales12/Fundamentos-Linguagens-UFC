# Programação Lógica: Modelando Conhecimento com Prolog

A **Programação Lógica** representa uma abordagem declarativa única para a resolução de problemas. Em vez de ditar uma sequência de passos, nós descrevemos **fatos** e **regras** que definem um domínio de conhecimento, e então o sistema de inferência descobre as respostas. **Prolog** é a linguagem mais emblemática desse paradigma.

---

## Programação Lógica e Prolog: Fatos, Regras e Consultas

Um programa em Prolog não tem um fluxo de execução tradicional. Ele é composto por uma **base de conhecimento** e **consultas**.

* **Fatos (Facts):** São declarações elementares e incondicionalmente verdadeiras sobre o domínio. São os "átomos" do conhecimento.
    * **Exemplos:** `homem(joao).`, `progenitor(joao, maria).` (João é progenitor de Maria).
* **Regras (Rules):** São inferências que descrevem como novo conhecimento pode ser deduzido a partir de fatos ou outras regras existentes. A sintaxe `cabeca :- corpo.` pode ser lida como "A cabeça é verdadeira se o corpo for verdadeiro".
    * **Exemplo:** `pai(X, Y) :- progenitor(X, Y), homem(X).` (X é pai de Y se X é progenitor de Y E X é homem).
* **Consultas (Queries):** São as perguntas feitas à base de conhecimento. O motor do Prolog explora automaticamente as relações e tenta encontrar todas as soluções possíveis que tornam a consulta verdadeira. Não há uma sequência de comandos explícita; o Prolog se encarrega da busca.

---

## Modelagem de Árvore Genealógica: Um Exemplo Clássico

Para demonstrar os conceitos fundamentais da programação lógica, escolhemos modelar um problema clássico e intuitivo: uma árvore genealógica simples. Esse tipo de problema é ideal para ilustrar como podemos definir relações familiares complexas a partir de informações básicas.

---

### Estrutura do Código Prolog

O código Prolog para uma árvore genealógica é tipicamente dividido em duas partes essenciais:

* **Base de Fatos:** Contém as declarações básicas e irrefutáveis sobre os indivíduos e suas relações diretas.
    ```prolog
    homem(joao).
    mulher(ana).
    progenitor(joao, pedro).
    progenitor(ana, pedro).
    ```
* **Base de Regras:** Estabelece as relações derivadas e mais complexas, usando os fatos como base para inferência.
    ```prolog
    pai(X, Y) :- progenitor(X, Y), homem(X).
    mae(X, Y) :- progenitor(X, Y), mulher(X).
    avo(X, Y) :- progenitor(X, Z), progenitor(Z, Y). % X é avô/avó de Y se X é progenitor de Z E Z é progenitor de Y
    irmao(X, Y) :- progenitor(Z, X), progenitor(Z, Y), X \= Y. % X é irmão de Y se eles têm o mesmo progenitor Z E X não é o próprio Y
    ```
Essa organização facilita a manutenção e ampliação do conhecimento, tornando o código claro e modular.

---

### Exemplos de Consultas (Queries)

Para interagir com a base de conhecimento, você faz consultas ao sistema Prolog:

* **Consulta:** `pai(joao, ana).`
    * **Tradução:** "João é pai de Ana?"
    * **Resposta Esperada:** `true` ou `false`, dependendo dos fatos definidos.
* **Consulta:** `avo(fernando, maria).`
    * **Tradução:** "Fernando é avô de Maria?"
    * **Resposta Esperada:** `true` ou `false`, dependendo da inferência das regras.
* **Consulta:** `irmao(pedro, X).`
    * **Tradução:** "Quem são os irmãos de Pedro?"
    * **Resposta Esperada:** Prolog buscará e retornará todos os valores possíveis para `X` que satisfaçam a relação (ex: `X = ana.`).

---

## Conclusão

A **Programação Lógica**, exemplificada pelo **Prolog**, oferece uma forma poderosa de resolver problemas que envolvem lógica, raciocínio e busca em bases de conhecimento complexas. Ao invés de nos preocuparmos com laços e controle de fluxo, o foco recai sobre a descrição precisa e declarativa do problema, permitindo que o motor de inferência deduza as respostas.

# Gerenciamento de Animais em um Zoológico: Desvendando a POO

A **Programação Orientada a Objetos (POO)** é uma abordagem essencial para desenvolver sistemas robustos, modelando entidades do mundo real de forma clara e reutilizável. Neste desafio, um sistema simples de gerenciamento de animais em um zoológico foi criado, simulando o comportamento de diferentes espécies. Isso demonstra os principais pilares da POO de forma prática e didática.

---

## Programação Orientada a Objetos (POO)

Este projeto foi cuidadosamente estruturado para ilustrar os quatro pilares fundamentais da Programação Orientada a Objetos:

### Abstração

A classe **`Animal`** foi definida como **abstrata**.

Ela representa um animal genérico e define o contrato mínimo que qualquer animal deve seguir: possuir um **nome** e um método **`EmitirSom()`** que deve ser implementado por todas as subclasses. Isso impede a criação de animais genéricos e obriga cada animal concreto a definir seu próprio som.

### Herança

A hierarquia de herança é organizada da seguinte forma:
Animal (classe abstrata)
├── Mamifero
│   └── Leao
└── Ave
└── Papagaio
As classes **`Mamifero`** e **`Ave`** herdam de **`Animal`** e servem de base para animais mais específicos, criando uma estrutura de especialização.

### Encapsulamento

As propriedades como **`Nome`** e **`Idade`** são protegidas por **encapsulamento**, garantindo controle sobre os dados.

Além disso, a visibilidade adequada é aplicada para permitir acesso somente onde for necessário, protegendo a integridade dos atributos.

### Polimorfismo

O método **`EmitirSom()`** é abstrato na classe **`Animal`** e **sobrescrito** em cada animal específico.

Dessa forma, mesmo usando uma lista de `Animal`, cada objeto pode executar seu comportamento específico de forma polimórfica:

```csharp
foreach (var animal in zoologico)
{
    animal.EmitirSom();
}
/ZoologicoPOO
│
├── Animal.cs            → Classe abstrata base
├── Mamifero.cs          → Subclasse de Animal
├── Ave.cs               → Subclasse de Animal
├── Leao.cs              → Subclasse de Mamifero
├── Papagaio.cs          → Subclasse de Ave
└── Program.cs           → Classe principal (Main)

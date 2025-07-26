# Estruturas de Controle: Programando Sistemas Dinâmicos e Inteligentes

Dominar as **estruturas de seleção (condicionais)** e **repetição (laços)** é fundamental para criar sistemas de software dinâmicos e responsivos. Este documento explora a aplicação dessas estruturas em dois cenários distintos: um sistema de automação residencial inteligente e um gerenciador de fila de atendimento virtual, ambos projetados para reforçar a lógica de controle e a tomada de decisões em tempo real.

---

## Cenário 1: Sistema de Automação Residencial Inteligente

No contexto de uma casa inteligente, um sistema precisa ajustar o ambiente (iluminação, climatização) e a segurança com base em condições como a presença de pessoas, horários e detecção de movimento.

### Funcionalidades Principais do Sistema Residencial:

* **Detecção de Ambiente:** Identifica o estado do ambiente (dia/noite, presença de pessoas, portas/janelas abertas) para guiar suas ações.
* **Controle de Iluminação:**
    * **Durante o dia:** Luzes permanecem apagadas se houver claridade natural.
    * **À noite:** Luzes são acesas automaticamente em ambientes com presença.
    * **Em caso de saída:** Todas as luzes são desligadas.
* **Ajuste de Climatização:**
    * **Com pessoas em casa:** O ar-condicionado é ligado se a temperatura ambiente estiver acima de um limite pré-definido.
    * **Casa vazia:** O ar-condicionado é desligado para economizar energia.
* **Monitoramento de Segurança:**
    * **Se um sensor de porta/janela detectar abertura indevida:** Um alerta é emitido.
    * **Em caso de movimento detectado à noite em área externa:** Holofotes de segurança são ativados.

### Como Executar o Sistema Residencial (Exemplo Conceitual):

Este é um cenário conceitual, mas um script Python (`automacao_casa.py`) poderia simular as condições:

1.  Certifique-se de ter o **Python 3** instalado.
2.  Imagine um arquivo `automacao_casa.py` no seu diretório.
3.  Execute no terminal:
    ```bash
    python automacao_casa.py
    ```
    A saída mostraria as condições simuladas (ex: "É noite, há pessoas em casa") e as ações tomadas pelo sistema (ex: "Luzes da sala acesas", "Ar-condicionado ligado").

---

## Cenário 2: Gerenciador de Fila de Atendimento Virtual

Este desafio simula um sistema de recepção para um evento ou serviço, focando no registro, listagem e controle de pessoas em uma fila virtual. Ele reforça o uso de estruturas **`if`** e **`while`**, além de manipulação de listas e validações lógicas.

### Funcionalidades Principais do Gerenciador de Fila:

* **Menu Interativo:** Exibe opções para adicionar pessoas à fila, listar a fila ou encerrar o atendimento.
* **Entrada na Fila com Verificação:** Solicita o nome da pessoa, mas impede a adição de nomes vazios ou repetidos na fila.
* **Listagem Formatada:** Mostra a lista numerada de pessoas na fila ou uma mensagem apropriada se a fila estiver vazia.
* **Encerramento Seguro:** O sistema só encerra quando o usuário explicitamente escolhe a opção de sair.

### Exemplo de Execução do Sistema de Fila:Bem-vindo ao sistema de gerenciamento de fila!

Escolha uma opção:
1 - Adicionar pessoa à fila
2 - Listar fila
3 - Sair
Digite o número da opção desejada: 1
Digite o nome da pessoa: Carlos
Carlos adicionado(a) à fila com sucesso!

Escolha uma opção:
1 - Adicionar pessoa à fila
2 - Listar fila
3 - Sair
Digite o número da opção desejada: 2

Fila atual:

Carlos
### Como Executar o Sistema de Fila:

1.  Salve o código em um arquivo chamado `gerenciador_fila.py`.
2.  Execute no terminal:
    ```bash
    python gerenciador_fila.py
    ```

# Estruturas de Controle: Programando Sistemas Dinâmicos e Inteligentes

Dominar as estruturas de seleção (condicionais) e repetição (laços) é fundamental para criar sistemas de software dinâmicos e responsivos. Este documento explora a aplicação dessas estruturas em dois cenários distintos: um sistema de automação residencial inteligente e um gerenciador de fila de atendimento virtual, ambos projetados para reforçar a lógica de controle e a tomada de decisões em tempo real.

---

## Cenário 1: Sistema de Automação Residencial Inteligente

No contexto de uma casa inteligente, um sistema precisa ajustar o ambiente (iluminação, climatização) e a segurança com base em condições como a presença de pessoas, horários e detecção de movimento.

### Funcionalidades Principais do Sistema Residencial

- **Detecção de Ambiente**  
  Identifica o estado do ambiente (dia/noite, presença de pessoas, portas/janelas abertas) para guiar suas ações.

- **Controle de Iluminação**  
  - Durante o dia: luzes permanecem apagadas se houver claridade natural.  
  - À noite: luzes são acesas automaticamente em ambientes com presença.  
  - Em caso de saída: todas as luzes são desligadas.

- **Ajuste de Climatização**  
  - Com pessoas em casa: o ar-condicionado é ligado se a temperatura ambiente estiver acima de um limite pré-definido.  
  - Casa vazia: o ar-condicionado é desligado para economizar energia.

- **Monitoramento de Segurança**  
  - Se um sensor de porta/janela detectar abertura indevida: um alerta é emitido.  
  - Em caso de movimento detectado à noite em área externa: holofotes de segurança são ativados.

### Como Simular o Sistema

Este é um cenário conceitual, mas um script Python (`automacao_casa.py`) poderia simular as condições:

1. Certifique-se de ter o **Python 3** instalado.
2. Crie um arquivo chamado `automacao_casa.py`.
3. Execute no terminal:

```bash
python automacao_casa.py


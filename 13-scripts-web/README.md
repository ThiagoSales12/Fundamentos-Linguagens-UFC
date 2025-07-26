# Organização Automática de Arquivos: O Poder das Linguagens de Script

**Linguagens de script** como Python e JavaScript são ferramentas poderosas para automação de tarefas, manipulação de dados e desenvolvimento rápido. Diferente de linguagens compiladas focadas em performance bruta, o objetivo aqui é a produtividade do desenvolvedor e a facilidade de interação com o sistema operacional.

Um problema comum que muitos de nós enfrentamos é a desorganização da pasta de "Downloads", que se acumula com dezenas de arquivos de todos os tipos. Este desafio apresenta um **script Python** simples, mas de grande impacto, que automatiza o processo de organização, movendo cada arquivo para uma subpasta correspondente ao seu tipo.

---

## A Organização de Arquivos Inteligente

O script em Python escaneia um diretório de origem (a pasta a ser organizada, como "Downloads") e move os arquivos para um diretório de destino, criando subpastas categorizadas automaticamente. Essa abordagem deixa o diretório organizado, facilitando o acesso aos arquivos.

### Funcionalidades Principais:

* **Mapeamento de Extensões:** O script utiliza um dicionário que relaciona extensões de arquivo (ex: `.jpg`, `.pdf`, `.zip`) a nomes de pastas de destino (ex: "Imagens", "Documentos", "Arquivos Compactados"), permitindo uma categorização clara.
* **Criação Automática de Pastas:** Antes de mover qualquer arquivo, o script verifica se a pasta de destino para aquela categoria já existe. Se não existir, ele a cria dinamicamente.
* **Movimentação Segura:** Utiliza o módulo `shutil` do Python para mover os arquivos, garantindo a integridade dos dados durante o processo.
* **Relatório Detalhado de Ações:** Ao final da execução, o script exibe um sumário claro de quantos arquivos foram movidos e para quais categorias, além de listar os arquivos que não foram classificados.

---

## Como Executar o Script

Para ver o organizador de arquivos em ação:

* **Preparação das Pastas:** O script é projetado para ser simples. Ele irá criar automaticamente as pastas `origem` e `destino` no mesmo local onde o script for executado, caso elas ainda não existam.
* **Adicione os Arquivos:** Coloque alguns arquivos de diferentes tipos (ex: `.txt`, `.jpg`, `.pdf`, `.zip`, `.exe`) dentro da pasta `origem` que foi criada.

    **Execute o Script:** Abra seu terminal ou prompt de comando, navegue até o diretório onde o script está salvo e execute o seguinte comando:

    ```bash
    python organizador_de_arquivos.py
    ```

    O script irá mover os arquivos da pasta `origem` para subpastas categorizadas dentro da pasta `destino` e exibirá um relatório detalhado no console, informando as ações realizadas.

---

## Conclusão

Este desafio demonstra o poder e a simplicidade das linguagens de script para resolver problemas práticos de automação do dia a dia. Com poucas linhas de Python e o uso de módulos nativos como `os` e `shutil`, foi possível criar uma ferramenta útil que economiza tempo e ajuda a manter o sistema de arquivos organizado.

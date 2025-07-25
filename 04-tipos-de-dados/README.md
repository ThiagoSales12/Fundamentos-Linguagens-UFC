# Comparação de Tipagem: Python, C# e JavaScript

No universo da programação, entender os **sistemas de tipagem** é tão crucial quanto dominar a sintaxe.  
É a base que garante desde a clareza do código até a robustez das aplicações.

Este documento compara os modelos de tipagem de três linguagens populares — **Python, C# e JavaScript** — detalhando como cada uma define, verifica e lida com tipos de dados, além das garantias de segurança que oferecem.

---

## 📌 Os Modelos de Tipagem em Destaque

As linguagens se diferenciam principalmente por dois critérios:

- **Momento da verificação de tipo**:
  - **Estática:** durante a compilação
  - **Dinâmica:** durante a execução

- **Rigor da conversão de tipos**:
  - **Forte:** conversões automáticas são raras ou inexistentes
  - **Fraca:** conversões automáticas são frequentes

---

## 🐍 Python: Tipagem Dinâmica e Forte

- **Paradigma:** Dinâmico + Forte  
- **Verificação:** Em tempo de execução  
- **Declaração de Variáveis:** Implícita, baseada no valor atribuído  
- **Coerção:** Sempre explícita  
- **Segurança:** Alta, devido à restrição de coerções implícitas

### Exemplo:

```python
x = 10         # x é um inteiro
print(type(x)) # <class 'int'>

x = "texto"    # x agora é uma string
print(type(x)) # <class 'str'>

# Gera TypeError:
# y = 5 + "3"


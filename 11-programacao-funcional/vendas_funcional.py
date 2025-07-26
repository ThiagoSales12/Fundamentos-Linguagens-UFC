vendas = [
    {"produto": "Notebook", "valor": 2500.0, "data": "2025-07-20"},
    {"produto": "Mouse", "valor": 80.0, "data": "2025-07-21"},
    {"produto": "Monitor", "valor": 1200.0, "data": "2025-07-21"},
    {"produto": "Teclado", "valor": 150.0, "data": "2025-07-22"},
    {"produto": "Cabo HDMI", "valor": 35.0, "data": "2025-07-22"},
]

def filtrar_vendas_minimas(vendas, valor_minimo):
    return list(filter(lambda v: v["valor"] >= valor_minimo, vendas))

def extrair_valores(vendas):
    return list(map(lambda v: v["valor"], vendas))

def soma_recursiva(valores):
    if not valores:
        return 0
    return valores[0] + soma_recursiva(valores[1:])

def calcular_total_vendas(vendas, valor_minimo):
    vendas_filtradas = filtrar_vendas_minimas(vendas, valor_minimo)
    valores_filtrados = extrair_valores(vendas_filtradas)
    return soma_recursiva(valores_filtrados)

if __name__ == "__main__":
    valor_minimo = 100.0
    total = calcular_total_vendas(vendas, valor_minimo)
    print(f"Total das vendas acima de R${valor_minimo:.2f}: R${total:.2f}")

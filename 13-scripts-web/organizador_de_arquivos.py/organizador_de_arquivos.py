import os
import shutil

extensoes = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documentos': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],
    'Compactados': ['.zip', '.rar', '.7z'],
    'Executáveis': ['.exe', '.msi'],
    'Vídeos': ['.mp4', '.mkv', '.avi'],
    'Música': ['.mp3', '.wav', '.flac']
}

PASTA_ORIGEM = 'downloads_a_organizar'
PASTA_DESTINO = 'downloads_organizados'

os.makedirs(PASTA_ORIGEM, exist_ok=True)
os.makedirs(PASTA_DESTINO, exist_ok=True)

relatorio = {}

for nome_arquivo in os.listdir(PASTA_ORIGEM):
    caminho_origem = os.path.join(PASTA_ORIGEM, nome_arquivo)

    if os.path.isfile(caminho_origem):
        _, extensao = os.path.splitext(nome_arquivo)
        categoria_encontrada = False

        for categoria, lista_extensoes in extensoes.items():
            if extensao.lower() in lista_extensoes:
                pasta_categoria = os.path.join(PASTA_DESTINO, categoria)
                os.makedirs(pasta_categoria, exist_ok=True)
                shutil.move(caminho_origem, os.path.join(pasta_categoria, nome_arquivo))
                relatorio[categoria] = relatorio.get(categoria, 0) + 1
                categoria_encontrada = True
                break

        if not categoria_encontrada:
            pasta_outros = os.path.join(PASTA_DESTINO, 'Outros')
            os.makedirs(pasta_outros, exist_ok=True)
            shutil.move(caminho_origem, os.path.join(pasta_outros, nome_arquivo))
            relatorio['Outros'] = relatorio.get('Outros', 0) + 1

# Exibe o relatório final
print("\nRelatório de Organização:")
for categoria, quantidade in relatorio.items():
    print(f"- {categoria}: {quantidade} arquivo(s) movido(s)")

if not relatorio:
    print("Nenhum arquivo encontrado para organizar.")

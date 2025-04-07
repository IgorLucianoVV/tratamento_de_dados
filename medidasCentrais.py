import pandas as pd
import re
import statistics
from collections import Counter

# Lê o arquivo original
with open("q6tratado", "r", encoding="utf-8") as f:
    linhas = f.readlines()

# Remove entradas "indefined"
dados_filtrados = [linha.strip() for linha in linhas if linha.strip().lower() != 'indefined']

# Contagem de frequência dos processadores
contagem = Counter(dados_filtrados)

# Transforma o Counter em uma lista com repetições
lista_expandida = []
for nome, freq in contagem.items():
    lista_expandida.extend([nome] * freq)

# Moda (pode ter mais de uma)
moda = statistics.multimode(lista_expandida)
mediana = statistics.median(lista_expandida)

# Média das frequências (frequência média dos nomes)
media_freq = statistics.mean(contagem.values())

# Frequência da(s) moda(s)
print("📊 Estatísticas baseadas em NOME dos processadores:")
for m in moda:
    print(f"Moda: {m} — aparece {contagem[m]} vezes")

print(f"Mediana (nome central): {mediana}")
print(f"Média de repetições (frequência média dos nomes): {media_freq:.2f}")

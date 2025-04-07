import pandas as pd
import re
import time
import statistics

# Configurações
CAMINHO_ARQUIVO = "dados_q6.csv"
ARQUIVO_SAIDA = "valoresCentrias"

# Armazena os tempos
tempos_leitura = []
tempos_escrita = []

# Repetir 30 vezes
for _ in range(5):
    inicio_leitura = time.time()

    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    dados_filtrados = [linha.strip() for linha in linhas if linha.strip().lower() != 'indefined']

    regex = re.compile(r"(?P<Fabricante>\w+)\s+(?P<Linha>\w+)\s+(?:(?P<Modelo>\w+)\s+)?(?P<Versao>\d+)?")

    tratados = []
    for linha in dados_filtrados:
        match = regex.match(linha)
        if match:
            tratados.append(match.groupdict())
        else:
            tratados.append({
                "Fabricante": None,
                "Linha": None,
                "Modelo": None,
                "Versao": None
            })

    df = pd.DataFrame(tratados)
    fim_leitura = time.time()
    tempos_leitura.append(fim_leitura - inicio_leitura)

    inicio_escrita = time.time()
    df.to_csv(ARQUIVO_SAIDA, index=False)
    fim_escrita = time.time()
    tempos_escrita.append(fim_escrita - inicio_escrita)

# Estatísticas leitura
media_leitura = statistics.mean(tempos_leitura)
moda_leitura = statistics.mode(tempos_leitura)
mediana_leitura = statistics.median(tempos_leitura)

# Estatísticas escrita
media_escrita = statistics.mean(tempos_escrita)
moda_escrita = statistics.mode(tempos_escrita)
mediana_escrita = statistics.median(tempos_escrita)

# Exibe resultados
print("📊 Estatísticas - Leitura")
print(f"Média:   {media_leitura:.6f} s")
print(f"Moda:    {moda_leitura:.6f} s")
print(f"Mediana: {mediana_leitura:.6f} s")

print("\n📊 Estatísticas - Escrita")
print(f"Média:   {media_escrita:.6f} s")
print(f"Moda:    {moda_escrita:.6f} s")
print(f"Mediana: {mediana_escrita:.6f} s")

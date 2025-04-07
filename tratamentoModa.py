import pandas as pd
import statistics

# Caminho do arquivo
CAMINHO_ARQUIVO = "dados_q7.csv"

# Lê os dados
df = pd.read_csv(CAMINHO_ARQUIVO)


print("Colunas no CSV:", df.columns.tolist())

# Verifica valores únicos antes do tratamento
print("\nValores únicos antes do tratamento:")
print(df["Nome_Processador"].value_counts())


df["Nome_Processador"] = df["Nome_Processador"].str.strip().replace("indefined", None)

# Calcula a moda (valor mais frequente) ignorando nulos
moda_categoria = df["Nome_Processador"].mode()[0]

# Substitui valores ausentes pela moda
df["Nome_Processador"].fillna(moda_categoria, inplace=True)

# Frequência da nova moda
frequencia_moda = (df["Nome_Processador"] == moda_categoria).sum()

# Resultado
print("\n📊 Análise após tratamento:")
print("Abordagem estatística mais adequada: Moda (valor mais frequente)")
print(f"Categoria mais frequente: {moda_categoria}")
print(f"Frequência da moda: {frequencia_moda}")

# Salva os dados tratados em um novo arquivo
df.to_csv("dados_q7_tratado.csv", index=False)

import pandas as pd

# Dados de exemplo
df = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "nome": ["Ana", "Bruno", "Carlos", "Daniela"],
    "idade": [28, 35, 22, 41],
    "cidade": ["Belo Horizonte", "Paracatu", "Goiânia", "São Paulo"]
})

# Salvar em Parquet
df.to_parquet("exemplo_dados.parquet", index=False)

print("Arquivo criado com sucesso!")
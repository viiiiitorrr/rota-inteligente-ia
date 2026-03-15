# Rota Inteligente - Simulação de Otimização de Entregas

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Dados simulados de entregas (coordenadas x e y)
dados = {
    "x": [2, 3, 5, 8, 7, 6, 1, 4, 9, 3],
    "y": [3, 7, 6, 4, 8, 2, 5, 9, 1, 4]
}

df = pd.DataFrame(dados)

# Número de entregadores / clusters
k = 3

# Aplicando K-Means
kmeans = KMeans(n_clusters=k, random_state=42)
df["cluster"] = kmeans.fit_predict(df[["x", "y"]])

# Centros dos clusters
centros = kmeans.cluster_centers_

print("Entregas agrupadas por zona:")
print(df)

# Plotagem dos resultados
plt.scatter(df["x"], df["y"], c=df["cluster"])
plt.scatter(centros[:, 0], centros[:, 1], marker="X", s=200)

plt.title("Agrupamento Inteligente de Entregas (K-Means)")
plt.xlabel("Coordenada X")
plt.ylabel("Coordenada Y")

plt.show()

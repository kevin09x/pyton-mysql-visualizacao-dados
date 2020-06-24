# Visualização de dados em Python


import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]

título = "Scatterplot: Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.title(título)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x, y, color="k", linestyle="-.")
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=200)
plt.legend()
plt.show()

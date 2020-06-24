# Boxplot - diagrama de caixa
import matplotlib.pyplot as plt
import random

vetor = []

for i in range(10000):
    numeros_aleatorio = random.randint(0, 10000)
    vetor.append(numeros_aleatorio)

plt.boxplot(vetor)
plt.title("Boxplot", color="#FF8C10")
plt.show()

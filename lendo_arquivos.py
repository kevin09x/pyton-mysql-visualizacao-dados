manipulador = open('arquivo.txt', 'r')
print("\nMetodo Read:\n")

primeira_linha = manipulador.readline()

print(primeira_linha is int)

manipulador.close()

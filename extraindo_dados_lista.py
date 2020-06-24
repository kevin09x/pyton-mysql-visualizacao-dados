valores = list()
while True:
  valores.append(int(input('Digite um valor: ')))
  resp = str(input('Quer continuar? [S/N] '))
  if resp in 'Nn':
    break
print('-=' * 31)
print(f'Você digitou {len(valores)} elementos.')  
valores.sort(reverse=True)
print(f'Os valores em ordem decrecente são {valores}')
if 5 in valores:
  print('o valor 5 faz parte da lista')
else:
  print('o valor 5 não faz parte da lista!')  
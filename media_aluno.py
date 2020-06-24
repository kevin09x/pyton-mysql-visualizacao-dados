from time import sleep as tempo
from media_aluno_defs import *
print('\n' * 1)
titulo()
tempo(1.1)
print('\n' * 1)
linha()
subtitilo()
linha()
print('\n' * 1)

nome = str(
    input('\033[32mInsira o seu nome\033[34m(a)\033[m\033[32m: \033[m \033[m')).upper()
print('\n' * 1)

nota1 = float(
    input(f"\033[33mDigite a primeira nota do aluno {nome}\033[m\033[34m: \033[m"))
nota2 = float(
    input(f"\033[33mDigite a segunda nota do aluno {nome}\033[m\033[34m: \033[m"))
nota3 = float(
    input(f"\033[33mDigite a terceira nota do aluno {nome}\033[m\033[34m: \033[m"))
nota4 = float(
    input(f"\033[33mDigite a quarta nota do aluno {nome}\033[m\033[34m: \033[m"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(
    f"\033[34mTirando {nota1}, {nota2}, {nota3}, {nota4} a média é {media}, {nome} você está... \033[m")
print('\n' * 4)

tempo(2)
if media < 6.9:
    print(
        f'\033[4;33m               REPROVADO! \033[m \n \033[32m \n             <<<- ESTUDE MAIS {nome} ->>>')

elif media >= 7:
    print(
        f'\033[4;33m               APROVADO! \033[m \n \033[32m\n               <<<- PARABÉNS {nome} ->>> \n')

elif media == 6:
    print(
        f'\033[4;33m               Você está RECUPERAÇÀO! \033[m \n \033[31m\n              <<<- QUASE-LÁ {nome} ->>>')
print('\n' * 1)


print('\n' * 1)

linha()

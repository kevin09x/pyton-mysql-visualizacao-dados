from menu_python_defs import *
from time import sleep as time

# passei 14m parado voltei de 12:14

line()
print('\t' * 1)
titulo_menu()
line()

resp = print(input('''
╔═══════════ MENU OPÇÕES════════════════════╗
║   1 - Remover Usuarios da lista.          ║
║   2 - Mostrar todos os Usuários.          ║
║   3 - Atualizar o Usuario da lista.       ║
║   4 - Sair do sistema.                    ║
╚═══════════════════════════════════════════╝
'''))

if resp == 1

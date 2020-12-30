from arquivos import grava_txt, lista_txt
from datetime import datetime

def menu():
    print('-' * 20 + '\nOlist \n\n 1)Marketplace\n', '2) Categoria\n', '3) subcategoria\n',
          '4) Cadastrar Marketplace\n', '5) Sair\n')

    op = int(input('Selecione uma opção: '))
    return op


def lista_(itens):
    for i in range(len(itens)):
        print('{}){}'.format(i + 1, itens[i]))


while True:

    op = menu()
    if op == 1:
        lista_(lista_txt('txt/marketplace.txt'))
    elif op == 2:
        lista_(lista_txt('txt/categorias.txt'))
    elif op == 3:
        lista_(lista_txt('txt/subcategorias.txt'))
    elif op == 4:
        nome = input('Inserir Marketplace:')
        grava_txt('txt/marketplace.txt', nome, 'a')
        grava_txt('txt/log_acesso.txt', f'marketplace.txt acessado em: {datetime.now().strftime("%b %d %Y %H:%M:%S")} para gravar o dado : {nome}', 'a')
    elif op == 5:
        exit(0)
    else:
        print('Opção indisponível. Tente novamente.')

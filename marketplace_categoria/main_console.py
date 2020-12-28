from arquivos import grava_txt, lista_txt


def menu():
    print('-' * 20 + '\nOlist \n\n 1)Marketplace\n', '2) Categoria\n', '3) subcategoria\n', '4) Sair\n')

    op = int(input('Selecione uma opção: '))
    return op


def lista_(itens):
    for i in range(len(itens)):
        print('{}){}'.format(i + 1, itens[i]))

    es = int(input('Selecione uma opção: '))
    return es


while True:

    op = menu()
    if op == 1:
        # grava_txt('txt/marketplace.txt','Cem')
        lista_(lista_txt('txt/marketplace.txt'))
    elif op == 2:
        lista_(lista_txt('txt/categorias.txt'))
    elif op == 3:
        lista_(lista_txt('txt/subcategorias.txt'))
    elif op == 4:
        exit(0)
    else:
        print('Opção indisponível. Tente novamente.')

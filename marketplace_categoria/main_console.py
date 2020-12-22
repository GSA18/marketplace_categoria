import listas

def menu():
    print('-'*20 +'\nOlist \n\n 1)Marketplace\n', '2) Categoria\n','3) subcategoria\n','4) Sair\n')

    op = int(input('Selecione uma opção: '))
    return op

while True:
     
       op = menu()
       if op == 1:
         print(marketpalce_lista)
       elif op == 2:
         print(categoria_lista)
       elif op == 3:
         print(subcategoria_lista) 
       elif op == 4:
           exit(0)
       else:
        print('Opção indisponível. Tente novamente.')

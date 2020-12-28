def lista_txt(cam: str) -> list:
    list_aux = []
    arquivo = open(cam, 'r')

    for linha in arquivo:

        linha = linha.strip()
        list_aux.append(linha.encode('iso-8859-1').decode('utf-8'))

    arquivo.close()

    return list_aux

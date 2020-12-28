from datetime import datetime


def lista_txt(cam: str) -> list:
    list_aux = []
    arquivo = open(cam, 'r')

    for linha in arquivo:
        linha = linha.strip()
        list_aux.append(linha.encode('iso-8859-1').decode('utf-8'))

    arquivo.close()
    cam_aux = cam.split('/')
    dado_aux = f'{cam_aux[1]} acessado em :{datetime.now().strftime("%c")}'
    grava_txt('txt/log_acesso.txt', dado_aux, 'a')

    return list_aux


def grava_txt(cam: str, dado: str, op: str) -> None:
    arquivo = open(cam, op)
    arquivo.write(f'{dado}\n')
    arquivo.close()

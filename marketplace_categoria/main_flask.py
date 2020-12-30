from flask import Flask, render_template
from arquivos import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    markeplace = {'nome': 'Marketplace', 'rota': '/marketplace'}
    categorias = {'nome': 'Categorias', 'rota': '/categorias'}
    subcategoria = {'nome': 'Subcategorias', 'rota': '/subcategorias'}
    lista = [markeplace, categorias, subcategoria]

    return render_template('index.html', nome='Olist', lista=lista)


@app.route('/marketplace')
def marketplace():
    l_aux = lista_txt('txt/marketplace.txt')
    l_dicionario = []

    for i in l_aux:
        l_dicionario.append({'nome': i, 'rota': '/categorias'})

    return render_template('index.html', nome="Lojas", lista=l_dicionario)


@app.route('/categorias')
def categoria():
    l_aux = lista_txt('txt/categorias.txt')
    l_dicionario = []

    for i in l_aux:
        l_dicionario.append({'nome': i, 'rota': '/subcategorias'})

    return render_template('index.html', nome="Categorias", lista=l_dicionario)


@app.route('/subcategorias')
def sub_categoria():
    l_aux = lista_txt('txt/subcategorias.txt')
    l_dicionario = []

    for i in l_aux:
        l_dicionario.append({'nome': i, 'rota': '/'})

    return render_template('index.html', nome="Subcategorias", lista=l_dicionario)


app.run()

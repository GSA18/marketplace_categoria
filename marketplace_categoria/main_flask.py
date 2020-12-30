from flask import Flask, render_template, request
from arquivos import *

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

markeplace = {'nome': 'Marketplace', 'rota': '/marketplace'}
categorias = {'nome': 'Categorias', 'rota': '/categorias'}
subcategoria = {'nome': 'Subcategorias', 'rota': '/subcategorias'}
castrar_marketpalce = {'nome': 'Cadastro Marketplace', 'rota': '/form_novo_dado'}
lista = [markeplace, categorias, subcategoria, castrar_marketpalce]

@app.route('/')
def index():
    return render_template('index.html', nome='Olist', lista=lista)


@app.route('/form_novo_dado')
def form_novo():
    return render_template('form_novo_dado.html', nome='Cadastro Marketplace')


@app.route('/cadastrar_marketplace')
def cadastro():
    nome_novo = request.args.get('novo_nome')
    grava_txt('txt/marketplace.txt', nome_novo, 'a')
    grava_txt('txt/log_acesso.txt',
              f'marketplace.txt acessado em: {datetime.now().strftime("%b %d %Y %H:%M:%S")} para gravar o dado : {nome_novo}',
              'a')
    return render_template('form_novo_dado.html', nome='Cadastro Marketplace')


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

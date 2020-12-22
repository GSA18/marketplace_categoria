from flask import Flask
from listas import *


app = Flask(__name__)

@app.route('/')
def index():
    h1 = '<h1> Olist </h1>'
    ol = '''
            <ol>
            <li><a href='/marketplace'>Marketplace</a></li>
            <li><a href='/categorias'>Categorias</a></li>
            <li><a href='/subcategorias'>Subcategorias</a></li>
            </ol>
        '''
    return f'{h1} {ol}'

@app.route('/marketplace')
def marketplace():
    l=marketpalce_lista
    h1 = '<h1> Marketpalce </h1>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {l}\n <br/> {voltar}'

@app.route('/categorias')
def categoria():
    l=categoria_lista
    h1 = '<h1> Categorias </h1>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {l}\n <br/> {voltar}'

@app.route('/subcategorias')
def sub_categoria():
    l=subcategoria_lista
    h1 = '<h1> Subcategorias </h1>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {l}\n <br/> {voltar}'


app.run()
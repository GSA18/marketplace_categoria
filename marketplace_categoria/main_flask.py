from flask import Flask, render_template
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
    l1 = marketpalce_lista
    return render_template('index.html', list_header="Lojas", lista=l1, cam='/categorias', titulo='Lojas')


@app.route('/categorias')
def categoria():
    l2 = categoria_lista
    return render_template('index.html', list_header="Categorias", lista=l2, cam='/subcategorias', titulo='Categorias')


@app.route('/subcategorias')
def sub_categoria():
    l3 = subcategoria_lista
    return render_template('index.html', list_header="Subcategorias", lista=l3, cam='/', titulo='Subcategorias')


app.run()

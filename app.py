# Importa a classe Flask do pacote flask
from flask import Flask, render_template

# Criar instacia da aplicação Flask
app = Flask(__name__)

# Define a rota
@app.route('/')
def ola_mundo():
    return render_template('pagina_inicial.html')

@app.route('/sobre')
def sobre():
    return '<h1>Esta é minha primeira aplicação Flask</h1><p>Estamos aprendendo a criar rotas</p>'

@app.route('/ajuda')
def ajuda():
    return '<h1>Página de ajuda</h1>'

@app.route('/ola/<nome>')
def ola_nome(nome):
    return f'<h1>Olá, {nome}!</h1> <p>Seja bem vindo(a)!<p>'


@app.route('/usuarios')
def lista_usuarios():
    usuarios = ['Ana', 'Isa', 'Maria', 'Noah', 'Luana']
    return render_template('usuarios.html', lista_de_usuarios=usuarios)




if __name__ == '__main__':
    # Inicia o servidor de desenvolvimento Flask
    app.run(debug=True) 



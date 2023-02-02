"""from app import app

from flask import request, render_template

#Raiz - home page - INDEX.HTML
@app.route("/", methods=['GET'])
def homepage():
    return render_template('index.html')

#login - LOGIN.HTML
@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')

#cadastro - FORMCLI.HTML
@app.route("/signin", methods=['GET'])
def signin():
    return render_template('formCli.html')

#autenticação -
@app.route("/autentica", methods=['POST'])
def autentica():
    usr =  request.form['usuario']
    psw = request.form['senha']
    return render_template('formCli.html', usuario=usr, senha=psw)


#página do cliente - USUARIO.HTML
@app.route("/cliente", methods=['POST'])
def cliente():
    return render_template('usuario.html')"""
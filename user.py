from app import app
from flask import request, render_template

#Raiz - home page - INDEX.HTML
@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


#login e cadastro - LOGIN.HTML
@app.route("/login", methods=['GET'])
def login():
    return render_template('login.html')


#autenticação -
@app.route("/autentica", methods=['POST'])
def autentica():
    usr = request.form['Login']
    psw = request.form['senha']
    return render_template('login.html', usuario=usr, senha=psw)


#página do cliente - USUARIO.HTML
@app.route("/participante", methods=['POST'])
def participante():
    return render_template('participante.html')
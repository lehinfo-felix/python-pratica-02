from flask import Blueprint, render_template

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def index():
    return render_template("index.html", page_title='Início')

@routes_bp.route("/cadastro")
def cadastro():
    return render_template("cadastro.html", page_title='Cadastro de usuários')

@routes_bp.route("/sobre")
def sobre():
    return render_template("sobre.html", page_title='Sobre o sistema')

@routes_bp.route("/login")
def login():
    return render_template("login.html", page_title='Perfil de administrador')

@routes_bp.route("/sucesso")
def sucesso():
    return render_template("sucesso.html", page_title='Perfil de administrador')

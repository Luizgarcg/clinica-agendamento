import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return "Clínica funcionando!"


@app.route("/pacientes")
def pacientes():
    con = sqlite3.connect("clinica.db")
    conx = con.cursor()
    conx.execute("select * from paciente")
    lista = conx.fetchall()
    con.close()
    return render_template("pacientes.html", pacientes=lista)

@app.route("/pacientes/novo")
def novo_paciente():
    return render_template("novo_paciente.html")


app.run(debug=True)

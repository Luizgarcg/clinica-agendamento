import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("inicio.html")


@app.route("/pacientes")
def pacientes():
    con = sqlite3.connect("clinica.db")
    conx = con.cursor()
    conx.execute("select * from paciente")
    lista = conx.fetchall()
    con.close()
    return render_template("pacientes.html", pacientes=lista)


@app.route("/pacientes/novo", methods=["GET", "POST"])
def novo_paciente():
    if request.method == "POST":
        nome = request.form["nome"]
        telefone = request.form["telefone"]
        idade = request.form["idade"]
        con = sqlite3.connect("clinica.db")
        conx = con.cursor()
        conx.execute(
            "insert into paciente(nome,telefone,idade) values(?,?,?)",
            (nome, telefone, idade),
        )
        con.commit()
        con.close()
        return redirect("/pacientes")
    return render_template("novo_paciente.html")


@app.route("/medicos")
def medicos():
    con = sqlite3.connect("clinica.db")
    conx = con.cursor()
    conx.execute("select * from medico")
    lista = conx.fetchall()
    con.close()
    return render_template("medicos.html", medicos=lista)


@app.route("/medicos/novo", methods=["GET", "POST"])
def novo_medico():
    if request.method == "POST":
        nome = request.form["nome"]
        especialidade = request.form["especialidade"]
        con = sqlite3.connect("clinica.db")
        conx = con.cursor()
        conx.execute(
            "insert into medico(nome,especialidade) values(?,?)",
            (nome, especialidade),
        )
        con.commit()
        con.close()
        return redirect("/medicos")
    return render_template("novo_medico.html")


@app.route("/consultas")
def consultas():
    con = sqlite3.connect("clinica.db")
    conx = con.cursor()
    conx.execute(
        "select c.id, p.nome, m.nome, c.dia, c.horario from consulta c join paciente p on c.id_paciente = p.id join medico m on c.id_medico = m.id order by c.dia, c.horario"
    )
    lista = conx.fetchall()
    con.close()
    return render_template("consultas.html", consultas=lista)


@app.route("/consultas/nova", methods=["GET", "POST"])
def nova_consulta():
    con = sqlite3.connect("clinica.db")
    conx = con.cursor()
    if request.method == "POST":
        id_paciente = request.form["id_paciente"]
        id_medico = request.form["id_medico"]
        dia = request.form["dia"]
        horario = request.form["horario"]
        conx.execute(
            "insert into consulta(id_paciente, id_medico, dia, horario) values(?,?,?,?)",
            (id_paciente, id_medico, dia, horario),
        )
        con.commit()
        con.close()
        return redirect("/consultas")
    conx.execute("select id, nome from paciente")
    lista_pacientes = conx.fetchall()
    conx.execute("select id, nome, especialidade from medico")
    lista_medicos = conx.fetchall()
    con.close()
    return render_template(
        "nova_consulta.html", pacientes=lista_pacientes, medicos=lista_medicos
    )


app.run(debug=True)

import sqlite3
con = sqlite3.connect('clinica.db')
conx = con.cursor()

def cadastrar_paciente():
  nome = input('nome: ')
  telefone = input('telefone: ')
  idade = int(input('idade: '))
  conx.execute("insert into paciente(nome,telefone,idade) values(?,?,?)", (nome, telefone, idade))
  con.commit()
  print('Paciente cadastrado com sucesso!', nome)

def cadastrar_medico():
  nome_medico = input("nome do medico: ")
  especialidade = input("especialidade: ")
  conx.execute("insert into medico(nome,especialidade) values(?,?)", (nome_medico, especialidade))
  con.commit()
  print('Medico cadastrado com sucesso!', nome_medico)

def procurar():
  conx.execute("select * from paciente")
  pacientes = conx.fetchall()
  for paciente in pacientes:
    print("ID:", paciente[0], "| Nome:", paciente[1], "| Telefone:", paciente[2], "| Idade:", paciente[3])

def listar_medico():
  conx.execute("select * from medico")
  medicos = conx.fetchall()
  for medico in medicos:
    print("ID:", medico[0], "| Nome:", medico[1], "| Especialidade:", medico[2])

def agendar_consulta():
  paciente_id = int(input("Digite o ID do paciente: "))
  medico_id = int(input("Digite o ID do médico: "))
  dia = input("Digite o dia (YYYY-MM-DD): ")
  horario = input("Digite o horário (ex: 14:30): ")
  conx.execute(
    "insert into consulta(id_paciente, id_medico, dia, horario) values(?,?,?,?)",
    (paciente_id, medico_id, dia, horario)
  )
  con.commit()
  print("Consulta agendada com sucesso!")

def listar_consultas():
  conx.execute(
    "select c.id, p.nome, m.nome, c.dia, c.horario from consulta c join paciente p on c.id_paciente = p.id join medico m on c.id_medico = m.id"
  )
  consultas = conx.fetchall()
  for consulta in consultas:
    print("ID:", consulta[0], "| Paciente:", consulta[1], "| Médico:", consulta[2], "| Dia:", consulta[3], "| Horário:", consulta[4])

def buscar_consulta_por_paciente():
  paciente_id = int(input("Digite o ID do paciente: "))
  conx.execute(
    "select c.id, p.nome, m.nome, c.dia, c.horario from consulta c join paciente p on c.id_paciente = p.id join medico m on c.id_medico = m.id where p.id = ?",
    (paciente_id,)
  )
  consultas = conx.fetchall()
  for consulta in consultas:
    print("ID:", consulta[0], "| Paciente:", consulta[1], "| Médico:", consulta[2], "| Dia:", consulta[3], "| Horário:", consulta[4])

while True:
  print("1 - cadastrar paciente")
  print("2 - cadastrar médico")
  print("3 - procurar pacientes")
  print("4 - procurar médicos")
  print("5 - agendar consulta")
  print("6 - listar consultas")
  print("7 - buscar consulta por paciente")
  print("8 - sair")
  opcao = int(input("escolha uma opção: "))
  if opcao == 1:
    cadastrar_paciente()
  elif opcao == 2:
    cadastrar_medico()
  elif opcao == 3:
    procurar()
  elif opcao == 4:
    listar_medico()
  elif opcao == 5:
    agendar_consulta()
  elif opcao == 6:
    listar_consultas()
  elif opcao == 7:
    buscar_consulta_por_paciente()
  elif opcao == 8:
    break
  else:
    print("opção inválida!")

con.commit()
con.close()
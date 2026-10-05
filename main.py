import sqlite3
con = sqlite3.connect('clinica.db')
conx = con.cursor()
def cadastrar_paciente():
  nome = input('nome: ')
  telefone = input('telefone: ')
  idade = int(input('idade: '))
  conx.execute("insert into paciente(nome,telefone,idade) values(?,?,?)",(nome,telefone,idade))
  print('Paciente cadastrado com sucesso!',nome)

def cadastrar_medico():
  nome_medico = input("nome do medico: ")
  especialidade = input("especialidade: ")
  conx.execute("insert into medico(nome,especialidade) values(?,?)", (nome_medico, especialidade))
  print('Medico cadastrado com sucesso!', nome_medico)
  
def procurar():
    conx.execute("select * from paciente")
    pacientes = conx.fetchall()
    for paciente in pacientes:
        print(f"ID: {paciente[0]}, Nome: {paciente[1]}, Telefone: {paciente[2]}, Idade: {paciente[3]}")
def listar_medico():
    conx.execute("select * from medico")
    medicos = conx.fetchall()
    for medico in medicos:
        print(f"ID: {medico[0]}, Nome: {medico[1]}, Especialidade: {medico[2]}")

while True:
   print("1 - cadastrar paciente")
   print("2 - cadastrar médico")
   print("3 - procurar pacientes")
   print("4 - procurar médicos")
   print("5 - sair")
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
       break
   else:
       print("opção inválida!")

con.commit()
con.close()

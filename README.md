# Clínica Agendamento

Sistema de agendamento de consultas para uma clínica médica, feito em Python com banco de dados SQLite. Tem duas versões: uma no **terminal** e uma **web** com Flask, HTML e CSS.

## Funcionalidades

- Cadastro e listagem de pacientes
- Cadastro e listagem de médicos
- Agendamento de consultas ligando paciente e médico
- Listagem de consultas mostrando os nomes (JOIN entre as tabelas)
- Versão terminal: busca de consultas por paciente

## Tecnologias

- Python
- SQLite (módulo `sqlite3`)
- Flask
- HTML e CSS

## Modelo do banco

Três tabelas ligadas por chave estrangeira:

- `paciente` (id, nome, telefone, idade)
- `medico` (id, nome, especialidade)
- `consulta` (id, id_paciente, id_medico, dia, horario)

## Como rodar

1. Clone o repositório e entre na pasta:

```
git clone https://github.com/Luizgarcg/clinica-agendamento.git
cd clinica-agendamento
```

2. Crie e ative o ambiente virtual (Windows):

```
python -m venv venv
venv\Scripts\activate
```

3. Instale o Flask:

```
python -m pip install flask
```

4. Crie o banco e as tabelas:

```
python banco.py
```

5. Escolha a versão:

**Terminal**

```
python main.py
```

**Web**

```
python app.py
```

Depois abra `http://127.0.0.1:5000` no navegador.

## Estrutura

```
clinica-agendamento/
  banco.py        cria o banco e as tabelas
  main.py         versão terminal (menu)
  app.py          versão web (Flask)

from datetime import datetime, timedelta

funcionarios = [{
    "Nome": "Isabel das Neves",
    "Especialidades":["Cirurgia e Traumatologia","Ortodontia"],
    "Status": "Disponível",
    "Agendamentos":[{
        "Paciente":"Bruno Soares",
        "Especialista": "Isabel das Neves",
        "Especialidade": "Ortodontia",
        "Atendimento": "Particular",
        "Tipo": "Primeira Consulta",
        "Data": datetime(2026,7,18,14),
    }] 
    },
    {
    "Nome": "Janaína Soares",
    "Especialidades":["Odontopediatria","Odontologia Estética"],
    "Status": "Disponível",
    "Agendamentos":[]
    },
    {
    "Nome": "Danilo Xavier",
    "Especialidades":["Estomatologia", "Periodontia"],
    "Status": "Disponível",
    "Agendamentos":[]
    },
    {
    "Nome": "Antônio Mendes",
    "Especialidades":["Implantodontia","Radiologia odontológica e imaginologia"],
    "Status": "Disponível",
    "Agendamentos":[]
    },       
]

clientes = [{
    "Nome":"Roberto de Almeida",
    "Consultas":[
        {"Especialidade":"Odontologia Estética",
    "Status": "Concluído", "Valor": 150}]
    },
    {
    "Nome":"Cristiano Nogueira",
    "Consultas": []
    },
    {
    "Nome":"David França",
    "Consultas": [{"Especialidade":"Estomatologia",
    "Status": "Concluído", "Valor": 300},
    {"Especialidade":"Ortodontia",
    "Status": "Andamento", "Valor": 150}]
    },
    {
    "Nome":"Silvana Menezes",
    "Consultas": [{"Especialidade":"Odontologia Estética",
    "Status": "Concluído", "Valor": 200}]
    },
]

especialidades = ["Cirurgia e Traumatologia","Ortodontia","Odontopediatria","Odontologia Estética",\
 "Estomatologia", "Periodontia", "Implantodontia","Radiologia odontológica e imaginologia"]

valores = {"Cirurgia e Traumatologia": 300,
    "Ortodontia": 150,
    "Odontopediatria": 200,
    "Odontologia Estética": 200,
    "Estomatologia": 300,
    "Periodontia": 180,
    "Implantodontia": 300,
    "Radiologia odontológica e imaginologia":100}
from datetime import datetime, timedelta
from dados import funcionarios, clientes, especialidades, valores
from agendamento import agendamento_consultas

menu_art = """
----- CLÍNICA ODONTOLÓGICA -----

1- Especialistas
2- Clientes
3- Agendamento de Consultas
0- Sair

"""

especialistas_art = """

----- ESPECIALISTAS -----

1- Cadastrar
2- Editar
3- Listar
4- Remover
0- Sair

"""

status_art = ("""
    ------ DEFINIR STATUS ------
    1- Disponível
    2- Afastado/Desligado/Suspenso
    """)

clientes_art = """

----- CLIENTES -----

1- Cadastrar
2- Editar
3- Listar
4- Remover
0- Sair

"""

agendamento_art = """

----- Agendamento -----

1- Cadastrar
2- Editar
3- Listar
4- Remover
0- Sair

"""

def definir_especialidades():
    escolhas = []
    for i in range(8):
        print(f"{i+1}- {especialidades[i]}")
    while True:
        try:
            index = (int(input("Digite o Número da Especialidade que deseja adicionar: ")) - 1)
        except ValueError:
            print("Escreva um valor válido")
        else:
            if index >=0 and index < 8:
                if especialidades[index] in escolhas:
                    print("Você já adicionou essa especialidade")
                else:
                    escolhas.append(especialidades[index])
            else:
                print("Digite um número entre 1 e 8")
                continue
        opcao = input("Deseja adicionar mais especialidades? (Enter para continuar adicionando ou Qualquer tecla para cancelar)")
        if opcao == "":
            continue
        else:
            break
    return escolhas

def definir_status():
    while True:
        print(status_art)
        status = 0
        try:
            status = int(input("Escolha o número do tipo de status: "))
        except ValueError:
            print("Digite um valor válido!")
        else:
            if status == 1:
                status = "Disponível"
                break
            elif status == 2:
                status = "Afastado/Desligado/Suspenso"
                break
            else:
                print("Digite 1 ou 2")
    return status

def cadastro_funcionarios():
    nome_adicionar = input("Qual o nome do especialista?")
    escolhas = definir_especialidades()
    especialidades_adicionar = escolhas
    status_adicionar = definir_status()
    funcionario = {"Nome": nome_adicionar,
    "Especialidades": escolhas,
    "Status": status_adicionar,
    "Agendamentos":[],
    }
    funcionarios.append(funcionario)
    print("Funcionário Cadastrado com sucesso!")

def editar_funcionarios():
    while True:
        for pessoa in funcionarios:
            print(pessoa["Nome"])
        nome = input("Qual o nome da pessoa que você deseja modificar? ")
        
        cont = 0
        for pessoa in funcionarios:
            if nome == pessoa["Nome"]:
                cont = 1
                print("""
                ----- Editar -----

                1- Nome
                2- Especialidades
                3- Status
                0- Sair
                
                """)
                try:
                    opcao = int(input())
                except ValueError:
                    print("Valor digitado não é aceito.")
                else:
                    if opcao > 0 and opcao <= 4:
                        if opcao == 1:
                            novo_nome = input("Novo nome: ")
                            pessoa["Nome"] = novo_nome
                            break
                        elif opcao == 2:
                            nova_escolha = definir_especialidades()
                            pessoa["Especialidades"] = nova_escolha
                            break
                        elif opcao == 3:
                            novo_status = definir_status()
                            pessoa["Status"] = novo_status
                            break
                    elif opcao == 0:
                        print("Saindo...")
                        break       
        if cont == 0:
            print("Nome não encontrado. Tente Novamente")
        break

def listar_funcionarios():
    for funcionario in funcionarios:
        print(f"""
        Nome: {funcionario["Nome"]}
        Especialidades: {funcionario["Especialidades"]}
        Status: {funcionario["Status"]}
        """)
        for consulta in funcionario["Agendamentos"]:
            i = 0
            print(f"""
            Agendamentos:
            Paciente: {funcionario["Agendamentos"][i]["Paciente"]}
            Especialista: {funcionario["Agendamentos"][i]["Especialista"]}
            Especialidade: {funcionario["Agendamentos"][i]["Especialidade"]}
            Atendimento: {funcionario["Agendamentos"][i]["Atendimento"]}
            Tipo: {funcionario["Agendamentos"][i]["Tipo"]}
            Data: {funcionario["Agendamentos"][i]["Data"]}
            """)
            i += 1

def remover_funcionarios():
    for pessoa in funcionarios:
            print(pessoa["Nome"])
    nome = input("Nome: ")
    cont = 0
    for pessoa in funcionarios:
        if pessoa["Nome"] == nome:
            cont = 1
            funcionarios.remove(pessoa)
            break
    if cont == 0:
        print("Nome não encontrado...")
    else:
        print(f"Ficha deletada com sucesso!")

def menu_especialista():
    while True:
        print(especialistas_art)
        try:
            opcao = int(input())
        except ValueError:
            print("O valor digitado não é aceito")
        else:
            if opcao == 1:
                cadastro_funcionarios()
            elif opcao == 2:
                editar_funcionarios()
            elif opcao == 3:
                listar_funcionarios()
            elif opcao == 4:
                remover_funcionarios()
            elif opcao == 0:
                break
            else:
                print("Comando inválido! Por favor, tente digitar um número entre 0 e 4")

def cadastro_clientes():
    nome_adicionar = input("Qual o nome do cliente?")
    cliente = {"Nome": nome_adicionar,
    "Consultas":[]
    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")

def editar_clientes():
    while True:
        for pessoa in clientes:
            print(pessoa["Nome"])
        nome = input("Qual o nome da pessoa que você deseja modificar? ")
        
        cont = 0
        for pessoa in clientes:
            if nome == pessoa["Nome"]:
                cont = 1
                print("""
                ----- Editar -----

                1- Nome
                0- Sair
                
                """)
                try:
                    opcao = int(input())
                except ValueError:
                    print("Valor digitado não é aceito.")
                else:
                    if opcao == 1:
                            novo_nome = input("Novo nome: ")
                            pessoa["Nome"] = novo_nome
                            break
                    elif opcao == 0:
                        print("Saindo...")
                        break       
        if cont == 0:
            print("Nome não encontrado. Tente Novamente")
        break

def listar_clientes():
    for cliente in clientes:
        print(f"""
        Nome: {cliente["Nome"]}
        Consultas:
        """)
        for consulta in cliente["Consultas"]:
            print(f"""
            Especialidade: {consulta["Especialidade"]}
            Status: {consulta["Status"]}
            Valor: R${consulta["Valor"]},00
            """)

def remover_clientes():
    for pessoa in clientes:
            print(pessoa["Nome"])
    nome = input("Nome: ")
    cont = 0
    for pessoa in clientes:
        if pessoa["Nome"] == nome:
            cont = 1
            clientes.remove(pessoa)
            break
    if cont == 0:
        print("Nome não encontrado...")
    else:
        print("Ficha deletada com sucesso!")

def menu_clientes():
    while True:
        print(clientes_art)
        try:
            opcao = int(input())
        except ValueError:
            print("O valor digitado não é aceito")
        else:
            if opcao == 1:
                cadastro_clientes()
            elif opcao == 2:
                editar_clientes()
            elif opcao == 3:
                listar_clientes()
            elif opcao == 4:
                remover_clientes()
            elif opcao == 0:
                break
            else:
                print("Comando inválido! Por favor, tente digitar um número entre 0 e 4")

def menu():
    opcao = 1
    while opcao != 0:
        print(menu_art)
        while True:
            try:
                opcao = int(input())
            except ValueError:
                print("O valor digitado não é aceito")
            else:
                if opcao >= 0 and opcao <= 3:
                    break
                else:
                    print("Digite um valor entre 0 e 3")
        if opcao == 1:
            menu_especialista()
        elif opcao == 2:
            menu_clientes()
        elif opcao == 3:
            agendamento_consultas()
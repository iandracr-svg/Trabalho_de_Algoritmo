from dados import funcionarios, clientes, especialidades, valores
from datetime import datetime, timedelta

agendamento_art = """

----- Agendamento -----

1- Cadastrar
2- Editar
3- Listar
4- Remover
0- Sair

"""
atraso = 50
desconto_1_consulta = 50
desconto_convenio = 30

def definir_data():
    while True:
        try:
            mes = int(input("Mês: "))
            dia = int(input("Dia: "))
            print("Horários Possíveis: 8,9,10,11,14,15,15,17")
            hora = int(input("Hora: "))

            if hora not in [8,9,10,11,14,15,15,17]:
                print("Horário indisponível!")
            else:
                data = datetime(2026, mes, dia, hora, 0 )
                return data
        except ValueError:
            print("Alguma das informações está errada. Tente novamente")

def definir_preco(especialidade,atendimento,tipo,atraso):
    valor = valores[especialidade]
    if atendimento == "Convenio":
        valor = valor - desconto_convenio
    if tipo == "Retorno":
        valor = 0
    else:
        valor -= desconto_1_consulta
    if atraso == True:
        valor += atraso
    return valor


def cadastro_agendamento():
    while True:
        # Agendamento de qual cliente?
        for pessoa in clientes:
            print(pessoa["Nome"])
        # (Atribuição de Variável)
        nome = input("Qual o nome da pessoa que você deseja adiconar uma consulta? ")
        # Esse Cliente existe? (Verificação)
        cont = 0
        for pessoa in clientes:
            if nome == pessoa["Nome"]:
                cont = 1
                paciente_adicionar = nome
                break
        if cont == 0:
            print("Nome não encontrado...")
            break
        # Qual é a especialidade procurada? (Verificação)
        for i in range(8):
            print(f"{i+1}- {especialidades[i]}")
        while True:
            try:
                index = (int(input("Especialidade: ")) - 1)
            except ValueError:
                print("Escreva um valor válido")
            else:
                if index >=0 and index < 8:
                        # Definir a especialidade (Atribuição de Variável)
                        especialidade = especialidades[index]
                        break
                else:
                    print("Digite um número entre 1 e 8")
                    continue
        # Tem alguem disponível com essa especialidade?
        escolhas = []
        for especialista in funcionarios:
            if especialista["Status"] == "Disponível":
                for especialidade in especialista["Especialidades"]:
                    if especialidade == especialidades[index]:
                        escolhas.append(especialista["Nome"])
        if len(escolhas) == 0:
            print("Não há nenhum funcionário disponível no momento.")
            break
        for i in range(len(escolhas)):
            print(f"{i+1}- {escolhas[i]}")
        # Se tiver, quais as opções de profissionais disponíveis?
        while True:
            try:
                index = (int(input("Especialista: ")) - 1)
            except ValueError:
                print("Digite um valor válido")
                continue
            except IndexError:
                print("Digite um valor dentro das escolhas apresentadas.")
                continue
            else:
                # Definir o especialista escolhido: (Atribuição de variáveis)
                nome_especialista = escolhas[index]
                i = 0
                for especialista in funcionarios:
                    if nome_especialista == especialista["Nome"]:
                        especialista = nome_especialista
                        index_especialista = i
                        break
                    i+=1
                break

        # Mostrar horários ocupados
        print("Horários Ocupados:")
        for consulta in funcionarios[index_especialista]["Agendamentos"]:
            print(consulta["Data"])
        # Verificar se o horário digitado está disponível
        while True:
            ocupado = False
            data = definir_data()
            for consulta in funcionarios[index_especialista]["Agendamentos"]:
                if consulta["Data"] == data:
                    ocupado = True
                    break
                if ocupado == True:
                    print("Esse horário não está disponível para esse profissional.")
                else:
                    break
            break
                    

        # Definir o tipo do atendimento
        print("""
        ----- ATENDIMENTO -----
        1- Convenio
        2- Particular
        """)
        while True:
            try:
                opcao = int(input())
            except ValueError:
                print("O valor digitado é inválido")
            else:
                if opcao == 1:
                    atendimento = "Convenio"
                    break
                elif opcao == 2:
                    atendimento = "Particular"
                    break
                else:
                    print("Digite 1 ou 2.")

        # Definir o tipo da consulta
        print("""
        ----- TIPO DA CONSULTA -----
        1- Primeira Consulta
        2- Retorno
        """)
        while True:
            try:
                opcao = int(input())
            except ValueError:
                print("O valor digitado é inválido")
            else:
                if opcao == 1:
                    tipo = "Primeira Consulta"
                    break
                elif opcao == 2:
                    tipo = "Retorno"
                    break
                else:
                    print("Digite 1 ou 2.")

        # Tem atraso ou n
        print("""
        ----- ATRASO -----
        1- Sim
        2- Não
        """)
        while True:
            try:
                opcao = int(input())
            except ValueError:
                print("O valor digitado é inválido")
            else:
                if opcao == 1:
                    atraso = True
                    break
                elif opcao == 2:
                    atraso = False
                    break
                else:
                    print("Digite 1 ou 2.")
        valor = definir_preco(especialidade,atendimento,tipo,atraso)
        agendamento = {
        "Paciente": nome,
        "Especialista": especialista,
        "Especialidade": especialidade,
        "Atendimento": atendimento,
        "Tipo": tipo,
        "Data": data,
        }
        funcionarios[index_especialista]["Agendamentos"].append(agendamento)

        consulta_adiconar = {"Especialidade": especialidade,
        "Status": "Agendado", "Valor": valor}
        for cliente in clientes:
            if cliente["Nome"] == nome:
                cliente["Consultas"].append(consulta_adiconar)
                break
        break
            
def listar_agendamento():
    # Verificar Agendamento de qual cliente?
    for pessoa in clientes:
        print(pessoa["Nome"])
    # (Atribuição de Variável)
    nome = input("Qual o nome da pessoa que você deseja listar as consultas? ")
    # Esse Cliente existe? (Verificação)
    cont = 0
    for pessoa in clientes:
        if nome == pessoa["Nome"]:
            cont = 1
            break
    continuar = True
    if cont == 0:
        print("Nome não encontrado...")
        continuar = False
    if continuar == False:
        return
    for pessoa in clientes:
        if pessoa["Nome"] == nome:
            for consulta in pessoa["Consultas"]:
                print(f"""
                Especialidade: {consulta["Especialidade"]}
                Status: {consulta["Status"]}
                Valor: {consulta["Valor"]}
                """)
            break
    return
    

def remover_agendamento():
    # Remover Agendamento de qual cliente?
    for pessoa in clientes:
        print(pessoa["Nome"])
    # (Atribuição de Variável)
    nome = input("Qual o nome da pessoa que você deseja listar as consultas? ")
    # Esse Cliente existe? (Verificação)
    cont = 0
    for pessoa in clientes:
        if nome == pessoa["Nome"]:
            cont = 1
            cliente = pessoa
            break
    continuar = True
    if cont == 0:
        print("Nome não encontrado...")
        continuar = False
        if continuar == False:
            return
    print(f"""
    {pessoa["Nome"]}

    Consultas:
    """)
    i = 0
    for consulta in pessoa["Consultas"]:
        print(f"""
        {i+1}- 
                Especialidade: {consulta["Especialidade"]}
                Status: {consulta["Status"]}
                Valor: {consulta["Valor"]}

        """)
        i += 1
    try:
        indice = int(input()) - 1
    except ValueError:
        print("Digite um número válido")
        return
    if indice < 0 or indice >= len(cliente["Consultas"]):
        print("Consulta inexistente")
        return
    del cliente["Consultas"][indice]
    print("Consulta removida com sucesso")

def editar_agendamento():
    # Mostrar clientes
    for pessoa in clientes:
        print(pessoa["Nome"])
    # Escolher cliente
    nome = input("Qual o nome da pessoa que deseja editar a consulta? ")
    cont = 0
    for pessoa in clientes:
        if pessoa["Nome"] == nome:
            cont = 1
            cliente = pessoa
            break
    if cont == 0:
        print("Nome não encontrado...")
        return
    # Verificar se possui consultas
    if len(cliente["Consultas"]) == 0:
        print("Esse cliente não possui consultas.")
        return
    # Mostrar consultas
    for i in range(len(cliente["Consultas"])):
        consulta = cliente["Consultas"][i]
        print(f"""
        {i+1}-
        Especialidade: {consulta["Especialidade"]}
        Status: {consulta["Status"]}
        Valor: {consulta["Valor"]}
        """)
    # Escolher consulta
    while True:
        try:
            index = int(input("Qual consulta deseja editar? ")) - 1
        except ValueError:
            print("Digite um número válido.")
        else:
            if index >= 0 and index < len(cliente["Consultas"]):
                break
            else:
                print("Consulta inválida.")
    # Menu de edição
    print("""
    ----- EDITAR CONSULTA -----
    1- Status
    2- Valor
    0- Cancelar
    """)
    while True:
        try:
            opcao = int(input())
        except ValueError:
            print("Digite um número válido.")
        else:
            if opcao == 1:
                print("""
                ----- STATUS ----
                1- Agendada
                2- Em Andamento
                3- Concluído
                4- Cancelado
                """)
                while True:
                    try:
                        status = int(input("Novo status: "))
                    except ValueError:
                        print("Digite um número válido.")
                    else:
                        if status == 1:
                            cliente["Consultas"][index]["Status"] = "Agendada"
                            break
                        elif status == 2:
                            cliente["Consultas"][index]["Status"] = "Em Andamento"
                            break
                        elif status == 3:
                            cliente["Consultas"][index]["Status"] = "Concluído"
                            break
                        elif status == 4:
                            cliente["Consultas"][index]["Status"] = "Cancelada"
                            break
                        else:
                            print("Escolha um número entre 1 e 4.")
            elif opcao == 2:
                while True:
                    try:
                        novo_valor = int(input("Novo valor: "))
                    except:
                        print("Digite um número inteiro")
                    else:
                        cliente["Consultas"][index]["Valor"] = novo_valor
                        break
            elif opcao == 0:
                return
            else:
                print("Escolha entre 0 e 2.")

    print("Consulta editada com sucesso!")

def agendamento_consultas():
    while True:
        print(agendamento_art)
        try:
            opcao = int(input())
        except ValueError:
            print("O valor digitado não é aceito")
        else:
            if opcao == 1:
                cadastro_agendamento()
            elif opcao == 2:
                editar_agendamento()
            elif opcao == 3:
                listar_agendamento()
            elif opcao == 4:
                remover_agendamento()
            elif opcao == 0:
                break
            else:
                print("Comando inválido! Por favor, tente digitar um número entre 0 e 4")
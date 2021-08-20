import pyodbc
import funcoesInserir as ins
import funcoesDeletar
import funcoesAtualizar
import funcoesConsultar as con
import funcoesRelacoes as rel

def retornar_conexão():#LEMBRAR DE TROCAR
    server  = "DAN-KATH\SQLEXPRESS"
    database = "YDTransporte"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    return pyodbc.connect(string_conexao)

inicio = True
print('----Bem Vindo ao Banco de Dados - YD Transporte---')
while inicio:
    acao = int(input('O que você deseja fazer?\n Digite 1 - Para inserir novos dados\n Digite 2 - Para deletar dados\n Digite 3 - Para atualizar dados\n Digite 4 - Para relaizar consultas gerais\n Digite 5 - Para realizar consultas pré-definidas\n Digite 6 - Para finalizar\n Digite sua escolha: '))
    conexao = retornar_conexão()
    if acao == 1:
        acao2 = int(input('\nO que você deseja fazer?\n Digite 1 - Para inserir nova filial\n Digite 2 - Para inserir novo cliente\n Digite 3 - Para inserir novo aluno\n Digite 4 - Para inserir nova escola\n Digite 5 - Para inserir novo empregado\n Digite 6 - Para inserir novo veículo\n Digite 7 - Para inserir novo contrato (Filial-Cliente)\n Digite 8 - Para inserir novo transporte (Escola-Veículo)\n Digite 9 - Para voltar ao menu anterior\n Digite sua escolha: '))
        if acao2 == 1:
            inserir = ins.inserirFilial(conexao)
            print(inserir)
        elif acao2 == 2:
            inserir = ins.inserirCliente(conexao)
            print(inserir)
        elif acao2 == 3:
            inserir = ins.inserirAluno(conexao)
            print(inserir)
        elif acao2 == 4:
            inserir = ins.inserirEscola(conexao)
            print(inserir)
        elif acao2 == 5:
            inserir = ins.inserirEmpregado(conexao)
            print(inserir)
        elif acao2 == 6:
            inserir = ins.inserirVeiculo(conexao)
            print(inserir)
        elif acao2 == 7:
            inserir = ins.inserirContrato(conexao)
            print(inserir)
        elif acao2 == 8:
            inserir = ins.inserirTransporte(conexao)
            print(inserir)
        else:
            pass
    if acao == 4:
        acao4 = int(input('\nO que você deseja fazer?\n Digite 1 - Para mostrar a relação de filiais\n Digite 2 - Para mostrar a relação de clientes\n Digite 3 - Para mostrar a relação de alunos\n Digite 4 - Para mostrar a relação de escolas\n Digite 5 - Para mostrar a relação de veiculos\n Digite 6 - Para mostrar a relação de motoristas\n Digite 7 - Para mostrar a relação de empregados\n Digite 8 - Para mostrar a relação de contratos\n Digite 9 - Para mostrar a relação de bairros\n Digite 10 - Para voltar ao menu anterior\n Digite sua escolha: '))
        if acao4 == 1:
            consultar = rel.consultarFilial(conexao)
            print(consultar)
        elif acao4 == 2:
            consultar = rel.consultarClientes(conexao)
            print(consultar)
        elif acao4 == 3:
            consultar = rel.consultarAlunos(conexao)
            print(consultar)
        elif acao4 == 4:
            consultar = rel.consultarEscolas(conexao)
            print(consultar)
        elif acao4 == 5:
            consultar = rel.consultarVeiculos(conexao)
            print(consultar)
        elif acao4 == 6:
            consultar = rel.consultaMotoristas(conexao)
            print(consultar)
        elif acao4 == 7:
            consultar = rel.consultarEmpregados(conexao)
            print(consultar)
        elif acao4 == 8:
            consultar = rel.consultarContratos(conexao)
            print(consultar)
        elif acao4 == 9:
            consultar = rel.consultarBairrosAtendidos(conexao)
            print(consultar)
        else:
            pass
    if acao == 5:
        acao3 = int(input('\nO que você deseja fazer?\n Digite 1 - Para mostrar a quantidade de clientes, alunos e empregados por filial\n Digite 2 - Para mostrar o veículo e o nome do motorista que mais leva alunos\n Digite 3 - Para mostrar a quantidade de alunos por cliente\n Digite 4 - Para mostrar a quantidade de alunos por bairro de residencia\n Digite 5 - Para consultar o nome dos alunos de um determinado cliente\n Digite 6 - Para consultar o número de telefone de um cliente responsável por um determinado aluno\n Digite 7 - Para consultar a quantidade de alunos de um determinado bairro\n Digite 8 - Para consultar a idade de um determinado aluno\n Digite 9 - Para consultar a quantidade de alunos de uma determinada escola\n Digite 10 - Para voltar ao menu anterior\n Digite sua escolha: '))
        if acao3 == 1:
            consultar = con.consultarFilial(conexao)
            print(consultar)
        elif acao3 == 2:
            consultar = con.consultarVeiculoMotorista(conexao)
            print(consultar)
        elif acao3 == 3:
            consultar = con.consultarQntAlunosCliente(conexao)
            print(consultar)
        elif acao3 == 4:
            consultar = con.consultarQntAlunosBairro(conexao)
            print(consultar)
        elif acao3 == 5:
            consultar = con.consultarAlunoPorCliente(conexao)
            print(consultar)
        elif acao3 == 6:
            consultar = con.consultarTelefoneCliente(conexao)
            print(consultar)
        elif acao3 == 7:
            consultar = con.consultarAlunosBairro(conexao)
            print(consultar)
        elif acao3 == 8:
            consultar = con.consultarIdade(conexao)
            print(consultar)
        elif acao3 == 9:
            consultar = con.consultarQntAlunoEscola(conexao)
            print(consultar)
        else:
            pass
    elif acao == 6:
        print("\n----Programa Finalizado - Até a próxima!---")

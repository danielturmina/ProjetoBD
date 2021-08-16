import pyodbc
import funcoesInserir as ins
import funcoesDeletar
import funcoesAtualizar
import funcoesConsultar

def retornar_conexão():#LEMBRAR DE TROCAR
    server  = "DAN-KATH\SQLEXPRESS"
    database = "YDTransporte"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    return pyodbc.connect(string_conexao)

inicio = True
print('----Bem Vindo ao Banco de Dados - YD Transporte---')
while inicio:
    acao = int(input('O que você deseja fazer?\n Digite 1 - Para inserir novos dados\n Digite 2 - Para deletar dados\n Digite 3 - Para atualizar dados\n Digite 4 - Para realizar consultas\n Digite 5 - Para finalizar\n Digite sua escolha: '))
    conexao = retornar_conexão()
    if acao == 1:
        acao2 = int(input('O que você deseja fazer?\n Digite 1 - Para inserir nova filial\n Digite 2 - Para inserir novo cliente\n Digite 3 - Para inserir novo aluno\n Digite 4 - Para inserir nova escola\n Digite 5 - Para inserir novo empregado\n Digite 6 - Para inserir novo veículo\n Digite 7 - Para inserir novo contrato (Filial-Cliente)\n Digite 8 - Para inserir novo transporte (Escola-Veículo)\n Digite 9 - Para voltar ao menu anterior\n Digite sua escolha: '))
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
    elif acao == 5:
        print("Programa Finalizado - Até a próxima!")

import pyodbc
import funcoesInserir as ins
import funcoesDeletar
import funcoesAtualizar
import funcoesConsultar

def retornar_conexão():
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
        acao2 = int(input('O que você deseja fazer?\n Digite 1 - Para inserir novo cliente\n Digite 2 - Para inserir novo aluno\n Digite 3 - Para inserir nova escola\n Digite 4 - Para inserir novo empregado\n Digite 5 - Para inserir novo veículo\n Digite 6 - Para voltar ao menu anterior\n Digite sua escolha: '))
        if acao2 == 5:
            inserir = ins.inserirVeiculo(conexao)
            print(inserir)
            pass
    elif acao == 4: #PARA EPRENDIZADO APENAS
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM aluno")
        linha = cursor.fetchall()
        if linha:
            print(linha)

        print('\n')

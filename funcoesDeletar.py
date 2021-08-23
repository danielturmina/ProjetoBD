import pyodbc

def deletarTelCliente(conexao):
    try:
        numTel = input('Digite o num de telefone que deseja deletar\n')
        cursor = conexao.cursor()
        codigo = "DELETE FROM telefones_cliente WHERE cliente_telefones = '" +numTel+ "'"
        cursor.execute(codigo)
        conexao.commit()
    except:
        print('Você digitou o numero de telefone de maneira incorreta\n')

    return 0

def deletarAluno(conexao):
    try:
        codAluno = input('Digite o código do Aluno que deseja deletar\n')
        cursor = conexao.cursor()
        codigo = "DELETE from aluno where codigo_aluno = '" +codAluno+ "'"
        cursor.execute(codigo)
        conexao.commit()
    except:
        print("Você digitou o código de maneira incorreta\n")

    return 0

def deletarCliente(conexao):
    try:
        cpfCliente = input('Digite o CPF do cliente que deseja deletar\n')
        cursor = conexao.cursor()
        codigo1 = "DELETE from aluno where cpf = '" +cpfCliente+ "'"
        codigo2 = "DELETE from telefones_cliente where cpf = '" +cpfCliente+ "'"
        codigo3 = "DELETE from contrata where cpf = '" +cpfCliente+ "'"
        codigo4 = "DELETE from cliente where cpf = '" +cpfCliente+ "'"
        codigoCompleto = [codigo1, codigo2, codigo3, codigo4]
        for i in codigoCompleto:
            cursor.execute(i)
        conexao.commit()
    except:
        print("Você digitou o CPF de maneira incorreta\n")

    return 0
    


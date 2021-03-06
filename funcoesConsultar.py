import pyodbc

def consultarFilial(conexao):
    try:
        sql = 'exec [dbo].[qntClientesAlunosEmpregados]'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('CNPJ', 'Razão Social', 'Qnt Clientes', 'Qnt Alunos','Qnt Empregados')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarVeiculoMotorista(conexao):
    try:
        sql = 'exec [dbo].[veiculoMotoristaMaisAlunos]'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchone()
        print('\n')
        print("('Placa', 'Modelo', 'Nome do Motorista', 'Sobrenome do Motorista','Qnt Alunos')")
        print(resultado)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarQntAlunosCliente(conexao):
    try:
        sql = 'exec [dbo].[qntAlunosPorCliente]'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('CPF', 'Nome do Cliente', 'Sobrenome do Cliente', 'Qnt Alunos')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarQntAlunosBairro(conexao):
    try:
        sql = 'exec [dbo].[qntAlunosPorBairro]'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('Bairro', 'Município', 'Qnt Alunos')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarAlunoPorCliente(conexao):
    try:
        cpf = input("Digite o CPF do cliente [Formato: 095.038.404-32]: ")
        sql = 'exec [dbo].[nomeDependente] ?'
        cursor = conexao.cursor()
        cursor.execute(sql, cpf)
        resultado = cursor.fetchall()
        print('\n')
        print("('Nome do Aluno', 'Sobrenome do Aluno')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarTelefoneCliente(conexao):
    try:
        codigo = int(input("Digite o código do aluno: "))
        sql = 'SELECT [dbo].[telefoneAluno](?)'
        cursor = conexao.cursor()
        cursor.execute(sql, codigo)
        resultado = cursor.fetchone()
        print('\n')
        if resultado[0] == None:
            print("Não há telefone registrado!")
        else:
            print("Telefone:",resultado[0])
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarAlunosBairro(conexao):
    try:
        nomeBairro = input("Digite o nome do bairro: ")
        sql = 'SELECT [dbo].[qtdAlunoBairro](?)'
        cursor = conexao.cursor()
        cursor.execute(sql, nomeBairro)
        resultado = cursor.fetchone()
        print('\n')
        if resultado[0] == None:
            print("Não há bairro registrado com esse nome!")
        else:
            print("Quantidade de Alunos:",resultado[0])
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarIdade(conexao):
    try:
        codigo = int(input("Digite o código do aluno: "))
        sql = 'SELECT [dbo].[saberIdade](?)'
        cursor = conexao.cursor()
        cursor.execute(sql, codigo)
        resultado = cursor.fetchone()
        print('\n')
        if resultado[0] == None:
            print("Não há aluno com esse código!")
        else:
            print("Idade:",resultado[0],"anos")
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarQntAlunoEscola(conexao):
    try:
        codigo = int(input("Digite o código da escola: "))
        sql = 'SELECT [dbo].[qtdAlunosPorEscola](?)'
        cursor = conexao.cursor()
        cursor.execute(sql, codigo)
        resultado = cursor.fetchone()
        print('\n')
        if resultado[0] == None:
            print("Não há escola com esse código!")
        else:
            print("Quantidade de Alunos:",resultado[0],)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"






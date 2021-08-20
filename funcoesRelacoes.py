def consultarFilial(conexao):
    try:
        sql = 'SELECT * FROM empresa_filial'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('CNPJ', 'Razão Social', 'Município Sede')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarClientes(conexao):
    try:
        sql = 'SELECT * FROM cliente'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('CPF', 'Nome', 'Sobrenome')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarAlunos(conexao):
    try:
        sql = 'SELECT * FROM aluno'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('Codigo', 'Data de Nascimento', 'Codigo Escola', 'Nome', 'Sobrenome', 'Rua', 'Numero', Complemento', 'Bairro', 'Municipio', 'Estado', CEP', 'Placa')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarEscolas(conexao):
    try:
        sql = 'SELECT * FROM escola'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('Codigo Escola', 'Nome', 'Rua', 'Numero', Complemento', 'Bairro', 'Municipio', 'Estado', CEP')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarVeiculos(conexao):
    try:
        sql = 'SELECT * FROM veiculo'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('Placa', Categoria Mínima Exigida', 'Modelo', 'Número Máximo de Lugares', 'Número da CNH Motorista', 'CPF Motorista', 'CNPJ Filial' )")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultaMotoristas(conexao):
    try:
        sql = 'SELECT * FROM motorista'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('CPF', 'Número da CNH', 'Categoria da CNH')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarEmpregados(conexao):
    try:
        sql = 'SELECT * FROM empregado'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('CPF', 'Nome', 'Sobrenome', 'Data de Nascimento', 'CNPJ Filial')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarContratos(conexao):
    try:
        sql = 'SELECT * FROM contrata'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('CNPJ Filia', 'CPF Cliente')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"

def consultarBairrosAtendidos(conexao):
    try:
        sql = 'SELECT * FROM bairros_atend'
        cursor = conexao.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print('\n')
        print("('Bairro Atendido', 'CNPJ Filial')")
        for x in resultado:
            print(x)
        return "--Consulta Realizada com Sucesso!--\n"
    except:
        return "A consulta não pode ser realizada, os dados foram inseridos incorretamente!\n"


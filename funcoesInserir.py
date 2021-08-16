import pyodbc

def inserirCliente(conexao):
    cpf = input("Digite o CPF do cliente [Ex: 095.038.473-04]: ")
    nome = input("Digite o nome do cliente: ")
    sobrenome = input("Digite o sobrenome do cliente: ")
    cnpj = input("Digite o CNPJ da da empresa filial [Ex: 76.419.484/0001-70]: ")
    flag= True
    listaTel = []
    while flag:
        telefone = input("Digite um telefone do cliente [Ex: '(81) 98877-6655']: ")
        teste = input("Deseja inserir mais um telefone para esse cliente ? [s/n]: ")
        listaTel.append(telefone)
        if teste == 's':
            pass
        else:
            flag= False
      
    inserirCliente = '''INSERT INTO cliente VALUES(?,?,?)'''
    inserirContrata = '''INSERT INTO contrata VALUES(?,?)'''
    inserirTelefones = '''INSERT INTO telefones_cliente VALUES(?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserirCliente, cpf,nome,sobrenome)
        cursor.execute(inserirContrata, cnpj, cpf)
        for x in listaTel:
            cursor.execute(inserirTelefones, x, cpf)
        conexao.commit()
        resultado = "Cliente inserido com sucesso!\n"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
    return resultado

def inserirAluno(conexao):
    codigo_aluno = int(input("Digite o código do aluno: "))
    data_nasc = input("Digite a data de nascimento do aluno [Ex: 12/12/2012]: ")
    codigo_escola = int(input("Digite o código da escola:  "))
    cpf_cliente = input("Digite o CPF do cliente [Ex: 095.038.473-04]: ")
    nome = input("Digite o nome do aluno: ")
    sobrenome = input("Digite o sobrenome do aluno: ")
    rua = input("Digite o nome da rua onde o aluno reside: ")
    numero = input("Digite o número da casa/apt onde o aluno reside: ")
    complemento = input("Digite o complemento da casa/apt onde o aluno reside: ")
    bairro = input("Digite o bairro onde o aluno reside: ")
    municipio = input("Digite o município onde o aluno reside: ")
    estado = input("Digite o Estado onde o aluno reside:")
    cep = input("Digite o CEP da onde o aluno reside:")
    placa = input("Digite a Placa [Ex: PCU-7705]: ")
    inserir = '''INSERT INTO aluno VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserir, codigo_aluno, data_nasc, codigo_escola, cpf_cliente, nome, sobrenome, rua, numero, complemento, bairro, municipio, estado, cep, placa)
        conexao.commit()
        resultado = "Aluno inserido com sucesso!\n"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
    return resultado

def inserirEscola(conexao):
    codigo_escola = int(input("Digite o código da escola:  "))
    nome = input("Digite o nome da escola: ")
    rua = input("Digite o nome da rua onde a escola está localizada: ")
    numero = input("Digite o número do imóvel onde a escola está localizada: ")
    complemento = input("Digite o complemento do imóvel onde a escola está localizada: ")
    bairro = input("Digite o bairro onde a escola está localizada: ")
    municipio = input("Digite o município  onde a escola está localizada: ")
    estado = input("Digite o Estado  onde a escola está localizada:")
    cep = input("Digite o CEP da onde a escola está localizada:")
    inserir = '''INSERT INTO escola VALUES(?,?,?,?,?,?,?,?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserir, codigo_escola, nome, rua, numero, complemento, bairro, municipio, estado, cep)
        conexao.commit()
        resultado = "Escola inserida com sucesso!\n"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
    return resultado

def inserirEmpregado(conexao):
    cpf_empregado = input("Digite o CPF do empregado [Ex: 095.038.473-04]: ")
    nome = input("Digite o nome do empregado: ")
    sobrenome = input("Digite o sobrenome do empregado: ")
    data_nasc = input("Digite a data de nascimento do empregado [Ex: 12/12/2012]: ")
    cnpj_filial = input("Digite o CNPJ da empresa filial contratante [Ex: 76.419.484/0001-70]: ")
    flag= True
    listaTel = []
    while flag:
        telefone = input("Digite um telefone do empregado [Ex: '(81) 98877-6655']: ")
        teste = input("Deseja inserir mais um telefone para esse empregado? [s/n]: ")
        listaTel.append(telefone)
        if teste == 's':
            pass
        else:
            flag= False

    tipo_empregado = input("Digite o tipo do empregado:\n Digite 1 - Para Assistente Administrativo\n Digite 2 - Para Motorista\nDigite sua escolha:  ")

    if tipo_empregado == "1":
        inserirEmpregado = '''INSERT INTO empregado VALUES(?,?,?,?,?)'''
        inserirTelefones = '''INSERT INTO telefones_empregado VALUES(?,?)'''
        inserirAssistente = '''INSERT INTO assistente_adm VALUES(?)'''
        cursor = conexao.cursor()
        try:
            cursor.execute(inserirEmpregado, cpf_empregado, nome, sobrenome, data_nasc, cnpj_filial)
            cursor.execute(inserirAssistente, cpf_empregado)
            for x in listaTel:
                cursor.execute(inserirTelefones, x, cpf_empregado)
            conexao.commit()
            resultado = "Empregado inserido com sucesso!\n"
        except:
            resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
        return resultado
        
    elif tipo_empregado == "2":   
        num_cnh = input("Digite o número da CNH do motorista: ")
        categoria = input("Digite a categoria da CNH do motorista [Ex: 'A','B','C','D' ou'E']: ")

        inserirEmpregado = '''INSERT INTO empregado VALUES(?,?,?,?,?)'''
        inserirTelefones = '''INSERT INTO telefones_empregado VALUES(?,?)'''
        inserirMotorista = '''INSERT INTO motorista VALUES(?,?,?)'''
        cursor = conexao.cursor()
        try:
            cursor.execute(inserirEmpregado, cpf_empregado, nome, sobrenome, data_nasc, cnpj_filial)
            cursor.execute(inserirMotorista, cpf_empregado, num_cnh, categoria)
            for x in listaTel:
                cursor.execute(inserirTelefones, x, cpf_empregado)
            conexao.commit()
            resultado = "Empregado inserido com sucesso!\n"
        except:
            resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
        return resultado
    

def inserirVeiculo(conexao): #Eu queria usar o EXECUTE, e retornar exatamente a mensagem de erro, mas ate agora nao consegui
    placa = input("Digite a Placa [Ex: PCU-7705]: ")
    categoria = input("Digite a categoria mínima para dirigí-lo [Ex: A, B, C, D ou E]: ")
    modelo = input("Digite o modelo do veículo: ")
    qnt_lugares = int(input("Digite a quantidade máxima de lugares do veículo: "))
    cnh_motorista = input("Digiteo num da CNH do motorista [Ex: 60768950437]: ")
    cpf_motorista = input("Digite o CPF do motorista [Ex: 095.038.473-04]: ")
    cnpj_filial = input("Digite o CNPJ da da empresa filial [Ex: 76.419.484/0001-70]: ")
    
    inserir = '''INSERT INTO veiculo VALUES(?,?,?,?,?,?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserir, placa, categoria, modelo,qnt_lugares,cnh_motorista,cpf_motorista,cnpj_filial)
        conexao.commit()
        resultado = "Veículo inserido com sucesso!\n"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
    return resultado

def inserirContrato(conexao):
    cpf = input("Digite o CPF do cliente [Ex: 095.038.473-04]: ")
    cnpj = input("Digite o CNPJ da da empresa filial [Ex: 76.419.484/0001-70]: ")
      
    inserirContrata = '''INSERT INTO contrata VALUES(?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserirContrata, cnpj, cpf)
        conexao.commit()
        resultado = "Contrato inserido com sucesso!\n"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
    return resultado

def inserirTransporte(conexao):
    codigo = int(input("Digite o código da escola:  "))
    placa = input("Digite a Placa [Ex: PCU-7705]: ")
      
    inserirTransporte = '''INSERT INTO transporta_para VALUES(?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserirTransporte, codigo, placa)
        conexao.commit()
        resultado = "Transporte inserido com sucesso!\n"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido!\n"
    return resultado
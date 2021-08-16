import pyodbc

def inserirCliente(conexao):
    cpf = input("Digite o CPF do cliente [Ex: 095.038.473-04]: ")
    nome = input("Digite o nome do cliente: ")
    sobrenome = input("Digite o sobrenome do cliente: ")
    cnpj = input("Digite o CNPJ da da emrpesa filiar [Ex: 76.419.484/0001-70]: ")
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
        resultado = "Cliente Inserido com sucesso\n"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido\n"
    return resultado

def inserirAluno():
    return 0

def inserirEscola():
    return 0

def inserirEmpregado():
    return 0

def inserirVeiculo(conexao): #Eu queria usar o EXECUTE, e retornar exatamente a mensagem de erro, mas ate agora nao consegui
    placa = input("Digite a Placa [Ex: PCU-7705]: ")
    categoria = input("Digite a categoria mínima para dirigí-lo [Ex: A, B, C, D ou E]: ")
    modelo = input("Digite o modelo do veículo: ")
    qnt_lugares = int(input("Digite a quantidade máxima de lugares do veículo: "))
    cnh_motorista = input("Digiteo num da CNH do motorista [Ex: 60768950437]: ")
    cpf_motorista = input("Digite o CPF do motorista [Ex: 095.038.473-04]: ")
    cnpj_filial = input("Digite o CNPJ da da emrpesa filial [Ex: 76.419.484/0001-70]: ")
    
    inserir = '''INSERT INTO veiculo VALUES(?,?,?,?,?,?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserir, placa, categoria, modelo,qnt_lugares,cnh_motorista,cpf_motorista,cnpj_filial)
        conexao.commit()
        resultado = "Inserido com sucesso"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido"
    return resultado
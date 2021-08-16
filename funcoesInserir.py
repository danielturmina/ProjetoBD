import pyodbc

def inserirCliente():
    return 0

def inserirAluno():
    return 0

def inserirEscola():
    return 0

def inserirEmpregado():
    return 0

def inserirVeiculo(conexao): #Eu queria usar o EXECUTE, e retornar exatamente a mensagem de erro, mas ate agora nao consegui
    placa = input("Digite a Placa: [Ex: PCU-7705]")
    categoria = input("Digite a categoria mínima para dirigí-lo: [Ex: A, B, C, D ou E]")
    modelo = input("Digite o modelo do veículo: ")
    qnt_lugares = int(input("Digite a quantidade máxima de lugares do veículo: "))
    cnh_motorista = input("Digiteo num da CNH do motorista: [Ex: 60768950437]")
    cpf_motorista = input("Digite o CPF do motorista: [Ex: 095.038.473-04]")
    cnpj_filial = input("Digite o CNPJ da da emrpesa filiar: [Ex: 76.419.484/0001-70]")
    
    inserir = '''INSERT INTO veiculo VALUES(?,?,?,?,?,?,?)'''
    cursor = conexao.cursor()
    try:
        cursor.execute(inserir, placa, categoria, modelo,qnt_lugares,cnh_motorista,cpf_motorista,cnpj_filial)
        conexao.commit()
        resultado = "Inserido com sucesso"
    except:
        resultado = "Inserção não realizada, você inseriu algum dado inválido"
    return resultado
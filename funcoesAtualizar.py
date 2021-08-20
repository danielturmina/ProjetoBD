import pyodbc
def atualizarEnd(conexao, tipo):
    tipoDado = ['código da escola', 'código do aluno', 'CPF do cliente']
    try:
        ponteiro = input(f'Digite o {tipoDado[tipo]} que deseja atualizar\n')
        cursor = conexao.cursor()
        end = [['a rua'],['o numero'], ['o complemento'], ['o bairro'], ['o municipio'], ['estado'], ['o CEP no formato [XX.XXX-XXX]']]

        for i in range(7):
            print(f'Digite {end[int(i)][0]}\n')
            entrada = input('')
            end[i].append(entrada)
        
        dadoFiltrado = tipoDado[tipo].split(' ')
        end.append(ponteiro)
        codigo = "UPDATE "+ dadoFiltrado[2] + " SET rua ='" +end[0][1] + "', numero = '" + end[1][1] + "', complemento = '" + end[2][1] + "', bairro = '" + end[3][1]+ "', municipio = '" + end[4][1] + "', estado = '" + end[5][1] + "', cep = '" + end[6][1] + "' WHERE codigo = '" + end[7] + "'"
        print(codigo)
        cursor.execute(codigo)
        conexao.commit()
    except:
        print('O endereço não pôde ser atualizado\n')

    return 0

def atualizarVeiculoAluno(conexao):
    try:
        codAluno = input('Digite o codigo do aluno que deseja transferir\n')
        numPlaca = input('Digite o novo número de placa no formato [XXX-YYYY]\n')
        cursor = conexao.cursor()
        codigo = "UPDATE aluno SET placa = '" +numPlaca+ "' WHERE codigo_aluno = '" + codAluno + "'"
        cursor.execute(codigo)
        conexao.commit()
    except:
        print('Não foi possível realizar a transferencia do aluno para outro veículo\n')

    return 0

def atualizarEmpregado(conexao):
    try:
        cpfEmpregado = input('Digite o CPF do empregado no formato [XXX.XXX.XXX-XX]\n')
        cnpjEmpresa = input('Digite o novo número de CNPJ [XX.XXX.XXX/XXXX-XX]\n')
        cursor = conexao.cursor()
        codigo = "UPDATE empregado SET cnpj = '" + cnpjEmpresa + "' WHERE cpf = '" + cpfEmpregado + "'"
        cursor.execute(codigo)
        conexao.commit()
    except:
        print('Não foi possível realizar a transferencia do empregado para outra filial\n')

    return 0
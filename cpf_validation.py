def error(error) -> bool:  # definição responsável por retornar os possíveis erros do cpf
    listaError = ('insira apenas numeros', 'o cpf está inválido')
    print(listaError[error])
    return False


class Validate:  # classe responsável por fazer todas validações e calculos necessários para o cpf
    def __init__(self, cpf):  # definição responsável por receber o cpf digitado
        self.cpf = cpf.replace('.', '').replace('-', '').replace('/', '')  # retira caracteres especiais do cpf

    def validCpf(self) -> bool:  # definição responsável por filtrar possíveis erros do cpf
        if self.cpf.isdigit():  # verifica se o cpf tem somente digitos
            pass
        else:
            return error(0)
        if len(self.cpf) == 11:  # verifica se o cpf tem 11 digitos
            pass
        else:
            return error(1)
        if len(set(list(self.cpf))) == 1: # verifica se os numeros do cpf não são repetidos
            return error(1)

    @property
    def verification(self) -> bool:  # definição responsável por todos os calculos
        verificate_Digit1 = False
        verificate_Digit2 = False
        result = 0
        stock = 0
        multiply = 10
        for i in self.cpf[0:9]:  # responsável pela primeira parte do calculo do primeiro digito verificador
            result = int(i) * multiply
            stock += int(result)
            multiply = multiply - 1
        verNumber1 = (stock * 10) % 11  # primeiro calculo de digito verificador
        if verNumber1 == 10:  # caso o resultado do primeiro digito seja 10, troca o mesmo por 0
            verNumber1 = 0
        if (int(self.cpf[9])) == verNumber1:  # verifica se o numero calculado e o primeiro digito verificador coincidem
            verificate_Digit1 = True

        stock = 0
        result = 0
        multiply = 11
        for i in self.cpf[0:10]:  # responsável pela primeira parte do calculo do segundo digito verificador
            result = int(i) * multiply
            stock += int(result)
            multiply = multiply - 1
        verNumber2 = (stock * 10) % 11  # segundo calculo de digito verificador
        if verNumber2 == 10:
            verNumber2 = 0
        if (int(self.cpf[10])) == verNumber2:  # verifica se o numero calculado e o segundo digito verificador coincide
            verificate_Digit2 = True
        if verificate_Digit1 == True and verificate_Digit2 == True:  # verifica se ambos os digitos verificadores coincidiram com seus calculos

            print('o cpf é valido')
            return True
        else:
            return error(1)

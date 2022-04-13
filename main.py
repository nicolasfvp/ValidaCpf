from cpf_validation import Validate

print('bem vindo ao verificador de cpf')
cpf = input('digite seu cpf \n')

validation = Validate(cpf)
validNum = validation.validCpf()
if validNum == None:
    validation.verification


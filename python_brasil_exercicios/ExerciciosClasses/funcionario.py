class Funcionario(object):

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def mostraNome(self):
        print("Nome: ", self.nome)

    def mostraSalario(self):
        print("Salario: ",  self.salario)

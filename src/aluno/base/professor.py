from src.aluno.base.funcionario import Funcionario


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        self.cpf = cpf
        self.nome = nome
        self.classe = classe
        self.cargo = 1
        self.diaria = 3
        self.salario = 0





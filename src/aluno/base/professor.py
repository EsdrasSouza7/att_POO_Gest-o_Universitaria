from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class Professor(Funcionario):

    def __init__(self, cpf: str, nome: str, classe: str):
        self.cpf = cpf
        self.nome = nome
        self.classe = classe
        self.cargo = Tipo.PROF
        self.diaria = 3
        self.salario = 0





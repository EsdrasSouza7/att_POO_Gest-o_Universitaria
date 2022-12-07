from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        self.cpf = cpf
        self.nome = nome
        if nivel > 30:
            self.nivel = 30
        elif nivel >= 1:
            self.nivel = nivel
        else:
            self.nivel = 1
        self.cargo = Tipo.STA
        self.diaria = 1
        self.salario = float(0)
        self.salarioMes = 1

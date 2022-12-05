from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class STA(Funcionario):

    def __init__(self, cpf: str, nome: str, nivel: int):
        self.cpf = cpf
        self.nome = nome
        self.nivel = nivel
        self.cargo = Tipo.STA
        self.diaria = 1

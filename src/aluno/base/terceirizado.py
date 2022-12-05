from src.aluno.base.funcionario import Funcionario
from src.cliente.tipo import Tipo


class Terceirizado(Funcionario):

    def __init__(self, cpf: str, nome: str, insalubre: bool):
        self.cpf = cpf
        self.nome = nome
        self.insalubre = insalubre
        self.cargo = Tipo.TERC
        self.diaria = 0

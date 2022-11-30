from src.aluno.base.funcionario import Funcionario
from src.cliente.irh_service import IRHService


class RHService(IRHService):
    def __init__(self):
        self.funcio = []

    def cadastrar(self, funcionario: Funcionario):
        for fun in self.funcio:
            if fun.getCpf() == funcionario.getCpf():
                print("Pessoa ja existente")
                return False
        self.funcio.append(funcionario)
        return True

    def remover(self, cpf: str):
        for fun in self.funcio:
            if fun.getCpf() == cpf:
                self.funcio.remove(fun)
                return True
        print("pessoa não encontrada!")
        return False

    def obterFuncionario(self, cpf: str):
        for fun in self.funcio:
            if fun.getCpf() == cpf:
                return fun
        print("Não Encontrado")
        return None

    def getFuncionarios(self):
        return self.funcio

    def getFuncionariosPorCategorias(self, tipo):
        temp = []
        for fun in self.funcio:
            if fun.cargo == tipo.value:
                temp.append(fun)
        return temp

    def getTotalFuncionarios(self):
        a = len(self.funcio)
        return a

    def solicitarDiaria(self, cpf: str):
        return False

    def partilharLucros(self, valor: float):
        return False

    def iniciarMes(self):
        pass

    def calcularSalarioDoFuncionario(self, cpf: str):
        return None

    def calcularFolhaDePagamento(self):
        return 0

from src.aluno.base.funcionario import Funcionario
from src.cliente.irh_service import IRHService
from src.aluno.base.terceirizado import Terceirizado
from src.cliente.tipo import Tipo


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
    #colocar os nomes em ordem alfabetica
    def getFuncionariosPorCategorias(self, tipo):
        temp = []
        for fun in self.funcio:
            if fun.cargo == tipo.value:
                temp.append(fun)
        return temp
    #Colocar todos os nomes em ordem alfabetica

    def getTotalFuncionarios(self):
        return len(self.funcio)

    def solicitarDiaria(self, cpf: str):
        funcionario = Terceirizado('0', 'None', False)
        for fun in self.funcio:
            if fun.getCpf() == cpf:
                funcionario = fun
        if funcionario.getQtdDiaria() > 0:
            funcionario.salario += 100
            funcionario.diaria -= 1
            return True
        else:
            return False


    def partilharLucros(self, valor: float):
        numfuncionarios = self.getTotalFuncionarios()
        if numfuncionarios == 0:
            return False
        else:
            lucros = valor/numfuncionarios
            for fun in self.funcio:
                fun.salario += lucros
            return True

    def iniciarMes(self):
        for fun in self.funcio:
            if fun.cargo == Tipo.PROF:
                fun.diaria = 3
            elif fun.cargo == Tipo.STA:
                fun.diaria = 1
            elif fun.cargo == Tipo.TERC:
                fun.diaria = 0

    def calcularSalarioDoFuncionario(self, cpf: str):
        fun = self.obterFuncionario(cpf)
        if fun.cargo == Tipo.PROF: #funcional
            if fun.getClasse() == "A":
                print('Test')



    def calcularFolhaDePagamento(self):
        return 0

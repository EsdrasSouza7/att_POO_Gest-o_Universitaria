from src.aluno.base.professor import Professor
from src.aluno.base.sta import STA
from src.aluno.manager.rh_service import RHService
from src.cliente.tipo import Tipo

preof = Professor("8945654", "Esdras", "E")
sta = STA("8798787", "AAA", 2)
rh = RHService()
rh.cadastrar(preof)
rh.cadastrar(sta)
print(rh.solicitarDiaria("8945654")) # diaria +100
print(rh.solicitarDiaria("123456"))
print(rh.calcularSalarioDoFuncionario("8945654")) # salario +11000
print(rh.calcularSalarioDoFuncionario('8798787'))


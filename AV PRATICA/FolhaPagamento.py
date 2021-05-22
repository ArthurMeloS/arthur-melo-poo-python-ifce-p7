from FolhaMovimento import FolhaMovimento
from Movimento import Movimento
from Colaborador import Colaborador

class FolhaPagamento:

    def __init__(self, mes, totalDescontos, totalProventos, ano):
        self.mes = mes
        self.totalDescontos = totalDescontos
        self.totalProventos = totalProventos
        self.ano = ano
        self.movimentos = []
        self.colaboradores = []

    # Questão 8 - Resposta
    def calcularFolha(self):
        for movimento in self.movimentos:
            if movimento.Movimento == Movimento.P:
                self.totalProventos += movimento.valor
            elif movimento.Movimento == Movimento.D:
                self.totalDescontos += movimento.valor

        totalSalarios = 0
        for colaborador in self.colaboradores:
            totalSalarios += colaborador.salarioAtual

        totalPagamento = (totalSalarios + self.totalProventos) - self.totalDescontos
        print('Total de Salários = {} Total de Proventos = {} Total de Descontos = {} Total a Pagar = {}'.format(totalSalarios, self.totalProventos, self.totalDescontos, totalPagamento))


    def inserirMovimentos(self, mov):
        if type(mov) == FolhaMovimento:
            self.movimentos.append(mov)

    def inserirColaboradores(self, colaborador : Colaborador):
        self.colaboradores.append(colaborador)
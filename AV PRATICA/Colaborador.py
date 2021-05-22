from FolhaMovimento import FolhaMovimento
from Movimento import Movimento


class Colaborador:

    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salarioAtual):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.bairro = bairro
        self.cep = cep
        self.cpf = cpf
        self.salarioAtual = salarioAtual
        self.movimentos = []

    # Questão 9 - Resposta
    def calcularSalario(self):
        totalProventos = 0.0
        totalDescontos = 0.0

        for movimento in self.movimentos:
            if movimento.Movimento == Movimento.P:
                totalProventos += movimento.valor
            elif movimento.Movimento == Movimento.D:
                totalDescontos += movimento.valor

        valorLiquido = (self.salarioAtual + totalProventos) - totalDescontos

        print('Codigo: {} Nome: {}\nSalário: {} Total Proventos: {} Total Descontos: {} Valor Liquido a Receber: {}'.format(
            self.codigo, self.nome, self.salarioAtual, totalProventos, totalDescontos, valorLiquido))

    def inserirMovimentosCol(self, mov):
        if type(mov) == FolhaMovimento:
            self.movimentos.append(mov)
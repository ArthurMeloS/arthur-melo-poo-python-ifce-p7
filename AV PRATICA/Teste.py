from FolhaPagamento import FolhaPagamento
from FolhaMovimento import FolhaMovimento
from Colaborador import Colaborador
from Movimento import Movimento

class Teste:
    def main():
        # Questão 1 - Resposta
        FP = FolhaPagamento(9, 0, 0, 2019)

        # Questão 2 - Resposta
        CL01 = Colaborador(100, "Manoel Claudino", "Av 13 de Maio 2081", "88671020", "Benfica", "60020-060" , "124543556-89", 4500.00)
        CL02 = Colaborador(200, "Carmelina da Silva", "Avenida dos Expedicionários 1200", "30351280", "Aeroporto", "60530-020" , "301789435-54", 2500.00)
        CL03 = Colaborador(300, "Gurmelina Castro Saraiva", "Av João Pessoa 1020", "32351089", "Damas", "60330-090", "350245632-76", 3000.00)

        # Questão 3 - Resposta
        MF01 = FolhaMovimento(CL01, 'Gratificacao', 4500.00, Movimento.P)
        MF02 = FolhaMovimento(CL01, 'Plano Saúde', 1000.00, Movimento.P)
        MF03 = FolhaMovimento(CL01, 'Pensão', 600.00, Movimento.D)
        MF04 = FolhaMovimento(CL02, 'Gratificacao', 2500.00, Movimento.P)
        MF05 = FolhaMovimento(CL02, 'Plano Saúde', 1000.00, Movimento.P)
        MF06 = FolhaMovimento(CL02, 'Faltas', 600.00, Movimento.D)
        MF07 = FolhaMovimento(CL03, 'Gratificacao', 4500.00, Movimento.P)
        MF08 = FolhaMovimento(CL03, 'Plano Saúde', 1000.00, Movimento.P)
        MF09 = FolhaMovimento(CL03, 'Pensão', 600.00, Movimento.D)

        # Questão 6 - Resposta
        FP.inserirMovimentos(MF01)
        FP.inserirMovimentos(MF02)
        FP.inserirMovimentos(MF03)
        FP.inserirMovimentos(MF04)
        FP.inserirMovimentos(MF05)
        FP.inserirMovimentos(MF06)
        FP.inserirMovimentos(MF07)
        FP.inserirMovimentos(MF08)
        FP.inserirMovimentos(MF09)

        # Questão 7 - Resposta
        CL01.inserirMovimentosCol(MF01)
        CL01.inserirMovimentosCol(MF02)
        CL01.inserirMovimentosCol(MF03)
        CL02.inserirMovimentosCol(MF04)
        CL02.inserirMovimentosCol(MF05)
        CL02.inserirMovimentosCol(MF06)
        CL03.inserirMovimentosCol(MF07)
        CL03.inserirMovimentosCol(MF08)
        CL03.inserirMovimentosCol(MF09)

        FP.inserirColaboradores(CL01)
        FP.inserirColaboradores(CL02)
        FP.inserirColaboradores(CL03)

        FP.calcularFolha()
        CL01.calcularSalario()
        CL02.calcularSalario()
        CL03.calcularSalario()

if __name__ == '__main__':
    Teste.main()
import API_BCA as api
class Investimentos:
    def __init__(self):
        pass
    

class RDBNubank:
    def __init__(self, valor_inicial, data_aplicacao, taxa_cdi, taxa_iof, data_vencimento=None):
        self.valor_inicial = valor_inicial
        self.data_aplicacao = data_aplicacao
        self.taxa_cdi = taxa_cdi
        self.taxa_iof = taxa_iof
        self.data_vencimento = data_vencimento

    def calcular_rendimento(self, data_atual):
        taxa_cdi = api.obter_tava_cdi()
        print(taxa_cdi)
        pass

    def calcular_imposto_de_renda(self):
        # Lógica para calcular o imposto de renda sobre o rendimento
        pass

    def resgatar(self, data_resgate):
        # Lógica para simular um resgate em determinada data
        pass

    def __str__(self):
        return f"RDB Nubank: Valor inicial: R$ {self.valor_inicial:.2f}, Data de aplicação: {self.data_aplicacao}, Taxa CDI: {self.taxa_cdi:.2f}%"


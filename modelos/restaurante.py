from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(28)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for indice, restaurante in enumerate(cls.restaurantes):
            id = indice + 1
            print(f'{id}- {restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | ⭐ {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return 'Ativo ✔️' if self._ativo else 'Inativo ❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if 0 <= nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Ainda sem avaliação.'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media_das_notas = round(soma_das_notas / quantidade_de_notas, 1)
        return media_das_notas
    
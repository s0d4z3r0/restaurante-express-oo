class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(28)} | {'Categoria'.ljust(25)} | {'Status'}')
        for indice, restaurante in enumerate(cls.restaurantes):
            id = indice + 1
            print(f'{id}- {restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        return 'Ativo ✔️' if self._ativo else 'Inativo ❌'
    
    def alternar_estado(self):
        self._ativo = not self._ativo
    
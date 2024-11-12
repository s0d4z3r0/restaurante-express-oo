from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_mex = Restaurante('Mexican Food', 'Mexicano')
# restaurante_japa = Restaurante('JapaNoi', 'Japonesa')
# restaurante_mex.alternar_estado()

restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
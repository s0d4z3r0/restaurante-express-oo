from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mex = Restaurante('Mexican Food', 'Mexicano')
restaurante_japa = Restaurante('JapaNoi', 'Japonesa')
restaurante_mex.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
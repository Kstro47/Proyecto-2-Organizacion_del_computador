import re
    
def model_input(videogames, msg = 'Ingresa el modelo del videojuego: '):
    while True:
        try:
            string = input(msg)
            pattern = '[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9]'
            
            if not re.match(pattern, string):
                raise Exception
            
            if len(string) > 8:
                raise Exception

            for videogame in videogames:
                if videogame.modelo == string:
                    print('Este videojuego ya existe en el inventario.')
                    raise Exception
        except:
            print('Error, valide sus datos')
        else:
            return string


def tittle_input(videogames, msg = 'Ingresa el título del videojuego: '):
    while True:
        try:
            string = input(msg)
            if len(string) > 10:
                raise Exception

            for videogame in videogames:
                if videogame.tittle == string:
                    print('Este videojuego ya está en la base de datos.')
                    raise Exception
        except:
            print('Error, ingrese datos válidos.')
        else:
            return string
        

def videogame_price(msg = 'Ingrese el precio del videojuego: '):
    while True:
        try:
            integer = float(input(msg))

            if integer < 0:
                raise Exception
        except:
            print('Error, valide sus datos.')
        else:
            return integer

def pintura_status(msg = 'Estado de la pintura:'):
    while True:
        try:
            print(msg)

            options = ['En exhibicion','En Mantenimiento']

            option = range_validation(options)

            if option == 0:
                return True
            else:
                return False
        except:
            print('Error, valide sus datos')

def range_validation(options):
    while True:
        try:
            for index, option in enumerate(options):
                print(f'{index + 1}- {option}')

            option = int(input('Escoge una opción: ')) - 1

            if not option in range(len(options)):
                raise Exception
        except:
            print('Error, valide sus datos.')
        else:
            return option









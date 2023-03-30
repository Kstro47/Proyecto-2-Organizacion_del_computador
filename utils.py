import re

def model_search_input(msg):
    while True:
        try:
            string = input(msg)
            pattern = '[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9]'
            
            if not re.match(pattern, string):
                raise ValueError('El modelo debe tener 6 letras mayúsculas seguidas de 2 dígitos')
            
            if len(string) > 8:
                raise Exception
            return string
        except ValueError as e:
            print(f'Error: {str(e)}. Intente de nuevo.')


def model_input(database, msg = 'Ingresa el modelo del videojuego: '):
    while True:
        try:
            string = input(msg)
            pattern = '[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][0-9][0-9]'
            
            if not re.match(pattern, string):
                raise ValueError('El modelo debe tener 6 letras mayúsculas seguidas de 2 dígitos')
            
            if len(string) > 8:
                raise Exception

            for videogames in database:
                    for videogame in videogames:
                        if videogame.model == string:
                            raise ValueError('Este modelo ya existe en la base de datos')
            return string
        except ValueError as e:
            print(f'Error: {str(e)}. Intente de nuevo.')
            


def tittle_input(database, msg = 'Ingresa el título del videojuego: '):
    while True:
        try:
            string = input(msg)
            if len(string) > 10:
                raise ValueError('El título debe tener menos de 10 caracteres')

            for videogames in database:
                for videogame in videogames:
                    if videogame.model == string:
                        raise ValueError('Este modelo ya existe en la base de datos')
            return string
        except ValueError as e:
            print(f'Error: {str(e)}. Intente de nuevo.')
            
        

def videogame_price(msg = 'Ingrese el precio del videojuego en Bs.: '):
    while True:
        try:
            integer = float(input(msg))

            if integer < 0 or integer > 999 :
                raise Exception
        except:
            print('Error, el precio no puede ser menor a "0" o mayor a "999"')
        else:
            return integer

def videogame_status(msg = 'Estado del videojuego:'):
    while True:
        try:
            print(msg)

            options = ['En stock','Alquilado']

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

            option = int(input('\nEscoge una opción: ')) - 1

            if not option in range(len(options)):
                raise Exception
        except:
            print('Error, escoja una opción válida.')
        else:
            return option









from Videogame import Videogame
from utils import *

class Rent_a_Game:
    def __init__(self):
        self.database:list[Videogame] = [[] for _ in range(3)]
        self.overflow_database:list[Videogame] = [[] for _ in range(6)]
        self.capacity = 9
        self.overflow_capacity = 18
        self.index = []

    def is_full(self):
        for sublist in self.database:
            if len(sublist) < self.capacity:
                return False
        for sublist in self.overflow_database:
            if len(sublist) < self.overflow_capacity:
                return False
        return True

    def hash_key_function(self, model):

        hash_key = sum([ord(char) for char in model])
        hash_key %= 3

        return hash_key
 
    def hashing_append(self, hash_key, videogame):
        if hash_key == 0:
            group = 0  # Primer grupo

        elif hash_key == 1:
            group = 1  # Segundo grupo

        else:
            group = 2  # Tercer grupo
        
        if len(self.database[group]) < 3:
            self.database[group].append(videogame) # Añadir videojuego al grupo
        else:
            self.overflow_append(group, videogame)  # Grupo está llena, se añade videojuego a un grupo de overflow

    def overflow_append(self, group_num, videogame):    
        full = False
        if not self.is_full():
            for group in self.overflow_database:
                if len(group) == 0:
                    group.append(group_num)
                    group.append(videogame)
                    full = False
                    return print(" Juego guardado con éxito ")
                elif 1 <= len(group) < 4:
                    if group[0] == group_num:
                            group.append(videogame)
                            full = False
                            return print(" Juego guardado con éxito")     
                elif len(group) == 4:
                    if group[0] == group_num:
                        full = True
            if full == True:
                print("El almacenamiento para esta llave está lleno.")
        else: 
            print("El almacenamiento está lleno.")


    def register_videogame(self):
        model = model_input(self.database)
        tittle = tittle_input(self.database)
        price = videogame_price()

        videogame = Videogame(model, tittle, price, True)
        key = self.hash_key_function(videogame.model)
        self.hashing_append(key, videogame)


        print("\n¡Videojuego registrado con éxito!\n")


    def search_videogame(self):
        print("¿Que acción desea realizar?")
        options = ['Buscar por modelo', 'Buscar por título']
        option = range_validation(options)
        if option == 0:
            videogame_model = model_search_input('Ingrese el modelo del videojuego que desea buscar: ')
            hash_value = self.hash_key_function(videogame_model)
            videogames = self.database[hash_value]
            for videogame in videogames:
                if videogame.model == videogame_model:                    
                    return videogame
            for group in self.overflow_database:
                if len(group) > 0:
                    if group[0] == hash_value:
                        for videogame in group:
                            if videogame.model == videogame_model:
                                return videogame
            return None
        if option == 1:
            
        

    def delete_videogame(self):
        options = ['Si', 'No']

        print("\nVideojuegos Registrados:\n")
        
        for videogames in self.database:
            for videogame in videogames:
                print(f'-- {videogame.show_primary()}')
        delete_videogame = model_search_input('Ingresa el modelo del videojuego que deseas eliminar: ')
        
        for videogames in self.database:
            for num, videogame in enumerate(videogames):
                if videogame.model == delete_videogame:
                    print("\n¿Seguro que quieres borrar este videojuego?\n")
                    option = range_validation(options)
                    if option == 0: 
                        videogames.pop(num)
                        print('Se ha borrado el videojuego correctamente.')
                        return
                    else:
                        return
        
        print("El videojuego ingresado no se encuentra almacenado, vuelva a intentar.")
    

    def menu(self):
        """
        Muestra el menu del programa
        """
        menu = ['Insertar videojuego', 'Búsqueda de videojuego', 'Alquiler de un videojuego','Devolución de un videojuego','Eliminación de un juego','Salir']

        while True:
            print('\nBienvenido a Rent-A-Game, escoga la opción de su preferencia:\n ')

            option = range_validation(menu)

            if option == 0:
                self.register_videogame()
                print (self.database)

            elif option == 1:
                if len(self.database) > 0:
                    found = self.search_videogame()
                    print(found)
                    if found != None:
                        print(f"Se ha encontrado el siguiente videojuego: {found.show_primary()} ")
                    else:
                        print("No se ha encontrado el videojuego.")
                else:
                    print("No hay videojuegos en la base de datos.")

            elif option == 2:
                if not self.is_full():
                    print(self.is_full());   
            
            elif option == 3:
                for games in self.database:
                    for game in games:
                        print(game.show_videogame())

            elif option == 4:
                self.delete_videogame()

            elif option == 5:
                self.write_txt()
                break

    def start_txt(self):
        with open("videojuegos.txt") as file_object:
            leer = file_object.read()
            videojuegos = leer.split("\n")
            for videojuego in videojuegos:
                lista_atributos = videojuego.split(",")
                if lista_atributos[0] == " " or lista_atributos[0] == "":
                    break
                else:
                    model = lista_atributos[0]
                    tittle = lista_atributos[1]
                    price = lista_atributos[2]
                    boolean = lista_atributos[3]
                    if boolean == "TRUE":
                        status = True
                    else:
                        status = False
                    videogame = Videogame(model, tittle, price, status)
                    key = self.hash_key_function(videogame.model)
                    self.hashing_append(key, videogame)                
        file_object.close       

    def write_txt(self):
        with open("videojuegos.txt","w") as file_object:
            for videogames in self.database:
                for videogame in videogames:
                    if videogame.status == True:
                        status = "TRUE"
                    else:
                        status = "FALSE"
                    price = str(videogame.price)
                    text=videogame.model+","+videogame.tittle+","+price+","+status+"\n"
                    file_object.write(text)
            for videogames in self.overflow_database:
                for videogame in videogames:
                    if videogame.status == True:
                        status = "TRUE"
                    else:
                        status = "FALSE"
                    price = str(videogame.price)
                    text=videogame.model+","+videogame.tittle+","+price+","+status+"\n"
                    file_object.write(text)
            file_object.write(" ")
        file_object.close


    def start(self):

        self.start_txt()
        self.menu()

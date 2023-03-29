class Videogame:
    def __init__(self, model: str, tittle: str, price: int, status: bool, deleted: bool):
        self.model = model
        self.tittle = tittle
        self.price = price
        self.status = status
        self.deleted = deleted

    def show_status(self):
        if self.status:
            return f'EN STOCK'
        else:
            return f'ALQUILADO'
        
    def show_videogame(self):
        return f'''
        - Título: {self.tittle}
        - Precio: {self.price}
        - Estado: {self.status}
        - Modelo: {self.model}
        '''

    def set_deleted(self):
        self.deleted = True

    def set_status(self, status):
        self.status = status



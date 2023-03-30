class Videogame:
    def __init__(self, model: str, tittle: str, price: int, status: bool):
        self.model = model
        self.tittle = tittle
        self.price = price
        self.status = status

    def show_status(self):
        if self.status:
            return f'EN STOCK'
        else:
            return f'ALQUILADO'
        
    def show_primary(self):
        return f'''
        - Modelo: {self.model}
        - Título: {self.tittle}
        - Precio: Bs.{self.price}
        - Estado: {self.status}
        '''

    def show_secondary(self):
        return f'''
        - Título: {self.tittle}
        - Precio: Bs.{self.price}
        - Estado: {self.status}
        - Modelo: {self.model}
        '''

    def set_status(self, status):
        self.status = status



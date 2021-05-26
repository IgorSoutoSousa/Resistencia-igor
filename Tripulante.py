class Tripulante:
    def __init__(self, nome, cargo, especie):
        self.__nome = nome
        self.__cargo = cargo
        self.__especie = especie
        

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
        
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, especie):
        self.__especie = especie            
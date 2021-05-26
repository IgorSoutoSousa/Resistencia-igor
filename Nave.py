class Nave:
    def __init__(self, idnave, fabricante, quant_trip, modelo, classe, capitao):
        self.__idnave = idnave
        self.__fabricante = fabricante
        self.__quant_trip = quant_trip
        self.__modelo = modelo
        self.__classe = classe
        self.__capitao = capitao
        
    
    @property
    def idnave(self):
        return self.__idnave
    
    @idnave.setter
    def idnave(self, idnave):
        self.__idnave = idnave      
        
    @property
    def fabricante(self):
        return self.__fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante):
        self.__fabricante = fabricante 
    
    @property
    def quant_trip(self):
        return self.__quant_trip
    
    @quant_trip.setter
    def quant_trip(self, quant_trip):
        self.__quant_trip = quant_trip 
    
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo      
             
    @property
    def classe(self):
        return self.__classe
    
    @classe.setter
    def classe(self, classe):
        self.__classe = classe      

    @property
    def capitao(self):
        return self.__capitao
    
    @capitao.setter
    def capitao(self, capitao):
        self.__capitao = capitao    

#CLASSE MEMBRO:
class Membro:
    def __init__(self, nome, especie, cargo, possuiNave = False, nave = None):
        self.__nome = nome
        self.__especie = especie
        self.__cargo = cargo
        self.__possuiNave = possuiNave
        self.__nave = nave
        
#GET´s e SET´s:
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, especie):
        self.__especie = especie
    
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo  

    @property
    def possuiNave(self):
        return self.__possuiNave
 
    @possuiNave.setter
    def possuiNave(self, possuiNave):
        if possuiNave.lower() == "s":
            return self.__possuiNave == True
        return False
             
    @property
    def nave(self):
        return self.__nave
    
    @nave.setter
    def nave(self, nave):
        return self.__nave
    
#Verificação booleana, se possui nave ou não:   
 
    def verficacao_possuiNave(self):
        if self.__possuiNave == "s":
            return True 
        return False
    
#METODO QUE VERIFICA NAVE COMO OBJETO:
   
    def verificaNave(self): 
        if self.__possuiNave == True:
            return self.__nave != None
        return self.__nave == None
    
 

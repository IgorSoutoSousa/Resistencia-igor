#lista graduação JEDI:

listaGrau = ['Padawan', 'Cavaleiro', 'Mestre']

#CLASSE JEDI:
class Jedi:
    def __init__(self, nome, graduacao, especie, corSabre, possuiNave = False, nave = None):
        self.__nome = nome
        self.__graduacao = graduacao
        self.__especie = especie
        self.__corSabre = corSabre
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
    def graduacao(self):
        return self.__graduacao
    
#Verificação booleana, se a graduação do Jedi está contida na listaGrau:
    @graduacao.setter
    def graduacao(self, graduacao):
        verificaGrau = False
        for op in listaGrau:
            if graduacao == op:
                verificaGrau = True
            if verificaGrau:
                self.__graduacao = graduacao
            else:
                print("Grau não correspondente a ordem Jedi")
          
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, especie):
        self.__especie = especie  
        
    @property
    def corSabre(self):
        return self.__corSabre
    
    @corSabre.setter
    def corSabre(self, corSabre):
        self.__corSabre = corSabre
        
    @property 
    def possuiNave(self):
        return self.__possuiNave

#Verificação booleana, se possui nave ou não:
    
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
    
#METODO QUE VERIFICA NAVE COMO OBJETO:
    
    def verificaNave(self): 
        if self.__possuiNave == True:
            return self.__nave != None
        return self.__nave == None
    
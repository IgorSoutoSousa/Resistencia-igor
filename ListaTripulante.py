class ListaTripulante:
    def __init__(self):
        self.__tripulantes = []
        
            
    @property
    def tripulantes(self):
        return self.__tripulantes
    
    @tripulantes.setter
    def tripulantes(self, tripulantes):
        for i in tripulantes:
            if i.possuiNave == "s":
                self.__tripulantes.append(i) 
from Jedi import Jedi
from Membro import Membro
from Nave import Nave
from ListaTripulante import ListaTripulante
from Tripulante import Tripulante


   
print(72*'-')
print("Bem-vindo; Esse é seu assistente de cadastro de Passaporte da Resistência")
print("Prencha o formulário")
print(72*'-')

escolha = input("Deseja se cadastrar como novo Membro da Resistência ou vc é um Jedi? (membro) ou (jedi): ")
if escolha.lower() == "membro":
    nome = input("Qual o seu nome?: ")
    especie = input("Qual sua espécie?: ")
    cargo = input("Qual seu Cargo?: ")
    possuiNave = input("Você possui nave [s] ou [n]: ")
    
    if possuiNave.lower() == "s":
        possuiNave = True 
        idnave = input("Qual a identificação de sua nave?: ")
        fabricante = input("Qual o fabricante de sua nave?: ")
        quant_trip = int(input("Qual a capacidade de tripulantes?: "))
        modelo = input("Qual o Modelo?: ")
        classe = input("Qual a Classe?: ")
        capitao = input("O capitão da Nave é Jedi ou Membro?: ")
        newnave = Nave(idnave, fabricante, quant_trip, modelo, classe, capitao)
        newmembro = Membro(nome, especie, cargo, possuiNave, newnave)
        
        print("Vamos cadastrar a lista de tripulantes? CLICK ENTER para continuar o cadastro, para ")
        print(8*'-')
        imprimir = input ("LISTA_TRIPULANTES")  
        print(8*'-')   
        while True:
            nome = input("Qual o nome do tripulante?: ")
            if nome == '':
                break
            
            cargo = input ("Qual o cargo do tripulante?: ")
            especie = input("Qual a especie do tripulante?: ")
            newtripulante = Tripulante(nome, cargo, especie)
            
            listatripulacao = []
            lista = ListaTripulante()
            lista.tripulantes = listatripulacao
        
        
        print("Chegamos ao final de seu questionário. CLICK ENTER para IMPRIMIR seu passaporte")
        print(8*'-')
        imprimir = input ("IMPRIMIR")  
        print(8*'-')   
        print(24*'-', "Passaporte Resistência", 24*'-')  
        print(72*'-') 
        print("⣿⣿⣿⡿⠛⠉⠉⠉⠙⠛⠻⢿⣿⣿⣿") 
        print("⣿⣿⠛⠄⢀⣤⣤⣤⣤⣄⡀⠄⠿⣿⣿")
        print("⣿⡿⠄⠄⢸⡿⠿⣿⣿⣿⣷⡀⠄⢿⣿")
        print("⣿⣷⣤⡀⣿⣿⣴⣿⣷⣾⣿⣧⣠⣿⣿")
        print("⣿⣿⣿⣶⠹⠿⠋⣉⡉⠛⠟⢠⣿⣿⣿")
        print("⣿⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿")
        print("⣿⣿⣿⣿⣷⣤⣀⣠⣀⣀⣴⣿⣿⣿⣿")
        print("Nome:", newmembro.nome,"/ Espécie:", newmembro.especie, "/ Cargo: ", newmembro.cargo)
        print("Registro Nave: ", newnave.idnave,"/ Fabricante:", newnave.fabricante, "/ Capacidade:", newnave.quant_trip, "/Classe:", newnave.classe)
        print(72*'-')    
    else:
        possuiNave = False
        newmembro = Membro(nome, especie, cargo, possuiNave)
        print("Chegamos ao final de seu questionário. CLICK ENTER para IMPRIMIR seu passaporte")
        print(8*'-')
        imprimir = input ("IMPRIMIR")  
        print(8*'-')   
        print(24*'-', "Passaporte Resistência", 24*'-')   
        print(72*'-') 
        print("⣿⣿⣿⡿⠛⠉⠉⠉⠙⠛⠻⢿⣿⣿⣿") 
        print("⣿⣿⠛⠄⢀⣤⣤⣤⣤⣄⡀⠄⠿⣿⣿")
        print("⣿⡿⠄⠄⢸⡿⠿⣿⣿⣿⣷⡀⠄⢿⣿")
        print("⣿⣷⣤⡀⣿⣿⣴⣿⣷⣾⣿⣧⣠⣿⣿")
        print("⣿⣿⣿⣶⠹⠿⠋⣉⡉⠛⠟⢠⣿⣿⣿")
        print("⣿⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿")
        print("⣿⣿⣿⣿⣷⣤⣀⣠⣀⣀⣴⣿⣿⣿⣿")
        print("Nome:", newmembro.nome,"/ Espécie:", newmembro.especie, "/ Cargo: ", newmembro.cargo)
        print(72*'-')    
if escolha.lower() == "jedi":
    nome = input("Qual o seu nome?: ")
    especie = input("Qual sua espécie?: ")
    graduacao = input("Qual a sua Graduação? Padawan, Cavaleiro, ou Mestre:: ") 
    corSabre = input("Qual a cor do seu sabre de Luz: ") 
    possuiNave = input("Você possui nave [s] ou [n]: ")
    if possuiNave.lower() == "s":
        possuiNave = True
        idnave = input("Qual a identificação de sua nave?: ")
        fabricante = input("Qual o fabricante de sua nave?: ")
        quant_trip = int(input("Qual a capacidade de tripulantes?: "))
        modelo = input("Qual o Modelo?: ")
        classe = input("Qual a Classe?: ")
        capitao = input("O capitão da Nave é Jedi ou Membro?: ")
        
        newnave = Nave(idnave, fabricante, quant_trip, modelo, classe, capitao)
        newjedi = Jedi(nome, graduacao, especie, corSabre, possuiNave, newnave)
        

        print("Vamos cadastrar a lista de tripulantes? CLICK ENTER para continuar o cadastro, para ")
        print(8*'-')
        imprimir = input ("LISTA_TRIPULANTES")  
        print(8*'-')   
        while True:
            nome = input("Qual o nome do tripulante?: ")
            if nome == '':
                break
            
            cargo = input ("Qual o cargo do tripulante?: ")
            especie = input("Qual a especie do tripulante?: ")
            newtripulante = Tripulante(nome, cargo, especie)
            
            listatripulacao = []
            lista = ListaTripulante()
            lista.tripulantes = listatripulacao
        
            
            
        
        print("Chegamos ao final de seu questionário. CLICK ENTER para IMPRIMIR seu passaporte")
        print(8*'-')
        imprimir = input ("IMPRIMIR")  
        print(8*'-')   
        print(24*'-', "Passaporte Resistência", 24*'-')  
        print(72*'-') 
        print("⣿⣿⣿⡿⠛⠉⠉⠉⠙⠛⠻⢿⣿⣿⣿") 
        print("⣿⣿⠛⠄⢀⣤⣤⣤⣤⣄⡀⠄⠿⣿⣿")
        print("⣿⡿⠄⠄⢸⡿⠿⣿⣿⣿⣷⡀⠄⢿⣿")
        print("⣿⣷⣤⡀⣿⣿⣴⣿⣷⣾⣿⣧⣠⣿⣿")
        print("⣿⣿⣿⣶⠹⠿⠋⣉⡉⠛⠟⢠⣿⣿⣿")
        print("⣿⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿")
        print("⣿⣿⣿⣿⣷⣤⣀⣠⣀⣀⣴⣿⣿⣿⣿")
        print("Nome Jedi:", newjedi.nome,"/ Espécie:", newjedi.especie, "/ Graduação:", newjedi.graduacao, "/ Sabre:", newjedi.corSabre)
        print("Registro Nave:", newnave.idnave,"/ Fabricante:", newnave.fabricante, "/ Capacidade:", newnave.quant_trip, "/Classe: ", newnave.classe, "/ Capitão é: ", newnave.capitao)
        print("Nome: ", newtripulante.nome, "/ Cargo: ", newtripulante.cargo, "/ Especie: ", newtripulante.especie) 
        print(72*'-') 
                   
    else:
        newjedi = Jedi(nome, graduacao, especie, corSabre, possuiNave)
        print("Chegamos ao final de seu questionário. CLICK ENTER para IMPRIMIR seu passaporte")
        print(8*'-')
        imprimir = input ("IMPRIMIR")  
        print(8*'-') 
        print(24*'-', "Passaporte Resistência", 24*'-')   
        print(72*'-') 
        print("⣿⣿⣿⡿⠛⠉⠉⠉⠙⠛⠻⢿⣿⣿⣿") 
        print("⣿⣿⠛⠄⢀⣤⣤⣤⣤⣄⡀⠄⠿⣿⣿")
        print("⣿⡿⠄⠄⢸⡿⠿⣿⣿⣿⣷⡀⠄⢿⣿")
        print("⣿⣷⣤⡀⣿⣿⣴⣿⣷⣾⣿⣧⣠⣿⣿")
        print("⣿⣿⣿⣶⠹⠿⠋⣉⡉⠛⠟⢠⣿⣿⣿")
        print("⣿⣿⣿⣿⡀⠄⠄⠄⠄⠄⠄⣴⣿⣿⣿")
        print("⣿⣿⣿⣿⣷⣤⣀⣠⣀⣀⣴⣿⣿⣿⣿")
        print("Nome Jedi:", newjedi.nome,"/ Espécie:", newjedi.especie, "/ Graduação:", newjedi.graduacao, "/ Sabre:", newjedi.corSabre)
        print(72*'-')  
else:
    print("Opção invalida")       
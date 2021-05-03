from Jedi import Jedi
from Membro import Membro
from Nave import Nave

#Relatório Visto de entrada na resistência. 2021.5.3

new_relatorio = {}
new = []

def relatorio_militante(chave, especie, cargo, idnave):
    new.append(especie)
    new.append(cargo)
    new.append(idnave)
    
    new_relatorio[chave] = new.copy()
    new.clear()
    
def exibir(chave):
    print('Nome: ',chave)
    print('Nota 1: ',new_relatorio[chave][0])
    print('Nota 2: ',new_relatorio[chave][1])
    print('Nota 3: ',new_relatorio[chave][2])
    print('Media: {:.2f}'.format(new_relatorio[chave][3]))
    print(15*'-')

#construir uma função para exibir o relatório final
#construir um lista com todos os dados


while True:

    nome = input("Qual o seu nome?: ")
    especie = input("Qual sua espécie?: ")
    cargo = input("Qual seu Cargo?: ")
    nave = input("Você possui nave [s] ou [n]: ")
    newmembro = Membro(nome, especie, cargo, nave)
    if nave == "s":
        idnave = input("Qual a identificação de sua nave?: ")
        fabricante = input("Qual o fabricante de sua name?: ")
        quant_trip = input("Qual a capacidade de tripulantes?: ")
        modelo = input("Qual o Modelo?: ")
        classe = input("Qual a Classe?: ")
        newnave = Nave(idnave, fabricante, quant_trip, modelo, classe)
    else:
        jedi = input("vc é Jedi?[s] ou [n]: ")
        if jedi == "s":
            graduacao = input("Qual seu nível: Padawan, Cavaleiro, ou Mestre: ")
            especie = input("Qual sua espécie?: ")
            sabre = input("Qual a cor do seu sabre de Luz: ") 
            newjedi = Jedi(nome, graduacao, especie, sabre)
   
    print("Chegamos ao final de seu questionário. Click enter para imprimir seu passaporte")
    print(15*'-')
    imprimir = input ("imprimir")  
    print(15*'-')   
    if imprimir == '':
        break
           
relatorio_militante(nome, especie, cargo, idnave)
        
for new in new_relatorio:
    exibir(new)
       

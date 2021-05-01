from Jedi import Jedi
from Membro import Membro
from Nave import Nave

#construir uma função para exibir o relatório final
#construir um lista com todos os dados


while True:
    nome = input("Qual o seu nome?: ")
    jedi = input("vc é Jedi?[s] ou [n]: ")
    nave = input("vc possui nave? [s] ou [n]: ")
    if jedi == "s":
        #jedi
        graduacao = input("Qual seu nível: Padawan, Cavaleiro, ou Mestre: ")
        especie = input("Qual sua espécie?: ")
        sabre = input("Qual a cor do seu sabre de Luz: ") 
        newjedi = Jedi(nome, graduacao, especie, sabre)
        break
    else:
        #membro
        especie = input("Qual sua espécie?: ")
        cargo = input("Qual seu Cargo?: ")
        nave = input("Você possui nave [s] ou [n]: ")
        if nave == "s":
            newmebro = Membro(nome, especie, cargo, nave)
    


print (newjedi.nome)
print (newjedi.graduacao)
print (newjedi.especie)
print (newjedi.sabre)
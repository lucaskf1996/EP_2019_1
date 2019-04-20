import random
def funcao_aparicao(posicao,vida,ataque,armadura,dinheiro,xp,nivel):
    chance = random.randint(1,7)

    if chance == '1':
        vida,dinheiro,nivel,xp = funcao_de_combate(vida,ataque,armadura,dinheiro,xp,nivel)
        return vida,dinheiro,nivel,xp
    return vida,dinheiro,nivel,xp
    
        

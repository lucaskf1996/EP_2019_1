
import random
import time

def funcao_aparicao(vida_jogador, cap_hp, ataque_jogador, itens_equipados, nivel_jogador, posicao, dinheiro, xp, cap_xp, game_over):
    chance = random.randint(1,7)
    
    if chance > 2:
        print ("Voce encontrou um monstro!\n")
        time.sleep(2)
        vida_jogador, cap_hp, nivel_jogador, xp, cap_xp, dinheiro, game_over = FUNCAO_COMBATE (vida_jogador, cap_hp, ataque_jogador, itens_equipados, nivel_jogador, posicao, dinheiro, xp, cap_xp, game_over)
        
def FUNCAO_COMBATE(vida_jogador, cap_hp, ataque_jogador, itens_equipados, nivel_jogador, posicao, dinheiro, xp, cap_xp, game_over):
    ataque_monstro = 80
    ataque_monstro += nivel_jogador * 0.1
    vida_monstro = 200
    vida_monstro += nivel_jogador * 0.1
     
    while vida_jogador > 0 and vida_monstro > 0:
        ataque = ["rock", "paper", "scissors"]
        ataque_monstro = ataque [random.randint (0,2)]
        ataque_jogador = input ("Escolha: rock, paper ou scissors:")
    
     
        if ataque_jogador == "scissors" and ataque_monstro == "paper":
            vida_monstro -= ataque_jogador
            print("você deu {0} de ataque".format (ataque_jogador))
        
            
        elif ataque_jogador == "paper" and ataque_monstro == "rock":
            vida_monstro-= ataque_monstro
            print("você deu {0} de ataque".format (ataque_jogador))
        
        elif ataque_jogador == "rock" and ataque_monstro == "scissors":
            vida_monstro -= ataque_jogador
            print("você deu {0} de ataque".format (ataque_jogador))
        
        
        elif ataque_jogador == ataque_monstro:
            print("Empate!! Digite um ataque novamente.")
            
        
        else:
            print("Você recebeu {0} de dano e agora está com {1}/{2} de vida".formar(ataque_monstro, vida_jogador, cap_hp))
            print (vida_jogador)
        
    if vida_jogador <= 0:
        print ("Você perdeu")
        game_over = True
        
    else:
        print("Você derrotou seu amigo!")
        
        nivel_jogador, cap_hp, xp, cap_xp, ataque_jogador = nivel_e_xp(nivel_jogador, cap_hp, xp, cap_xp, ataque_jogador)
 
    
    return vida_jogador, cap_hp, nivel_jogador, xp, cap_xp, dinheiro, game_over


    

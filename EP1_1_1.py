# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 07:38:10 2019

@author: fuque
"""

##### IMPRIME TUDO DO CENARIO ATUAL #####

def imprimir_cenario(cenario_atual):
    print(cenario_atual["titulo"])
    print("-"*len(cenario_atual["titulo"]))
    time.sleep(1)
    print(cenario_atual["descricao"])
    print("")
    time.sleep(1)
    print("Opcoes:")
    time.sleep(1)
    for i in cenario_atual["opcoes"]:
        print(i,":",cenario_atual["opcoes"][i])
    print("")
 
##### ATUALIZA A VARIAVEL CENARIO_ATUAL #####

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do Insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                "itens do local": "Mostra uma lista com os itens que foram encontrados"
            }
        },
            
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor",
                "itens do local": "Mostra uma lista com os itens que foram encontrados"
            }
        },
            
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {
                
            }
        },
        
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                "itens do local": "Mostra uma lista com os itens que foram encontrados"
            }
        },
            
        "sala de teleporte": {
                "titulo": "",
                "descricao": "",
                "opcoes": { "teleporte": "Escreva o nome correto do local, ou...",
                "biblioteca": "Ir para a biblioteca"          
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
##### DICIONARIOS PARA SISTEMA DE ITENS #####

    itens_no_mapa = {     # Dicionario para find_items()
        "local": ["item", "item2", "item3"],
        "local2": ["item", "item2", "item3"],
        "Local3": ["item", "item2", "item3"]
    }

    itens_por_mapa = {     # Dicionario para show_possible_items()
        "local": {
            "item": True,
            "item2": False,
            "item3": False #...
        },
        "local2": {
            "item": False,
            "item2": False,
            "item3": False #...
        },
        "Local3": {
            "item": False,
            "item2": False,
            "item3": False #...
        }
    }
        

##### VARIAVEIS DO JOGADOR #####

    hp_jogador=20
    mochila=["bilhete", "marmita", "carteirinha"]
    itens_equipados=[["baralho", "seu casaco"], [1, 1]]
    nivel_do_jogador=1
    cap_xp_jogador=1
    xp_do_jogador=0

#### FIM VARIAVEIS DO JOGADOR
    
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    nome_jogador=input("Digite seu nome: ")
    time.sleep(2)
    print()
    print("'{0}!'".format(nome_jogador))
    time.sleep(2)
    print("Seu amigo se aproxima de voce e te entrega um baralho")
    time.sleep(1)
    print("'Voce esqueceu isso ontem'")
    time.sleep(2)
    print()
    print("baralho foi equipado. Só cuidado pra nao jogar no olho dos outros")
    time.sleep(1)
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    time.sleep(4)
    
    print("")    

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        # Aluno A: substitua este comentário pelo código para imprimir 
        # o cenário atual.
        
        imprimir_cenario(cenario_atual) # Imprime o cenario atual com o as descricoes e opcoes.
        

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""
            
            while (escolha == "itens do local" or escolha == "procurar itens" or escolha == "usar item") and escolha in opcoes:   # Substituir por uma funcao?
                if escolha == "itens do local":
                    show_possible_items(cenario_atual["titulo"], itens_por_mapa)
                    
                if escolha == "procurar itens":
                    resultado_find_items=find_items(cenario_atual["titulo"], itens_no_mapa, itens_por_mapa)  #[give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] 
                    mochila.append(resultado_find_items[0])
                    itens_no_mapa = resultado_find_items[1]
                    itens_por_mapa = resultado_find_items[2]
                
                if escolha == "usar item":
                    hp_jogador, mochila, itens_equipados = item_effects(mochila, hp_jogador, itens_equipados)
                
                opcoes = cenario_atual['opcoes']
                # Aluno B: substitua este comentário e a linha abaixo pelo código
                # para pedir a escolha do usuário.
                escolha = ""
                
            if escolha in opcoes:   # Tem que arrumar isso aqui?
                nome_cenario_atual = escolha
            else:
                time.sleep(1)
                print("Sua indecisão foi sua ruína!")
                game_over = True
    time.sleep(1)
    print("")
    print("Você morreu!")

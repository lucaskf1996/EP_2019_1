# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 07:38:10 2019

@author: fuque
"""

import time
import random
from contextlib import contextmanager
import threading
import json
import _thread

def techlab (mochila):
    mochila.append("foda-se")
    print("\nvocê recebeu o item 'foda-se'\n")
    return mochila

########## SISTEMA DE COMBATE #########

##### NIVEL E XP #####

def nivel_e_xp(nivel_jogador, cap_hp, xp, cap_xp, ataque_base):
    if xp+1==cap_xp:
        nivel_jogador+=1
        cap_xp*=2
        xp=0
        print("Voce passou para o nivel", nivel_jogador, "!\n")
        cap_hp+=10
    else:
        xp+=1
    return nivel_jogador, cap_hp, xp, cap_xp, ataque_base


##### FUNCAO DE APARICAO #####

def funcao_aparicao(vida_jogador, cap_hp, ataque_jogador, itens_equipados, nivel_jogador, posicao, dinheiro, xp, cap_xp, game_over):
    chance = random.randint(1,7)
    
    if chance > 2:
        print ("Voce encontrou um monstro!\n")
        time.sleep(2)
        vida_jogador, cap_hp, nivel_jogador, xp, cap_xp, dinheiro, game_over = FUNCAO_COMBATE (vida_jogador, cap_hp, ataque_jogador, itens_equipados, nivel_jogador, posicao, dinheiro, xp, cap_xp, game_over)
    return vida_jogador, cap_hp, nivel_jogador, xp, cap_xp, dinheiro, game_over


##### FUNCAO PADRAO DE COMBATE #####
      
def FUNCAO_COMBATE(vida_jogador, cap_hp, ataque_jogador, itens_equipados, nivel_jogador, posicao, dinheiro, xp, cap_xp, game_over):
    ataque_monstro = 5
    ataque_monstro = int(ataque_monstro + nivel_jogador * 5)
    vida_monstro = 15
    vida_monstro = int(vida_monstro + nivel_jogador * 5)
     
    while vida_jogador > 0 and vida_monstro > 0:
        ataque = ["rock", "paper", "scissors"]
        escolha_monstro = ataque [random.randint (0,2)]
        escolha_jogador = input ("Escolha: rock, paper ou scissors:")
        
        while escolha_jogador not in ataque:
            print("\nEscolha invalida")
            escolha_jogador = input("Escolha: rock, paper ou scissors:")
     
        if escolha_jogador == "scissors" and escolha_monstro == "paper":
            vida_monstro -= ataque_jogador
            print("você deu {0} de ataque".format (ataque_jogador))
        
            
        elif escolha_jogador == "paper" and escolha_monstro == "rock":
            vida_monstro-= ataque_jogador
            print("você deu {0} de ataque".format (ataque_jogador))
        
        
        elif escolha_jogador == "rock" and escolha_monstro == "scissors":
            vida_monstro -= ataque_jogador
            print("você deu {0} de ataque".format (ataque_jogador))
        
        
        elif escolha_jogador == escolha_monstro:
            print("Empate!! Digite um ataque novamente.")
            
        
        else:
            vida_jogador -= ataque_monstro
            print("Você recebeu {0} de dano e agora está com {1}/{2} de vida".format(ataque_monstro, vida_jogador, cap_hp))
        
    if vida_jogador <= 0:
        print ("Você perdeu")
        game_over = True
        
    else:
        time.sleep(1)
        print("\nVocê derrotou seu amigo! Voce roubo... encontrou 5 reais!\n")
        dinheiro += 5
        nivel_jogador, cap_hp, xp, cap_xp, ataque_jogador = nivel_e_xp(nivel_jogador, cap_hp, xp, cap_xp, ataque_jogador)
 
    
    return vida_jogador, cap_hp, nivel_jogador, xp, cap_xp, dinheiro, game_over

##### FUNCAO DE COMBATE RAUL #####

def FUNCAO_COMBATE_RAUL (vida_jogador, cap_hp, ataque_jogador, itens_equipados, nivel_jogador, dinheiro, xp, cap_xp, game_over, Raul): #itens_equipados[1][0]
    
    ataque_monstro = 80
    vida_monstro = 600
    
    @contextmanager
    def tempo_combate(seconds):
        timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            return(dano) 
        finally:
            timer.cancel()
    
        # ends after 60 seconds - ***ainda a definir tempo de duração de batalha***
    time_limit = 3
    
    while vida_monstro > 0 and vida_jogador > 0:
        
        print("Comece a digiter 'a'+'enter' em \n")    
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        
        with tempo_combate(time_limit):
            dano=0
            while True:
                button_press = input("digite a + enter VÁRIAS VEZES!!!! ")
                if "a" == button_press:
                    dano += ataque_jogador+itens_equipados[1][0]+random.randint(-5, 5)
                    print ()
                    
        time.sleep(3)

        if button_press == "a":
            dano+=ataque_jogador+itens_equipados[1][0]+random.randint(-5, 5)                
        
        print("acabou o tempo")
        
        print("Voce deu {0} de dano".format(dano))
           
        vida_monstro -= dano
        if vida_monstro >0:
            if vida_jogador - (ataque_monstro - itens_equipados[1][1]) < 0:
                vida_jogador = 0
            else:
                vida_jogador -= (ataque_monstro+itens_equipados[1][1])
            
        print("Voce recebeu {0} de dano e agora tem {1}/{2} de vida".format(ataque_monstro, vida_jogador, cap_hp))
            
    if vida_jogador > 0:
        dinheiro+=5
        print("O cara desmaiou... Voce ganhou 5 de dinheiros e 1 de xp")
        nivel_jogador, cap_hp, xp, cap_xp, ataque_jogador = nivel_e_xp(nivel_jogador, cap_hp, xp, cap_xp, ataque_jogador)
        Raul = False
        
    game_over = True
        
    return vida_jogador, game_over, Raul


########## SISTEMA DE ITENS ##########


##### LOJA #####

def buy_item(itens_na_mochila,dinheiro):
    loja = {
  'cafe' : 5
, 'pao de queijo': 15
, 'lata de coca': 10
}
    for i in loja:
        print("-", i," ", loja[i])
    print ("\n Voce tem", dinheiro, "dinheiros")
    buy = input('Qual item quer comprar? (escreva o nome certo...) Digite "sair" se quiser fechar a loja: ')
    while buy != 'sair' or loja == {}:
        if buy in loja:
            if dinheiro >= loja[buy]:
                itens_na_mochila.append(buy)
                dinheiro -= loja[buy]
                del(loja[buy])
                for i in loja:
                    print("-", i,":", buy, "reais")
                print ("\nVoce adicionou", i, "ao seu inventario e agora tem", dinheiro, "dinheiros")
                buy = input('Qual item quer comprar? (escreva o nome certo...) Digite "sair" se quiser fechar a loja: ')
            else:
                print ('Você não tem dinheiro pra comprar esse item... (é a crise)')
                buy = input('Qual item quer comprar? (escreva o nome certo...) Digite "sair" se quiser fechar a loja: ')
        else:
            print ('Esse item não existe... (escreveu certo?)')
            buy = input('Qual item quer comprar? (escreva o nome certo...) Digite "sair" se quiser fechar a loja: ')
    return (itens_na_mochila,dinheiro)


##### USAR ITEM #####
            
def use_item(nome_do_item, dados_do_item, vida_jogador, cap_hp, bag, itens_equip):
    ### Usa o item de acordo com a sua categoria
    contador_inventario=0
    if dados_do_item["efeito"] == "recupera hp": # Recupera vida
        if vida_jogador+dados_do_item["valor"] > cap_hp:
            vida_jogador = cap_hp
        else:
            vida_jogador+=dados_do_item["valor"]
        time.sleep(1)
        print("Voce está com", vida_jogador,"de vida")
        time.sleep(2)
        print()
        while nome_do_item != bag[contador_inventario]:
            contador_inventario+=1
        bag.remove(nome_do_item)
        return [vida_jogador, cap_hp, bag, itens_equip]
    
    elif dados_do_item["efeito"] == "arma": # Para equipar arma
        bag.append(itens_equip[0][0])
        itens_equip[0][0]=nome_do_item
        itens_equip[1][0]=dados_do_item["valor"]
        time.sleep(1)
        print("Voce equipou", nome_do_item)
        time.sleep(2)
        print()
        bag.remove(nome_do_item)
        return [vida_jogador, cap_hp, bag, itens_equip]
    
    elif dados_do_item["efeito"] == "armadura": # Para equipar armadura
        bag.append(itens_equip[0][1])
        itens_equip[0][1]=nome_do_item
        itens_equip[1][1]=dados_do_item["valor"]
        time.sleep(1)
        print("Voce equipou", nome_do_item)
        time.sleep(2)
        print()
        bag.remove(nome_do_item)
        return [vida_jogador, cap_hp, bag, itens_equip]
        
    elif dados_do_item["efeito"] == "chave": # Como usar chave???
        time.sleep(1)
        print("vai enfiar isso onde?")
        time.sleep(1)
        print("voce nao pode fazer o que esta pensando neste momento")
        time.sleep(2)
        print()
        return [vida_jogador, cap_hp, bag, itens_equip]
        
    elif dados_do_item["efeito"] == "leitura":  # Le o livro, bilhete, papel...
        time.sleep(1)
        print(dados_do_item["valor"])
        time.sleep(2)
        print()
        return [vida_jogador, cap_hp, bag, itens_equip]
    
        

##### O QUE CADA ITEM FAZ #####
        
def item_effects(itens_na_mochila, vida_jogador, cap_hp, itens_equip): # Recebe uma lista, a vida, a mochila e o equipamento
    tem_na_mochila={} # Mostra o que tem na mochila
    
    ### Dicionario com itens. Keys sao itens e value a categoria (efeito : recupera hp, armadura, arma, chave, leitura)
    with open('texto_itens.txt','r') as arquivo:
        conteudo = arquivo.read()
        efeito_dos_itens = json.loads(conteudo)
            
    ### Cria uma biblioteca com os itens que tem na mochila com seus respectivos values
    for i in itens_na_mochila:
        tem_na_mochila[i] = efeito_dos_itens[i]
        print(i, ":", tem_na_mochila[i]["descricao"])
    
    escolha_item=input("Digite o nome do item que quer usar ou 'sair' para escolher outra açao: ")
    print()
     #print([i, vida_jogador, itens_na_mochila, itens_equip])
    
    while True:
        if escolha_item == "sair":
            return [vida_jogador, cap_hp, itens_na_mochila, itens_equip]
        elif escolha_item in tem_na_mochila:
            for i in tem_na_mochila:
                if i == escolha_item:
                    return use_item(i, tem_na_mochila[i], vida_jogador, cap_hp, itens_na_mochila, itens_equip) # Retorna vida, mochila, equipamento nessa ordem
        print("Voce nao possui esse item ou digitou algo errado")
        time.sleep(1)
        escolha_item=input("Digite o nome do item que quer usar ou 'sair' para escolher outra açao: ")
        print()
    return vida_jogador, cap_hp, itens_na_mochila, itens_equip


##### ITENS QUE PODEM SER ENCONTRADOS NO MAPA #####

def show_possible_items(posicao_jogador, dicionario_itens_por_mapa):
    ### Dicionario com itens. Keys sao locais, Values sao outros dicionarios onde as Keys sao os itens e as values sao booleanos para saber se o jogador ja obteve o item ou não ###
    for i, k in dicionario_itens_por_mapa[posicao_jogador].items():
        if k == True:    # Se ele ja obteve o item, o nome aparece
            print("-"+ i)
        if k == False:    # Se ele não obteve o item, o nome não aparece
            print("-?????")
    
    
##### FUNCAO DE ACHAR ITENS #####
        
def find_items(posicao_jogador, dicionario_itens_no_mapa, dicionario_itens_por_mapa): #Essa funcao sera utilizada com um append?
    ### Dicionario com os itens que ainda não foram descobertos. Keys sao locais, Values são listas com os itens que ainda podem ser descobertos ###
    if len(dicionario_itens_no_mapa[posicao_jogador])!= 0:
        rng=random.randint(0,10)
        if rng>=4:
            rng_qual_item = random.randint(0,len(dicionario_itens_no_mapa[posicao_jogador])-1)
            time.sleep(1)
            print("Voce achou {0}".format(dicionario_itens_no_mapa[posicao_jogador][rng_qual_item]))
            give_to_player = dicionario_itens_no_mapa[posicao_jogador][rng_qual_item]
            del(dicionario_itens_no_mapa[posicao_jogador][rng_qual_item]) # Tira o item da lista
            dicionario_itens_por_mapa[posicao_jogador][give_to_player] = True # Seta que o player ja encontrou o item
            return [give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] # Retorna o que o jogador achou, a lista de itens no mapa e a lista de itens true/false
        else:
            time.sleep(1)
            print("Voce nao encontrou nenhum item") # Caso tenha falhado no "dado"
            give_to_player = None  # Isso nao vai funcionar do jeito que eu quero. Como fazer: criar uma lista que recebe esses returns >> teste com if?
            return [give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] # Retorna o que o jogador achou, a lista de itens no mapa e a lista de itens true/false
    else:
        time.sleep(1)
        print("Voce ja encontrou todos os itens deste lugar") # Caso ja tenha encontrado todos
        give_to_player = None  # Isso nao vai funcionar do jeito que eu quero. Como fazer: criar uma lista que recebe esses returns >> teste com if?
        return [give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] 
    

########## FIM SISTEMA DE ITENS ##########

    
########## SISTEMA DE CENARIOS ##########
        
##### SALA DO TELEPORTE #####    
    
def funcao_teleporte(destino,nivel,vida,dinheiro,cenarios):
    if nivel >= 3:
        if destino in cenarios:
            return (destino,dinheiro,vida)
        vida = vida - 5
        dinheiro = dinheiro - 5
        print("Essa sala não existe. Voce perdeu 5 de vida e 5 de dinheiro")
        return ("sala de teleporte",dinheiro,vida)
    print("Teleporte só pode ser usado a partir do nível 3!")
    return ("sala de teleporte",dinheiro,vida)
    
    
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
    with open("cenarios_json.txt", 'r') as arquivo:
        conteudo = arquivo.read()
        cenarios = json.loads(conteudo)
                
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    
    Raul = True
    
##### DICIONARIOS PARA SISTEMA DE ITENS #####

    itens_no_mapa = {     # Dicionario para find_items()
        "Saguao do perigo": ["moletom do D.A", "acai do contem","guarda chuva","calca do mickey"],
        "Caverna da tranquilidade": ["livro de python", "pochete","capacete de bike","oculos"],
        "Sala dos anciãos": ["pen drive do Raul"],
        "Arsenal da engenharia": ["prototipo quebrado", "jaleco", "pistola"],
        "Prédio da engenharia": ["Snickers","lata de coca","marmita","energetico"],
        "Arsenal insano":["Snickers","Tornno CNC", "furadeira portatil"],
        "Habitat da engenharia": ["armadura medieval","elastico"],
        "fabrica de relatório": ["ferro de solda portatil"],
        "habitat do fuka":["espada de papelao", "faca de plastico"],
        "Devolvam nosso aquárioo!!":["pipoca da maquina","salgadinho"]

        
        
        
        
    }

    itens_por_mapa = {     # Dicionario para show_possible_items()
        "Saguao do perigo": {"moletom do D.A":False , "acai do contem":False , "guarda chuva":False ,"calca do mickey":False 
           
        },
        "Caverna da tranquilidade": {"livro de python":False, "pochete":False,"capacete de bike":False,"oculos":False

        },
        "Prédio da engenharia": {"Snickers":False,"lata de coca":False,"marmita":False,"energetico":False

        },
        "Arsenal da engenharia":{"prototipo quebrado":False, "jaleco":False, "pistola":False
        
        },
        "Sala dos anciãos":{"pen drive do Raul":False
         
        },
        "Arsenal insano":{"Tornno CNC":False, "furadeira portatil":False
                   
        },
        "Habitat da engenharia": {"armadura medieval":False,"elastico":False
        
        },
        "fabrica de relatório": {"ferro de solda portatil":False
        },
                                 
        "habitat do fuka":{"espada de papelao":False, "faca de plastico":False
        },                   
                           
        "Devolvam nosso aquárioo!!":{"pipoca da maquina":False,"salgadinho":False
        }
        
                                  
    }
        
        

        

##### VARIAVEIS DO JOGADOR #####

    hp_jogador=400
    cap_hp=400
    ataque_base_jogador = 10
    mochila=["bilhete", "marmita", "carteirinha"]
    itens_equipados=[["baralho", "seu casaco"], [1, 1]]
    nivel_do_jogador=1
    cap_xp_jogador=1
    xp_do_jogador=0
    dinheiro = 0

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
    time.sleep(1)
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
        "adiamento do EP. Voce percebe que algo está estranho, o prédio vazio"
        "e tudo muito quieto. Ai voce pensa 'what the fuck is going on?'(boa sorte...)")
    time.sleep(4)
    
    print("")    

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
            

        imprimir_cenario(cenario_atual) # Imprime o cenario atual com o as descricoes e opcoes.
        
        if nome_cenario_atual == "tech lab":
            mochila = techlab(mochila)

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            escolha = input("Escolha uma ação:")        
            print()
            
            
            while (escolha == "itens do local" or escolha == "procurar itens" or escolha == "usar item" or escolha == "loja") and escolha in opcoes:   # Substituir por uma funcao?
                if escolha == "itens do local":
                    show_possible_items(cenario_atual["titulo"], itens_por_mapa)
                    
                if escolha == "procurar itens":
                    resultado_find_items=find_items(cenario_atual["titulo"], itens_no_mapa, itens_por_mapa)  #[give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] 
                    if resultado_find_items[0]!= None:
                        mochila.append(resultado_find_items[0])
                    itens_no_mapa = resultado_find_items[1]
                    itens_por_mapa = resultado_find_items[2]
                
                if escolha == "usar item":
                    hp_jogador, cap_hp, mochila, itens_equipados = item_effects(mochila, hp_jogador, cap_hp, itens_equipados)
                    
                if escolha == "batalhar":
                    hp_jogador, game_over, Raul = FUNCAO_COMBATE_RAUL(hp_jogador, cap_hp, ataque_base_jogador, itens_equipados, nivel_do_jogador, dinheiro, xp_do_jogador, cap_xp_jogador, game_over, Raul )
                
                if escolha == "loja":
                    mochila, dinheiro = buy_item(mochila,dinheiro)
                
                time.sleep(2)
                print()
                for i in cenario_atual["opcoes"]:
                    print(i,":",cenario_atual["opcoes"][i])
                escolha =  input("Escolha uma ação:")
                print()
            
            if escolha == "teleporte" and escolha in opcoes:
                if "pen drive do Raul" in mochila:
                    destino = input("Digite o nome da sala. Se voce errar existem penalidades: ")
                    nome_cenario_atual, hp_jogador, dinheiro = funcao_teleporte(destino, nivel_do_jogador, hp_jogador, dinheiro, cenarios)
                else:
                    print("Voce precisa do pen drive do Raul")
                    escolha = "andar professor"
            elif  escolha == "batalhar" and escolha in opcoes:
                hp_jogador, game_over, Raul = FUNCAO_COMBATE_RAUL (hp_jogador, cap_hp, ataque_base_jogador, itens_equipados, nivel_do_jogador, dinheiro, xp_do_jogador, cap_xp_jogador, game_over, Raul)
                
            elif escolha in opcoes:   # Tem que arrumar isso aqui?
                nome_cenario_atual = escolha 
                if escolha != ("professor" or "casa do pao de queijo" or "sala de teleporte"):
                    hp_jogador, cap_hp, nivel_do_jogador, xp_do_jogador, cap_xp_jogador, dinheiro, game_over = funcao_aparicao(hp_jogador, cap_hp, ataque_base_jogador, itens_equipados, nivel_do_jogador, cenario_atual["titulo"], dinheiro, xp_do_jogador, cap_xp_jogador, game_over)
                
            else:
                time.sleep(1)
                print("Sua indecisão foi sua ruína!")
                game_over = True
                
    if Raul == True:
        time.sleep(1)
        print("")
        print("Você morreu!")
    else:
        print("Parabéns a EP não foi adiada, porque o professor está no chão!")

# Programa principal.
if __name__ == "__main__":
    main()

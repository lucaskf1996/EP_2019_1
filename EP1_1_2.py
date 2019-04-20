# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 07:38:10 2019

@author: fuque
"""

import time
import random

########## SISTEMA DE ITENS ##########

##### USAR ITEM #####
            
def use_item(nome_do_item, dados_do_item, vida_jogador, bag, itens_equip):
    ### Usa o item de acordo com a sua categoria
    contador_inventario=0
    if dados_do_item["efeito"] == "recupera hp": # Recupera vida
        vida_jogador+=dados_do_item["valor"]
        time.sleep(1)
        print("Voce recuperou", dados_do_item["valor"])
        time.sleep(2)
        print()
        while nome_do_item != bag[contador_inventario]:
            contador_inventario+=1
        bag.remove(nome_do_item)
        return [vida_jogador, bag, itens_equip]
    
    elif dados_do_item["efeito"] == "arma": # Para equipar arma
        bag.append(itens_equip[0][0])
        itens_equip[0][0]=nome_do_item
        itens_equip[1][0]=dados_do_item["valor"]
        time.sleep(1)
        print("Voce equipou", nome_do_item)
        time.sleep(2)
        print()
        bag.remove(nome_do_item)
        return [vida_jogador, bag, itens_equip]
    
    elif dados_do_item["efeito"] == "armadura": # Para equipar armadura
        bag.append(itens_equip[0][1])
        itens_equip[0][1]=nome_do_item
        itens_equip[1][1]=dados_do_item["valor"]
        time.sleep(1)
        print("Voce equipou", nome_do_item)
        time.sleep(2)
        print()
        bag.remove(nome_do_item)
        return [vida_jogador, bag, itens_equip]
        
    elif dados_do_item["efeito"] == "chave": # Como usar chave???
        time.sleep(1)
        print("vai enfiar isso onde?")
        time.sleep(1)
        print("voce nao pode fazer o que esta pensando neste momento")
        time.sleep(2)
        print()
        return [vida_jogador, bag, itens_equip]
        
    elif dados_do_item["efeito"] == "leitura":  # Le o livro, bilhete, papel...
        time.sleep(1)
        print(dados_do_item["valor"])
        time.sleep(2)
        print()
        return [vida_jogador, bag, itens_equip]
    
        

##### O QUE CADA ITEM FAZ #####
        
def item_effects(itens_na_mochila, vida_jogador, itens_equip): # Recebe uma lista, a vida, a mochila e o equipamento
    tem_na_mochila={} # Mostra o que tem na mochila
    
    ### Dicionario com itens. Keys sao itens e value a categoria (efeito : recupera hp, armadura, arma, chave, leitura)
    efeito_dos_itens={
        "pao de queijo":{
                "descricao": "O potinho é melhor que o normal. Cura 3 pontos de vida",
                "efeito": "recupera hp", #alguma coisa
                "valor":3
        },
        "prototipo quebrado":{
                "descricao": "Nao serve pra mais nada. Parece bom pra bater nos amigos. Tem 1 de ataque. Pode ser equipado",
                "efeito": "arma", #alguma coisa
                "valor":1
        },
        "moletom do D.A":{
                "descricao": "Ele é ok. Tem 3 de defesa. Pode ser equipado",
                "efeito": "armadura",
                "valor": 3
        },
        "seu casaco":{
                "descricao": "Voce gosta dele e usou ele durante o Ensino Médio inteiro. Tem 1 de defesa. Pode ser equipado",
                "efeito": "armadura", #alguma coisa
                "valor":1
        },
        "faca de plastico":{
                "descricao": "Parece que foi um projeto de alguem na impressora 3D. Vai brincar la vai. Tem 3 de ataque. Pode ser equipado",
                "efeito": "arma",
                "valor": 3
        },
        "carteirinha":{
                "descricao": "Voce achou depois que passou pela catraca. OLHA ESSA FOTO HAHAHAHAHAHA",
                "efeito": "chave",
                "valor": None
        },
        "bilhete":{
                "descricao": 'Você perguntou pra um amigo onde era a sala do professor. Ele te deu isso',
                "efeito": "leitura",
                "valor": '"206 predio 1"\n É verdade esse bilhete?'
        },
        "ferro de solda portátil":{
                "descricao": "Nao sei se o problema vai ser o codigo de etica. Tem 6 de ataque. Pode ser equipado",
                "efeito": "arma",
                "valor": 6
        },
        "jaleco":{
                "descricao": "Pra nao estragar sua roupa. Tem 4 de defesa. Pode ser equipado",
                "efeito": "armadura",
                "valor": 4
        },
        "acai do contem":{
                "descricao": 'Nao. Isso nao tem gosto de terra. Cura 2 pontos de vida',
                "efeito": "recupera hp",
                "valor": 2
        },
        "lata de coca":{
                "descricao": "Nesse predio é mais barato. Recupera 2 pontos de vida",
                "efeito": "recupera hp",
                "valor": 1
        },
        "pipoca da maquina":{
                "descricao": "Alguem ja comeu isso? Recupera ???? ponto(s) de vida",
                "efeito": "recupera hp",
                "valor": random.randint(0,3)
        },
        "marmita":{
                "descricao": 'Professor pode esperar uma chepa ne? Recupera 5 pontos de vida',
                "efeito": "recupera hp",
                "valor": 5
        },
        "Snickers":{
                "descricao": 'Da aquela salvada entre as aulas. Cura 2 pontos de vida',
                "efeito": "recupera hp",
                "valor": 2
        },
        "livro de python":{
                "descricao": "COMO ODEIO PYTOHN. DA VONTADE DE JOGAR ISSO EM ALGUEM....\ne se.... Pode ser equipado",
                "efeito": "arma",
                "valor": 4
        },
        "espada de papelao":{
                "descricao": "Caramba. Quem ta espalhando essas coisas pela facul??? Tem 3 de ataque. Pode ser equipado",
                "efeito": "arma",
                "valor": 3
        },
        "pochete":{
                "descricao": 'Nao protege nada e é a maior vergonha usar essa coisa. Tem 2 de defesa. Pode ser equipado',
                "efeito": "armadura",
                "valor": 2
        },
        "convite para festa":{
                "descricao": '"Corote Xperience"\nA festa é hoje. Sera que o professor adia a EP pra depois de amanha?',
                "efeito": "leitura",
                "valor": None
        },
        "pistola":{
                "descricao": 'É a de cola quente, mas imaginacao é tudo. Tem 5 de ataque. Pode ser equipado',
                "efeito": "arma",
                "valor": 5
        },
        "armadura medieval":{
                "descricao": "Tava ficando sem ideia ja. Me quebra um galho ae. Tem 6 de ataque. Pode ser equipado",
                "efeito": "armadura",
                "valor": 6
        },
        "cafe":{
                "descricao": "S2. Recupera 2 pontos de vida",
                "efeito": "recupera hp",
                "valor": 3
        },
        "baralho":{
                "descricao": 'Pro truco durante o almoco. Só cuidado pra nao jogar no olho dos outros. Tem 1 de ataque. Pode ser equipado',
                "efeito": "arma",
                "valor": 1
        },
        "Torno CNC":{
                "descricao": 'Como que voce... mas...... quer saber, foda-se. Tem 10 de ataque. Pode ser equipado',
                "efeito": "arma",
                "valor": 10
        },
        "furadeira portatil":{
                "descricao": 'Ta sem pilha, relaxa. Tem 7 de ataque. Pode ser equipado',
                "efeito": "arma",
                "valor": 7
        }
    }
            
    ### Cria uma biblioteca com os itens que tem na mochila com seus respectivos values
    for i in itens_na_mochila:
        tem_na_mochila[i] = efeito_dos_itens[i]
        print(i, ":", tem_na_mochila[i]["descricao"])
    
    escolha_item=input("Digite o nome do item que quer usar ou 'sair' para escolher outra açao: ")
    print()
     #print([i, vida_jogador, itens_na_mochila, itens_equip])
    
    while True:
        if escolha_item == "sair":
            return [vida_jogador, itens_na_mochila, itens_equip]
        elif escolha_item in tem_na_mochila:
            for i in tem_na_mochila:
                if i == escolha_item:
                    return use_item(i, tem_na_mochila[i], vida_jogador, itens_na_mochila, itens_equip) # Retorna vida, mochila, equipamento nessa ordem
        print("Voce nao possui esse item ou digitou algo errado")
        time.sleep(1)
        escolha_item=input("Digite o nome do item que quer usar ou 'sair' para escolher outra açao: ")
        print()
    return vida_jogador, itens_na_mochila, itens_equip


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
        if destino == cenarios:
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
                "descricao": "Se teleportar para outro cenário pode ser útil...",
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

            escolha = input("Escolha uma ação:")        
            print()
            
            
            while (escolha == "itens do local" or escolha == "procurar itens" or escolha == "usar item") and escolha in opcoes:   # Substituir por uma funcao?
                if escolha == "itens do local":
                    show_possible_items(cenario_atual["titulo"], itens_por_mapa)
                    
                if escolha == "procurar itens":
                    resultado_find_items=find_items(cenario_atual["titulo"], itens_no_mapa, itens_por_mapa)  #[give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] 
                    if resultado_find_items[0]!= None:
                        mochila.append(resultado_find_items[0])
                    itens_no_mapa = resultado_find_items[1]
                    itens_por_mapa = resultado_find_items[2]
                
                if escolha == "usar item":
                    hp_jogador, mochila, itens_equipados = item_effects(mochila, hp_jogador, itens_equipados)
                
                opcoes = cenario_atual['opcoes']
                
                escolha =  input("Escolha uma ação:")
                print()
               
            if escolha in opcoes:   # Tem que arrumar isso aqui?
                nome_cenario_atual = escolha
            else:
                time.sleep(1)
                print("Sua indecisão foi sua ruína!")
                game_over = True
    time.sleep(1)
    print("")
    print("Você morreu!")

# Programa principal.
if __name__ == "__main__":
    main()

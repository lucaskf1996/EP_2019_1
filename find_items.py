# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:03:33 2019

@author: fuque
"""

##### FUNCAO DE ACHAR ITENS #####
        
def find_items(posicao_jogador, dicionario_itens_no_mapa, dicionario_itens_por_mapa, flag): #Essa funcao sera utilizada com um append?
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
            if flag == 1:
                time.sleep(1)
                print("Voce nao encontrou nenhum item") # Caso tenha falhado no "dado"
                give_to_player = None  # Isso nao vai funcionar do jeito que eu quero. Como fazer: criar uma lista que recebe esses returns >> teste com if?
                return [give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] # Retorna o que o jogador achou, a lista de itens no mapa e a lista de itens true/false
    else:
        time.sleep(1)
        print("Voce ja encontrou todos os itens deste lugar") # Caso ja tenha encontrado todos
        give_to_player = None  # Isso nao vai funcionar do jeito que eu quero. Como fazer: criar uma lista que recebe esses returns >> teste com if?
        return [give_to_player, dicionario_itens_no_mapa, dicionario_itens_por_mapa] 
    

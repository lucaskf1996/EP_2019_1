# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:02:23 2019

@author: fuque
"""
##### ITENS QUE PODEM SER ENCONTRADOS NO MAPA #####

def show_possible_items(posicao_jogador, dicionario_itens_por_mapa):
    ### Dicionario com itens. Keys sao locais, Values sao outros dicionarios onde as Keys sao os itens e as values sao booleanos para saber se o jogador ja obteve o item ou não ###
    for i, k in dicionario_itens_por_mapa[posicao_jogador].items():
        if k == True:    # Se ele ja obteve o item, o nome aparece
            print("-"+ i)
        if k == False:    # Se ele não obteve o item, o nome não aparece
            print("-?????")
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 16:00:48 2019

@author: fuque
"""

##### USAR ITEM #####
            
def use_item(nome_do_item, vida_jogador, bag, itens_equip):
    ### Usa o item de acordo com a sua categoria
    contador_inventario=0
    if nome_do_item["efeito"] == "recupera hp": # Recupera vida
        vida_jogador+=nome_do_item["valor"]
        return [vida_jogador, bag, itens_equip]
    
    elif nome_do_item["efeito"] == "arma": # Para equipar arma
        bag.append(itens_equip[0][0])
        for i in nome_do_item:
            itens_equip[0][0]= i
        while nome_do_item != bag[contador_inventario]:
            contador_inventario+=1
        del(bag[contador_inventario])
        return [vida_jogador, bag, itens_equip]
    
    elif nome_do_item["efeito"] == "armadura": # Para equipar armadura
        bag.append(itens_equip[0][1])
        for i in nome_do_item:
            itens_equip[0][1]= i
        while nome_do_item != bag[contador_inventario]:
            contador_inventario+=1
        del(bag[contador_inventario])
        return [vida_jogador, bag, itens_equip]
        
    elif nome_do_item["efeito"] == "chave": # Como usar chave???
        time.sleep(1)
        print("vai enfiar isso onde?")
        time.sleep(1)
        print("voce nao pode fazer o que esta pensando neste momento" )
        return [vida_jogador, bag, itens_equip]
        
    elif nome_do_item["efeito"] == "leitura":  # Le o livro, bilhete, papel...
        time.sleep(1)
        print(nome_do_item["valor"])
        return [vida_jogador, bag, itens_equip]
    
        

##### O QUE CADA ITEM FAZ #####
        
def item_effects(itens_na_mochila, vida_jogador, bag, itens_equip): # Recebe uma lista, a vida, a mochila e o equipamento
    tem_na_mochila={} # Mostra o que tem na mochila
    
    ### Dicionario com itens. Keys sao itens e value a categoria (efeito : recupera hp, armadura, arma, chave, leitura)
    efeito_dos_itens={
        "nome do item":{
                "descricao": "",
                "efeito": "", #alguma coisa
                "valor":"",
                "descoberto": ""
        }
    }
            
    ### Cria uma biblioteca com os itens que tem na mochila com seus respectivos values
    for i in itens_na_mochila:
        tem_na_mochila[i] = efeito_dos_itens[i]
        print(tem_na_mochila[i], ":", tem_na_mochila[i]["descricao"])
    
    escolha_item=input("Digite o nome do item que quer usar ou 'sair' para escolher outra açao:")
    
    while escolha_item not in tem_na_mochila or escolha_item != "sair": # Enquanto não digitar sair ou um item na mochila
        print("Voce nao possui esse item ou digitou algo errado")
        escolha_item= input("Digite o nome do item que quer usar ou 'sair' para escolher outra açao:")
    
    if escolha_item in tem_na_mochila:
        for i in tem_na_mochila:
            if i == escolha_item:
                return use_item(i, vida_jogador, itens_na_mochila, itens_equip) # Retorna vida, mochila, equipamento nessa ordem

##### USAR ITEM #####
            
def use_item(nome_do_item, dados_do_item, vida_jogador, bag, itens_equip):
    ### Usa o item de acordo com a sua categoria
    contador_inventario=0
    if dados_do_item["efeito"] == "recupera hp": # Recupera vida
        vida_jogador+=dados_do_item["valor"]
        while nome_do_item != bag[contador_inventario]:
            contador_inventario+=1
        bag.remove(nome_do_item)
        return [vida_jogador, bag, itens_equip]
    
    elif dados_do_item["efeito"] == "arma": # Para equipar arma
        bag.append(itens_equip[0][0])
        itens_equip[0][0]=nome_do_item
        itens_equip[1][0]=dados_do_item["valor"]
        bag.remove(nome_do_item)
        return [vida_jogador, bag, itens_equip]
    
    elif dados_do_item["efeito"] == "armadura": # Para equipar armadura
        bag.append(itens_equip[0][1])
        itens_equip[0][1]=nome_do_item
        itens_equip[1][1]=dados_do_item["valor"]
        bag.remove(nome_do_item)
        return [vida_jogador, bag, itens_equip]
        
    elif dados_do_item["efeito"] == "chave": # Como usar chave???
        time.sleep(1)
        print("vai enfiar isso onde?")
        time.sleep(1)
        print("voce nao pode fazer o que esta pensando neste momento")
        return [vida_jogador, bag, itens_equip]
        
    elif dados_do_item["efeito"] == "leitura":  # Le o livro, bilhete, papel...
        time.sleep(1)
        print(nome_do_item["valor"])
        return [vida_jogador, bag, itens_equip]
    
        

##### O QUE CADA ITEM FAZ #####
        
def item_effects(itens_na_mochila, vida_jogador, itens_equip): # Recebe uma lista, a vida, a mochila e o equipamento
    tem_na_mochila={} # Mostra o que tem na mochila
    
    ### Dicionario com itens. Keys sao itens e value a categoria (efeito : recupera hp, armadura, arma, chave, leitura)
    efeito_dos_itens={
        "comida_teste":{
                "descricao": "comida para teste",
                "efeito": "recupera hp", #alguma coisa
                "valor":1,
                "descoberto": True
        },
        "espada_teste":{
                "descricao": "arma para teste",
                "efeito": "arma", #alguma coisa
                "valor":1,
                "descoberto": True
        },
        "armadura_teste":{
                "descricao": "armadura para teste",
                "efeito": "armadura",
                "valor": 1,
                "descoberto": True
        },
        "espada_teste2":{
                "descricao": "arma para teste 2",
                "efeito": "arma", #alguma coisa
                "valor":0,
                "descoberto": True
        },
        "armadura_teste2":{
                "descricao": "armadura para teste 2",
                "efeito": "armadura",
                "valor": 0,
                "descoberto": True
        },
        "chave_teste":{
                "descricao": "chave para teste",
                "efeito": "chave",
                "valor": None,
                "descoberto": True
        },
        "livro_teste":{
                "descricao": "livro para teste",
                "efeito": "leitura",
                "valor": "Esse tipo de item vai imprimir isso",
                "descoberto": True
        }
    }
            
    ### Cria uma biblioteca com os itens que tem na mochila com seus respectivos values
    for i in itens_na_mochila:
        tem_na_mochila[i] = efeito_dos_itens[i]
        print(i, ":", tem_na_mochila[i]["descricao"])
    
    escolha_item=input("Digite o nome do item que quer usar ou 'sair' para escolher outra açao: ")
    
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


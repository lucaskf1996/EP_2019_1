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
                "valor": 2
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

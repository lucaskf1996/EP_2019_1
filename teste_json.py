# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:57:31 2019

@author: FUKADA
"""
import random

itens={"pao de queijo":{
                "descricao": "O potinho é melhor que o normal. Cura 3 pontos de vida",
                "efeito": "recupera hp", #alguma coisa
                "valor":10
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
        "ferro de solda portatil":{
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
                "valor": 10
        },
        "lata de coca":{
                "descricao": "Nesse predio é mais barato. Recupera 2 pontos de vida",
                "efeito": "recupera hp",
                "valor": 5
        },
        "pipoca da maquina":{
                "descricao": "Alguem ja comeu isso? Recupera ???? ponto(s) de vida",
                "efeito": "recupera hp",
                "valor": random.randint(0,10)
        },
        "marmita":{
                "descricao": 'Professor pode esperar uma chepa ne? Recupera 5 pontos de vida',
                "efeito": "recupera hp",
                "valor": 20
        },
        "Snickers":{
                "descricao": 'Da aquela salvada entre as aulas. Cura 2 pontos de vida',
                "efeito": "recupera hp",
                "valor": 5
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
        "pen drive do Raul":{
                "descricao": 'Serve para entrar na sala de teleporte (é o computador do raul)',
                "efeito": "chave",
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
        },
        "salgadinho":{
                "descricao": 'Cheetos de requeijao é uma merda. Recupera 1 ponto de vida',
                "efeito": "recupera hp",
                "valor": 1
        },
        "elastico":{
                "descricao": 'Se fizer uma arma na cortadora a laser fica nice. Tem 2 de ataque. Pode ser equipado',
                "efeito": "arma",
                "valor": 2
        },
        "guarda chuva":{
                "descricao": 'Sempre bom estar preparado. Tem 3 de ataque. Pode ser equipado',
                "efeito": "arma",
                "valor": 3
        },
        "energetico":{
                "descricao": 'RedBull é mó caro. Recupera 3 pontos de vida',
                "efeito": "recupera hp",
                "valor": 3
        },
        "capacete de bike":{
                "descricao": 'Venha de bicicleta. Tem 3 de defesa. Pode ser equipado',
                "efeito": "armadura",
                "valor": 3
        },
        "oculos":{
                "descricao": 'Ninguem bate em uma pessoa de oculos. Tem 10 de defesa. Pode ser equipado',
                "efeito": "armadura",
                "valor": 10
        },
        "aparelho fixo":{
                "descricao": 'Ja tomo uma bolada de aparelho? Tem -3 de defesa. Pode ser equipado',
                "efeito": "armadura",
                "valor": -3
        },
        "foda-se":{
                "descricao": 'É isso. Tem 100000000000 de ataque. Pode ser equipado',
                "efeito": "arma",
                "valor": 100000000000
        },
        "calca do mickey":{
                "descricao": '. Tem 7 de defesa. Pode ser equipado',
                "efeito": "armadura",
                "valor": 7
        }
    }
        
import json
   
itens_json= json.dumps(itens)

with open('texto_itens.txt','w') as texto_itens:
    texto_itens.write(itens_json)

    
with open('texto_itens.txt','r') as arquivo:
    conteudo = arquivo.read()
    itens = json.loads(conteudo)

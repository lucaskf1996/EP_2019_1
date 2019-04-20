# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:49:57 2019

@author: User
"""
 
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
        "marmita":{
                "descricao": "Professor pode esperar uma chepa ne? Recupera 5 pontos de vida",
                "efeito": "recupera hp",
                "valor": 5
        },
        "Snickers":{
                "descricao": "Da aquela salvada entre as aulas. Cura 2 pontos de vida",
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
        
      
        
def funcao_teleporte(destino,nivel,vida,dinheiro,cenarios):
    if nivel >= 3:
        if destino == cenarios:
            return (destino,dinheiro,vida)
        vida = vida - 5
        dinheiro = dinheiro - 5
        return ("sala de teleporte",dinheiro,vida)
    print("Teleporte só pode ser usado a partir do nível 3!")
    return ("sala de teleporte",dinheiro,vida)


def nivel_e_xp(nivel_jogador, xp, cap_xp):
    xp_jogador = 0 #AVERIGUAR
    if xp_jogador+1==cap_xp:
        nivel_jogador+=1
        cap_xp*=2
        xp_jogador=0
    else:
        xp_jogador+=1
    return [nivel_jogador, xp, cap_xp]



import random
def funcao_aparicao(vida_jogador, vida_inimigo, ataque_jogador, ataque_inimigo, itens_equipados, nivel_jogador, posicao, dinheiro, xp, iniciar_combate):
    chance = random.randint(1,7)
    
    if chance == 1:
        vida_jogador, dinheiro, nivel_jogador, xp = FUNCAO_COMBATE (vida_jogador, vida_inimigo, ataque_jogador, ataque_inimigo, itens_equipados, nivel_jogador, posicao, dinheiro, xp)
        iniciar_combate = input ("Iniciar ataque: escreva 'start': ")
        print (iniciar_combate)
    return vida_jogador,dinheiro,nivel_jogador,xp


       

def FUNCAO_COMBATE (vida_jogador, vida_inimigo, ataque_jogador, ataque_inimigo, itens_equipados, nivel_jogador, posição, dinheiro, xp, iniciar_combate): #itens_equipados[1][0]
    itens_equipados = [["baralho", "seu casaco"], [1, 1]]
    
    if iniciar_combate == 'start' or 'Start' or 'START':
        print ("pressione 'a' para atacar!!")
        a = input("")
    else:
        print ("pressione 'a' para atacar!!")
        
        from contextlib import contextmanager
        import threading
        import _thread
        
        class TimeoutException(Exception):
            def __init__(self, msg=''):
                self.msg = msg
        
        @contextmanager
        def tempo_combate(seconds, msg=''):
            timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
            timer.start()
            try:
                yield
            except KeyboardInterrupt:
                raise TimeoutException("Timed out for operation {}".format(msg))
            finally:
                # if the action ends in specified time, timer is canceled
                timer.cancel()
        
        import time
        # ends after 60 seconds - ***ainda a definir tempo de duração de batalha***
        time_limit = 61        
        with time_limit(61, 'sleep'):
            
            while time.sleep(60):
               ataque_monstro = 10
               ataque_monstro += (xp + nivel_jogador * 0.5)
               vida_monstro = 400
               vida_monstro += (xp + nivel_jogador) * 0.5
               
               class TimeoutException(Exception):
                   def __init__(self, msg=''):
                        self.msg = msg
                
                @contextmanager
                def time_limit(seconds, msg=''):
                    timer = threading.Timer(seconds, lambda: _thread.interrupt_main())
                    timer.start()
                    try:
                        yield
                    except KeyboardInterrupt:
                        raise TimeoutException("Timed out for operation {}".format(msg))
                    finally:
                        # if the action ends in specified time, timer is canceled
                        timer.cancel()
                
                import time
                
                with time_ataque_monstro(2, 'sleep'):
                    while time.sleep(1):
                    vida_monstro -= a
                    vida_jogador -= ataque_monstro
                    return vida_monstro
                        
               
               
               if a == input(""):
                    a = 10
                    a += itens_equipados[1][0]
                    print (input(""))
                    return input("")

                
              
        
        

                
                
                    
                
                    
                 
                 
                
                
                     
                    
                 
        
    
    
        
    
    
    
    
    
    
    
    
    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:14:09 2019

@author: User
"""

import json


cenarios = {
    "inicio": {
        "titulo": "Saguao do perigo",
        "descricao": "Voce esta no saguao de entrada do Insper",
        "opcoes": {
            "andar professor": "Tomar o elevador para o andar do professor",
            "biblioteca": "Ir para a biblioteca",
            "itens do local": "Mostra uma lista com os itens que foram encontrados",
            "procurar itens": "Tenta achar um item no local",
            "casa do pao de queijo": "Um pao de queijo seria bem nice agora",
            "4 andar":"voltar"
        }
    },
        
    "andar professor": {
        "titulo": "Andar do desespero",
        "descricao": "Voce chegou ao andar da sala do seu professor",
        "opcoes": {
            "inicio": "Tomar o elevador para o saguao de entrada",
            "itens do local": "Mostra uma lista com os itens que foram encontrados",
            "procurar itens": "Tenta achar um item no local",
            "sala do teleporte": "Se teleportar para outro cenário pode ser útil...",
            "professor": "Falar com o professor"
        }
    },
        
    "professor": {
        "titulo": "O monstro do Python",
        "descricao": "Voce foi pedir para o professor adiar o EP. "
                     "O professor revelou que é um monstro "
                     "e voce ve que é hora de batalhar.",
        "opcoes": {
            "batalhar": "É só isso. Não tem mais jeito. Acabou. Boa sorte..."
        }
    },
    
    "biblioteca": {
        "titulo": "Caverna da tranquilidade",
        "descricao": "Voce esta na biblioteca",
        "opcoes": {
            "inicio": "Voltar para o saguao de entrada",
            "itens do local": "Mostra uma lista com os itens que foram encontrados",
            "procurar itens": "Tenta achar um item no local",
            "sala das entidades": "Ir para a sala das entidades"
        }
    },
        
    "sala de teleporte": {
        "titulo": "Computador do Raul",
        "descricao": "Se teleportar para outro cenário pode ser útil...",
        "opcoes": {
            "teleporte": "Escreva o nome correto do local, ou...",
            "andar professor": "Tomar o elevador para o andar do professor",
            "itens do local": "Mostra uma lista com os itens que foram encontrados"
        }
    },
        
    "casa do pao de queijo":{
        "titulo": "PAO DE QUEIJOOOO",
        "descricao":"SIM",
        "opcoes":{
            "inicio": "Voltar para o saguao de entrada",
            "loja": "Comprar comidinha"
        }
    },
    
    "sala de entidades":{
        "titulo": "Sala dos anciãos",
        "descricao": "",
        "opcoes":{
            "itens do local": "Mostra uma lista com os itens que foram encontrados",
            "procurar itens": "Tenta achar um item no local",
            "biblioteca": "Ir para a biblioteca"
        }
    },
    
    "fab lab":{
        "titulo": "Arsenal da engenharia",
        "descricao": "Onde o engenheiro se equipa para batalha",
        "opcoes":{
            "prédio 2": "Ir para o saguão do prédio 2",
            "itens do local": "Mostra uma lista com os itens que foram encontrados",
            "procurar itens": "Tenta achar um item no local"
        }
    },
    "predio 2":{
        "titulo": "Prédio da engenharia",
        "descricao": "FORA ADM/ECONO",
        "opcoes":{
            "fab lab": "Ir para o fab lab",
            "inicio": "Ir para o prédio 1",
            "itens do local": "Mostra uma lista com os itens que foram encontrados",
            "procurar itens": "Tenta achar um item no local"
        }
    },
    "tech lab":{
        "titulo": "Arsenal insano",
        "descricao": "Só para os guerreiros",
        "opcoes":{
            "inicio": "Voltar para o saguao de entrada",
            "itens do local": "Mostra uma lista com os itens que foram encontrados",
            "procurar itens": "Tenta achar um item no local"
        }
    },
    "4 andar":{
            "titulo": "Habitat da engenharia",
            "descricao": "great again",
            "opcoes":{
                "inicio": "Voltar para o saguao de entrada",
                "itens do local": "Mostra uma lista com os itens que foram encontrados",
                "procurar itens": "Tenta achar um item no local",
                "habitat do fukada": "vai la mongar",
                "lab instrumed": "indo encontrar o Carlitos"
            }
     },
        
    "lab instrumed":{
        "titulo": "fabrica de relatório",
        "descricao": "indo encontrar o Carlitos",
        "opcoes": {
                "4 andar":"voltar",
                "itens do local": "Mostra uma lista com os itens que foram encontrados",
                "procurar itens": "Tenta achar um item no local"
                
                }
    },
    "habitat do Fuka":{
            "titulo": "habitat do fuka",
            "descricao": "provavelmente mongando",
            "opcoes":{
                    "4 andar":"voltar",
                    "itens do local": "Mostra uma lista com os itens que foram encontrados",
                    "procurar itens": "Tenta achar um item no local"
                    
                }
    },
    "aquario":{
            "titulo": "Devolvam nosso aquárioo!!",
            "descricao": "Só engenharia, por favor.",
            "opcoes":{
                    "predio 2": "sair do aquário (tem certeza? Eles podem roubar)",
                    "itens do local": "Mostra uma lista com os itens que foram encontrados",
                    "procurar itens": "Tenta achar um item no local"                                               
                }
    }
}
            
cenarios = json.dumps(cenarios)
with open("cenarios_json.txt", 'w') as conteudo:
    conteudo.write(cenarios)
    
with open("cenarios_json.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    cenarios = json.loads(conteudo)
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:46:16 2019

@author: fuque
"""
##### O QUE PRECISA FAZER? #####
'''
CADA MONSTRO DA 1 DE XP
'''

def nivel_e_xp(nivel_jogador, xp_jogador, cap_xp):
    if xp_jogador+1==cap_xp:
        nivel_jogador+=1
        cap_xp*=2
        xp_jogador=0
    else:
        xp_jogador+=1
    return [nivel_jogador, xp_jogador, cap_xp]


''' Area de teste
nivel_do_jogador=1
cap_xp_jogador=1
xp_do_jogador=0

Exercício Programa - 2019/1 - Design de Software
------------------------------------------------

Alunos: 
- Lucas Keichi Fukada, lucaskf@al.insper.edu.br
- Sicrano de Almeida, sicranoa1@insper.edu.br

------------------------------------------------
Só queria que esse pesadelo acabasse =(

O que precisa fazer:

-EXTRA: ROLA UM FORTH WALL BREAK?

-COMBATE: PEDRA/PAPEL/TESOURA, PAR OU IMPAR, JRPG, QUEM APERTA MAIS (TEMPO DE MAQUINA), PUZZLE, CHARADA, SORTEIO, PACIFIST RUN (SEM MATAR)?, HOMICIDE RUN(SANGUEEEEEE)? FUNCAO_DE_COMBATE(VIDA_JOGADOR, ATAQUE_JOGADOR, ARMADURA_JOGADOR, NIVEL): RETURN (VIDA_JOGADOR, DINHEIRO, XP)

-INIMIGO: RAUL/HUMBERTO FUNCAO_DE_COMBATE(VIDA_JOGADOR, ATAQUE_JOGADOR, ARMADURA_JOGADOR): RETURN (VIDA_JOGADOR, DINHEIRO, XP)

-APARIÇÃO DE MONSTROS: TODA VEZ QUE ENTRA NA SALA, TEM CHANCE. FUNCA_APARICAO(POSICAO_JOGADOR, VIDA_JOGADOR, ATAQUE_JOGADOR, ARMADURA_JOGADOR, NIVEL): CHAMA FUNCAO_DE_COMBATE. RETURN (VIDA_JOGADOR, ATAQUE_JOGADOR, ARMADURA_JOGADOR, NIVEL)

-INVENTARIO: ADQUIRIR ITENS QUANDO PASSA POR CERTAS SALAS. SERVEM PARA PERMITIR ACESSO A OUTRAS SALAS. "EXPLORE" FEATURE("JOGA UM DADO" PARA VER SE ACHA ITEM. DEVE MOSTRAR UMA LISTA QUANTOS ITENS SAO POSSIVEIS DE ENCONTRAR NA SALA/CENA, EX: "-????, -????, -ESPADA".)

-TELEPORTE: CONTEXTO COMUM PARA EASTER EGGS MAIS FACEIS. CASTIGO?

-JSON PARA DESCRIÇÃO DA CENA É O QUE A GENTE APRENDEU HJ

-FEATURE EXTRA 1: NÍVEL? MULTIPLICADOR (ENTRA NO SISTEMA DE COMBATE)

-FEATURE EXTRA 2: SAVE STATE? (Use pickle lib?https://stackoverflow.com/questions/18606097/python-text-game-how-to-make-a-save-feature)

-FEATURE EXTRA 3: DINHEIRO + LOJA? ENTRA NO SISTEMA DE COMBATE. INTEGRADO SISTEMA DE NIVEL. INTEGRADO SISTEMA DE ITEM

-FEATURE EXTRA 4?: ITENS ALEATORIOS NO MAPA
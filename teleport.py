def funcao_teleporte(destino,nivel,vida,dinheiro,cenarios):
    if nivel >= 3:
        if destino == cenarios:
            return (destino,dinheiro,vida)
        vida = vida - 5
        dinheiro = dinheiro - 5
        return ("sala de teleporte",dinheiro,vida)
    print("Teleporte só pode ser usado a partir do nível 3!")
    return ("sala de teleporte",dinheiro,vida)

    

def buy_item(itens_na_mochila,dinheiro):
    loja = {
  'protótipo quebrado' : 10
, 'pochete': 15
, 'lata de coca': 15
, 'espada de papelão': 20
}
    print (loja)
    print (dinheiro)
    buy = input('Qual item quer comprar? (escreva o nome certo...) Digite "sair" se quiser fechar a loja')
    while buy != 'sair':
        if buy in loja:
            if dinheiro >= loja[buy]:
                itens_na_mochila.append[buy]
                dinheiro -= loja[buy]
                del(loja[buy])
                print(loja)
                print(dinheiro)
                buy = input('Qual item quer comprar? (escreva o nome certo...) Digite "sair" se quiser fechar a loja')
             else:
                print ('Você não tem dinheiro pra comprar esse item... (é a crise)')
                buy = input('Qual item quer comprar? (escreva o nome certo...) Digite "sair" se quiser fechar a loja')
        else:
            print ('Esse item não existe... (escreveu certo?)')
            buy = input('Qual item quer comprar? (escreva o nome certo...)')
    return (itens_na_mochila,dinheiro)

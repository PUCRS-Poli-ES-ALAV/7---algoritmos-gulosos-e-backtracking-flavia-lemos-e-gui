def problema_troco(valor, moedas):
    S = [] #conjunto da solução
    s = 0 #soma dos itens em S
    while s != valor:
        if (moedas == []):
            break
        x = max(moedas)
        y = x + s
        if (x + s <= valor):
            S.append(x)
            s = s + x
        else:
            moedas.remove(x) 

    return S

print (problema_troco(2.89, [1, 0.25, 0.10, 0.05, 0.01]))
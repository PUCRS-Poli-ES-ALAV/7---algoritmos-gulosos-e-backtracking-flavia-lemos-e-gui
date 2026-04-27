def SDM_Guloso (s, f, n):
    f_i= -1000
    X = []
    i = 0
    iteracoes = 0 
    for k in range(1, n+1):
        iteracoes +=1
        if(s[k-1] > f_i):
            X.append(k)
            i = k
            f_i = f[k-1]
    return X, iteracoes

s = [2, 4, 6, 9, 6, 7, 9,  3, 13, 1,  9]
f = [4, 5, 7, 6, 9, 10, 11, 13, 14, 6, 12]
n = len(s)

X, iteracoes = SDM_Guloso(s, f, n)

print(f"s = {s}")
print(f"f = {f}")
print(f"SDM (índices): {X}")
print(f"Tamanho da SDM: {len(X)}")
print(f"Iterações: {iteracoes}")

s = [6, 9, 7, 18,1,23,25,30]
f = [15, 15, 16, 24, 26, 28, 30, 34]
n = len(s)

X, iteracoes = SDM_Guloso(s, f, n)

print(f"s = {s}")
print(f"f = {f}")
print(f"SDM (índices): {X}")
print(f"Tamanho da SDM: {len(X)}")
print(f"Iterações: {iteracoes}")

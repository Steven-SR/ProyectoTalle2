"""
Dominio: El tablero hatsa ese punto, la pieza a probar, las posiciones de movimiento
y el punto a llenar
Codominio: Si logra colocar la pieza, el tablero con la pieza colocada y un True
sino, el tablero original y un falso
"""
def move(T, cpiz,i,j,x,y):
    newT = [row[:] for row in T] 
    if canplace(newT, cpiz, i, j):
        for oi in range(len(cpiz)):
            for oj in range(len(cpiz[0])):
                if cpiz[oi][oj]!='.':
                    newT[oi + i][oj + j] = cpiz[oi][oj]
        if newT[x][y]!='.':
            return newT, True
    return T, False

"""
Dominio: El tablero hatsa ese punto, la pieza a probar, las posiciones de movimiento
Codominio: Verdaero si puede colocar la pieza, falso si no
"""
def canplace(T, piZ, i, j):
    for oi in range(len(piZ)):
        for oj in range(len(piZ[0])):
            if oi + i >= len(T) or oj + j >= len(T[0]) or T[oi + i][oj + j] != ".":
                if piZ[oi][oj]!='.':
                        return False
    return True

"""
Dominio: Una matriz, en este caso una pieza
Codominio: Otra matriz, que es una versión recortada de la que entró
"""
def cropM(M):
    Mempty = []
    Mtrans = []
    for fila in M:
        if not all(dotn == '.' for dotn in fila):
            Mempty.append(fila)
    for j in range(len(Mempty[0])):
        columna = [Mempty[i][j] for i in range(len(Mempty))]
        if not all(dotn == '.' for dotn in columna):
            Mtrans.append(columna)
    res = []
    for j in range(len(Mtrans[0])):
        fila = [Mtrans[i][j] for i in range(len(Mtrans))]
        res.append(fila)
    return res

"""
Dominio: Una matriz y un numero de "giros" a hacer
Codominio: La matriz rotada correspondiente
"""
def rotate(X, n):
    temp = [row[:] for row in X]  
    for _ in range(n):
        temp = flip(transpose(temp))
    if n > 4:
        return flip(temp)
    return temp

"""
Dominio: Una matriz
Codominio: La version transpuesta de la matriz
"""
def transpose(A):
    return [[A[j][i] for j in range(len(A[0]))] for i in range(len(A))]

"""
Dominio: Una matriz
Codominio: Una matriz, con las filas volteadas
"""
def flip(A):
    return [row[::-1] for row in A]

"""
Dominio: Una matriz
Codominio: Las coordenadas de el primer punto enconrado
"""
def nextpos(T):
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]=='.':
                return (i,j)

"""
Dominio: La matriz tablero, la lista con las piezas y el primer '.' a llenar
Codominio: Una matriz que en caso posible esta llena con las piezas
"""
def call(Tab, final,npos): 
    if not final:
        return Tab
    for actPiz in final:
        rotations = [rotate(actPiz, h) for h in range(1, 9)]
        ogTab = [row[:] for row in Tab] 
        for i in range(len(Tab)+1):
            for j in range(len(Tab[0])+1):
                x,y=npos  
                for p in rotations:
                    p=cropM(p)
                    newTab, stat = move(Tab, p,i,j, x, y)
                    if stat:
                        leftPiz = final.copy()
                        leftPiz.remove(actPiz)
                        result = call(newTab, leftPiz, nextpos(newTab))
                        if result:
                            return result
            Tab = [row[:] for row in ogTab]  

def inputs():
    m,n,cant=input().split()
    m=int(m)
    n=int(n)
    cant=int(cant)
    Zfinal = []
    for _ in range(cant):
        piz = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            line = input()
            for j in range(4):
                piz[i][j] = line[j]
        Zfinal.append(piz)
    piz = [["." for _ in range(n)] for _ in range(m)]
    result = call(piz, Zfinal,nextpos(piz))
    if result:
        for i in result:
            for j in i:
                print(j, end=" ")  
            print()  
    else:print(-1)

inputs()
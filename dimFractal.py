from numpy import zeros, arange, fix, polyfit
from math  import log

"""
Algoritmo de Higuchi
Input:  x       Una lista de valores
        kmax    Maximo valor de k   

Output: Dimension fractal que describe la lista x
"""
def hfd(x,kmax=5):

    N = len(x)

    lmk = zeros((kmax,kmax))

    for k in range(1,kmax+1):
        for m in range(1,k+1):

            lmki=0

            for i in range(1, int(fix((N-m)/k)) +1):
                lmki = lmki + abs(x[(m+i*k) -1] - x[(m+(i-1)*k) -1])
            
            Ng = (N-1)/(fix((N-m)/k)*k)
            lmk[m-1][k-1] = (lmki*Ng)/k

    Lk  = [ log( sum( [lmk[fila][k] for fila in range(kmax)])/(k+1)) for k in range(kmax)]
    Lnk = [ log(1/(i+1)) for i in range(kmax)]

    return polyfit(Lnk,Lk,1)[0]




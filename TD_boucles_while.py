#exercice 2
#1)
n = 0
while n < 10 :
    print(n)
    n = n + 2
#2)
n = 61
while n < 100 :
    print(n)
    n = n + 2
    
#exercice 3
#1)
def decroissant_for(n):
    for i in range(n,-1,-1):
        print(i, end=' ')
decroissant_for(6)
#2)
def decroissant_while(n):
    while n > -1 :
        print(n,end=' ')
        n = n - 1
decroissant_while(6)

#exercice 4
#3)
def somme1(n1,n2):
    S = 0
    for k in range(n1,n2):
        S = S + k
    return S
print(somme1(1,5))

def somme2(n1,n2):
    S = 0
    for k in range(n1+1,n2+1):
        S = S + k
    return S
print(somme2(1,5))

#exercice 5
#1)
def nombres_alenvers(n):
    alenvers = ''
    while n > 0:
        alenvers = alenvers + str(n%10)
        n = n // 10
    return int(alenvers)
print(nombres_alenvers(1234))

#2)
def palindrome(n):
    return n == nombres_alenvers(n)
print(palindrome(1234))
print(palindrome(121))

#exercice 6
#1)
L = 700
N = 0
while L < 800:
    L = L * 1.015
    N = N + 1
print(N-1)

#2)
L = 700
N = 0
somme = 0
while L < 800:
    L = L * 1.015
    N = N + 1
    somme = somme + L*12
print(N-1,L,somme-L*12)

#exercice 7
#2)
def est_premier(nb):
    if nb == 1 or nb == 0:
        return False
    div = 2
    while div < nb:
        if nb % div == 0:
            return False
        div = div + 1
    return True
print(est_premier(7))
print(est_premier(8))
print(est_premier(2))
print(est_premier(1))

#3)
def k_premiers(k):
    x = 0
    nb_premier = 0
    while nb_premier < k:
        if est_premier(x) == True:
            print(x, end= ' ')
            nb_premier = nb_premier + 1
        x = x + 1
    print()
k_premiers(3)
k_premiers(5)

#exercice 8
def est_present(c,s):
    i = 0
    while i < len(s):
        res = c == s[i]
        i = i + 1
        if res == True:
            return res
    return False
print(est_present('t','python'))
print(est_present('z',"je ne trouve pas"))
print(est_present('a',''))

#exercice 9
def syracuse(x):
    i = x
    vol = 0
    altitude = x
    while i > 1:
        print(i,end=' ')
        vol = vol + 1
        if i % 2 == 0:
            i = i // 2
        else:
            i = i * 3 + 1
        if altitude < i:
            altitude = i
    print()
    print('le temps de vol pour',x,'est de',vol,'et son altitude maximale est de',altitude)
syracuse(3)

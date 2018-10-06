def solve(n):
    somme=0
    for i in range(10001):
        #on parcourt les entiers de 0 à 10000
        j=0
        k=True
        while j<=50 and k:
            i=i+reverse(i)
            if palindrome(i):
                somme=somme+1
                k=False
            else:
                j=j+1
    return 10001-somme
    
def palindrome(nombre):
    b=str(nombre)
    n=len(b)
    c=n//2
    for i in range(c):
        if b[i]!=b[-(i+1)]:
            return False
    return True

def reverse(i):
    b=str(i)
    n=len(b)
    l=''
    for i in range(n):
        l=l+b[-(i+1)]
    return int(l)
    
assert solve(2)==249
print(solve(2))
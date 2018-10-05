def solve(n):
    somme=0
    nombre=n
    while int(nombre)!=0:
        intermediaire=(nombre//10)*10
        somme=somme+(nombre-intermediaire)
        nombre=nombre//10
    return somme

assert solve(2**15)==26


semilla = 7       
a = 5     
c = 3       
m = 3400000
iteraciones = 50

def congruencial_lineal(semilla, a, c, m, iteraciones):
    resultados = []                 
    x = semilla                   

    print(f"Semilla inicial: {x}\n")

    
    for i in range(iteraciones):
        x = (a * x + c) % m        # Formula
        resultados.append(x)


    return resultados



valores = congruencial_lineal(semilla, a, c, m, iteraciones)

print("\nSecuencia generada:")
print(valores)


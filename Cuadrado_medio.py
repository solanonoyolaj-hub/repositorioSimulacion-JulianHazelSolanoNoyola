

semilla = 5731        
n = 4                 
iteraciones = 3      

# Función del método
def cuadrado_medio(semilla, n, iteraciones):
    resultados = []                              
    x = int(str(semilla).zfill(n))               

    print(f"Semilla inicial: {x}\n")

    for i in range(iteraciones):                 
        x_cuadrado = x ** 2                     
        x_str = str(x_cuadrado).zfill(2 * n)    
        mitad = len(x_str) // 2                 
        start = mitad - (n // 2)                
        end = start + n                         
        x = int(x_str[start:end])               
        resultados.append(x)             

    return resultados


valores = cuadrado_medio(semilla, n, iteraciones)

print("\nSecuencia generada:")
print (valores)

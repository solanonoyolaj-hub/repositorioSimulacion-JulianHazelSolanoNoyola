

a = 5        
m = 30   
x = 7       
n = 20       

for i in range(n):
    x = (a * x) % m      
    r = x / m             
    print(f"R{i+1} = {r:.4f}")

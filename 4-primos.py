'''
2 - Números primos
    -- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e 
    retornar todos os números primos até o numero N. 
    
    EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];
   
'''

#  Criar uma função linear que resolva p

def pri(p, all=[]):

    for i in range(1, p+1):
        
        count = 0
        
        for j in range(1, p+1):
            
            if i % j == 0:
                count += 1
                
        if count == 2:
            all.append(i)
            
    return all


test = pri(10)  
print(test)


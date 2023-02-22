'''
2 - Números primos
    -- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e 
    retornar todos os números primos até o numero N. 
    
    EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];
   
'''

#  Criar uma função recursiva que resolva p

def pri(p, all=[], n=2, count=0):

    while True:

        try:

            if type(p) != int or p < 2:
                raise ValueError

            i = 1

            while i < p+1:
                
                if n % i == 0:
                    count += 1
                    
                i += 1
                
                if count > 2:
                    break
                
            if count == 2:
                all.append(n)

            if n != p:
                n += 1
                return pri(p, all, n)
            else:
                return all

        except ValueError:
            return 'Erro! Insira um valor numérico maior do que 1!'

test = pri(10)  
print(test)

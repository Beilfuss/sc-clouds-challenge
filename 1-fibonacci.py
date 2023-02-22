'''
1 - Fibonnaci
    -- Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a 
    função), e retornar o valor correspondente desse número na sequencia fibonnaci. 
    
    EX. fib(0) = 0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
'''

# Criar uma função recursiva que resolva fibonacci

def fib(pos, count=0, p=None, n=None):

    while True:
        
        try:
            
            if pos < 0:
                raise ValueError
            
            if count == 0:
                
                if pos == 0:
                    return 0
                
                p = 0   # prior
                n = 1   # next
                count = 1
            
            else:
                
                t = n
                n = p + n
                p = t
                
                count += 1
                
            if pos != count:
                return fib(pos, count, p, n)
            else:
                return n
            
        except ValueError:
            pos = int(input('Insira um valor maior ou igual a 0: '))

test = fib(12)
print(test)

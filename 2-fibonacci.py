'''
1 - Fibonnaci
    -- Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a 
    função), e retornar o valor correspondente desse número na sequencia fibonnaci. 
    
    EX. fib(0) = 0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
'''

# Criar uma função linear que resolva fibonacci

def fib(pos):

    if pos == 0:
        return 0

    p = 0
    n = 1

    for i in range(pos-1):

        t = n
        n = p + n
        p = t

    return n

test = fib(0)
print(test)

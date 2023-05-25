import numpy as np

# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Enter the number of coins: '))
coins = np.random.randint(0,2,n)
print(n,'->',*coins) 
countTails = np.count_nonzero (coins == 0 )
countEagles = np.count_nonzero (coins == 1 )
if countTails < countEagles:
    print(countTails)    
else:
    print(countEagles)  

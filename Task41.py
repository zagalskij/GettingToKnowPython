def fillArray(numberArray):
    array = [input() for _ in range(numberArray)]
    return array


def comparsion(array):
    return [array[i] for i in range(1,n-1) 
            if array[i-1] < array[i] > array[i+1]]



n = int(input("Enter the number elements шт the array: "))
array = fillArray(n)
print(len(comparsion(array)))

def FillArray(numberArray, array):
    if numberArray == 0:
        return array
    array.append(int(input()))
    return (FillArray(numberArray-1, array))   

def UniqArray(array1, array2, array3 = [], j = 0):
    print(len(array2))
    j == len(array2)
    for i in range(len(array1)):
        j= 0
        while (array1[i] != array2[j]) or (j != len(array2)-1):
            print(bool(array1[i] != array2[j]) or (j != len(array2)-1))
            j = j+1
            if j == len(array2):
                array3.append(array1[i])
    return array3

array1 = []
array2 = []
numberArray1 = int(input("Enter the number of elements first array:"))
array1 = FillArray(numberArray1, array1)
numberArray2 = int(input("Enter the number of elements second array:"))
array2 = FillArray(numberArray2, array2)
print(UniqArray(array1, array2))
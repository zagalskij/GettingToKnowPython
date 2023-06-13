# def fillArray2(numberArray, array, i = 0):
#     if numberArray == 0:
#         return array
#     array.append(int(input()))
#     return (fillArray(numberArray-1, array, i+1))   


def fillArray(numberArray):
    array = [input() for _ in range(numberArray)]
    return array
    

# def uniqArray(array1, array2, array3 = []):
#     for i in range(len(array1)):
#         j= 0
#         while j != len(array2):
#             if array1[i] == array2[j]:
#                 break
#             if j == len(array2)-1:
#                 array3.append(array1[i])
#             j = j+1
#     return array3





array1 = []
array2 = []
numberArray1 = int(input("Enter the number of elements first array: "))
array1 = fillArray(numberArray1)
numberArray2 = int(input("Enter the number of elements second array: "))
array2 = fillArray(numberArray2)
print(*[num for num in array1 if num not in array2])
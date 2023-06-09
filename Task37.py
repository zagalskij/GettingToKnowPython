def FillStr(n):
    if (n == 0):
        return " "
    number = int(input())
    return str(number)+FillStr(n-1)


def ReverseStr(strNumber, i = 0):
    if i == len(strNumber):
        return ""
    return ReverseStr(strNumber, i+1) + strNumber[i] 


n = int(input('Enter the number: '))
strNumber = FillStr(n)
print(f'Input: {n} -> {strNumber}')
print(f'Output: {n} ->{ReverseStr(strNumber)}')

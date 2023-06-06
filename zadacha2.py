def Calculate(theFirstNumber, theSecondNumber):
    return (theFirstNumber+theSecondNumber, theFirstNumber-theSecondNumber,
            theFirstNumber*theSecondNumber, theFirstNumber/theSecondNumber)


theFirstNumber = int(input('Enter the first number: '))
theSecondNumber =int(input('Enter the second number: '))
operation = Calculate(theFirstNumber, theSecondNumber)
print(f'the amount: {operation[0]}')
print(f'difference: {operation[1]}')
print(f'composition: {operation[2]}')
print(f'private: {operation[3]}')
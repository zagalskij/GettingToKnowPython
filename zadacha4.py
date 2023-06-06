theNumberOfBeatiful = int(input('Enter the number of beatiful: '))
beatiful = {input() for _ in range(theNumberOfBeatiful)}
theNumberOfSmart = int(input('Enter the number of beatiful: '))
smart = {input() for _ in range(theNumberOfSmart)}
theNumberOfStrong = int(input('Enter the number of beatiful: '))
strong = {input() for _ in range(theNumberOfBeatiful)}
print(len(beatiful.intersection(smart,strong)))
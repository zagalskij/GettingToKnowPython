list = input().split() 
print(sum(list.count(x) - 1 for x in list) // 2)




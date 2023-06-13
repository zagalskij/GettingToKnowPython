def same_by(characteristic, objects):
    if len(objects) == 0:
        return True
    first = characteristic(objects[0])
    for i in range(1, len(objects)):
        if bool(first != characteristic(objects[i])):
           return False 
    return True


values = [2, 4, 3] 
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
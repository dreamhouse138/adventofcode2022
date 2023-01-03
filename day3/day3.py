def getItemPriorities(file):
    prio = 0
    with open(file, 'r') as f:
        for line in f:
            first, second = set(line[:len(line)//2]), set(line[len(line)//2:])
            same = first.intersection(second).pop()
            if same.lower() == same:
                prio += (ord(same) - ord('a') + 1)
            else:
                prio += (ord(same) - ord('A') + 27)
    
    return prio

print(getItemPriorities('day3_input.txt'))



def getThrees(file):
    prio = 0
    with open(file, 'r') as f:
        package = []
        for line in f:
            if len(package) == 3:
                first, second, third = set(package[0]), set(package[1]), set(package[2]) 
                same = (first & second & third).pop()
                            
                if same.lower() == same:
                    prio += (ord(same) - ord('a') + 1)
                else:
                    prio += (ord(same) - ord('A') + 27)
                package = [line.strip()]
            else:
                package.append(line.strip())
        
        first, second, third = set(package[0]), set(package[1]), set(package[2]) 
        same = (first & second & third).pop()    
        if same.lower() == same:
            prio += (ord(same) - ord('a') + 1)
        else:
            prio += (ord(same) - ord('A') + 27)
    
    return prio

print(getThrees('day3_input.txt'))

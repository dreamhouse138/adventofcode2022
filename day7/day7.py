
def getTotalFileSize(file):
    tree = {}
    total = 0
    with open(file, 'r') as f:
        prevDir = []
        currDir = ''
        path = ''
        for line in f:
            if line[0] == '$':
                if line[2:4] == 'cd' and line[5:7] != '..':
                    prevDir.append(currDir)
                    currDir = line[5:].strip()
                    path += currDir
                    tree[path] = 0
                
                elif line[2:4] == 'cd' and line[5:7] == '..': 
                    path = path[0: len(path) - len(currDir)]
                    currDir = prevDir.pop()
                
                elif line[2:4] == 'ls':
                    pass
            else:
                if line[0:3] == 'dir':
                    continue
                else:
                    size = int(line[0: line.find(' ') + 1])
                    tree[path] += size
                    stackPath = ''
                    for d in prevDir[1:]:
                        stackPath += d
                        tree[stackPath] += size

        for d in tree:
            if tree[d] <= 100000:
                total += tree[d]
        
        return total

print(getTotalFileSize('day7_input.txt'))



def chooseDeletedDir(file):
    tree = {}
    with open(file, 'r') as f:
        prevDir = []
        currDir = ''
        path = ''
        for line in f:
            if line[0] == '$':
                if line[2:4] == 'cd' and line[5:7] != '..':
                    prevDir.append(currDir)
                    currDir = line[5:].strip()
                    path += currDir
                    tree[path] = 0
                
                elif line[2:4] == 'cd' and line[5:7] == '..': 
                    path = path[0: len(path) - len(currDir)]
                    currDir = prevDir.pop()
                
                elif line[2:4] == 'ls':
                    pass
            else:
                if line[0:3] == 'dir':
                    continue
                else:
                    size = int(line[0: line.find(' ') + 1])
                    tree[path] += size
                    stackPath = ''
                    for d in prevDir[1:]:
                        stackPath += d
                        tree[stackPath] += size

        
        requiredSpace = 30000000 - (70000000 - tree['/'])
        minReq = float('inf')
        for d in tree:
            if tree[d] >= requiredSpace:
                minReq = min(minReq, tree[d])
        
        return minReq

print(chooseDeletedDir('day7_input.txt'))
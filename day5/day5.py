def findTopOfStack(file):
    table = {}
    tops = ''
    with open(file, 'r') as f:
        stack, instructions = [
            part.split('\n') for part in f.read().split('\n\n')
        ]

        stacks = len(stack[-1].strip().replace(' ', ''))
        for i in range(stacks):
            table[i + 1] = []
        
        for item in range(len(stack) - 1):
            for i, thing in enumerate(stack[item][1::4]):
                if thing != ' ':
                    table[i + 1].append(thing)

        for instruct in instructions:
            arr = instruct.split()
            numMove = int(arr[1])
            stackNo = int(arr[3])
            stackTo = int(arr[5])
            
            for i in range(numMove):
                moved = table[stackNo].pop(0)
                table[stackTo].insert(0, moved)
        
        for s in table:
            tops += table[s][0]
    
    return tops

print(findTopOfStack('day5_input.txt'))


def findTopOfStackMulti(file):
    table = {}
    tops = ''
    with open(file, 'r') as f:
        stack, instructions = [
            part.split('\n') for part in f.read().split('\n\n')
        ]

        stacks = len(stack[-1].strip().replace(' ', ''))
        for i in range(stacks):
            table[i + 1] = []
        
        for item in range(len(stack) - 1):
            for i, thing in enumerate(stack[item][1::4]):
                if thing != ' ':
                    table[i + 1].append(thing)
        

        for instruct in instructions:
            arr = instruct.split()
            numMove = int(arr[1])
            stackNo = int(arr[3])
            stackTo = int(arr[5])

            moved = table[stackNo][0:numMove]
            table[stackNo] = table[stackNo][numMove:]
            
            for i in range(len(moved) - 1, -1, -1):
                table[stackTo].insert(0, moved[i])

        for s in table:
            tops += table[s][0]

    return tops


print(findTopOfStackMulti('day5_input.txt'))
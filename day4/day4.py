def inRange(file):
    result = 0
    with open(file, 'r') as f:
        for line in f:
            l = line.strip().split(',')
            first, second = l[0], l[1]
            fsplit = first.split('-')
            ssplit = second.split('-')
            fset = set(range(int(fsplit[0]), int(fsplit[1]) + 1))
            sset = set(range(int(ssplit[0]), int(ssplit[1]) + 1))
            if fset.issubset(sset) or sset.issubset(fset):
                result += 1

    return result

print(inRange('day4_input.txt'))

def overlap(file):
    result = 0
    with open(file, 'r') as f:
        for line in f:
            l = line.strip().split(',')
            first, second = l[0], l[1]
            fsplit = first.split('-')
            ssplit = second.split('-')
            fset = set(range(int(fsplit[0]), int(fsplit[1]) + 1))
            sset = set(range(int(ssplit[0]), int(ssplit[1]) + 1))
            if len(fset & sset) > 0:
                result += 1

    return result

print(overlap('day4_input.txt'))



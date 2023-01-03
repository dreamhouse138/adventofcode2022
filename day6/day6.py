def firstFourWindow(file):
    processed = 0
    seen = set()
    with open(file, 'r') as f:
        seq = f.read()
        n = len(seq)
        i, j = 0, 0
        while j - i != 4:
            if seq[j] not in seen:
                seen.add(seq[j])
                j += 1
            else:
                seen = set()
                i += 1
                j = i
    return j

print(firstFourWindow('day6_input.txt'))


def firstMessage(file):
    processed = 0
    seen = set()
    with open(file, 'r') as f:
        seq = f.read()
        n = len(seq)
        i, j = 0, 0
        while j - i != 14:
            if seq[j] not in seen:
                seen.add(seq[j])
                j += 1
            else:
                seen = set()
                i += 1
                j = i
    return j

print(firstMessage('day6_input.txt'))

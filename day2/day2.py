# A, X - Rock
# B, Y - Paper
# C, Z - Scissor


def getScore(file):
    choices = {'X':1, 'Y':2, 'Z':3}
    score = 0
    with open(file, 'r') as f:
        for line in f:
            l = line.strip().split(' ')
            opponent, you = l[0], l[1]
            score += choices[you]
            if (opponent == 'A' and you == 'X') or (opponent == 'B' and you == 'Y') or (opponent == 'C' and you == 'Z'):
                score += 3
            elif (opponent == 'A' and you == 'Y') or (opponent == 'B'and you == 'Z') or (opponent == 'C' and you == 'X'):
                score += 6
    
    return score

print(getScore('day2_input.txt'))


def getFixedScore(file):
    choices = {'A':1, 'B':2, 'C':3}
    score = 0
    with open(file, 'r') as f:
        for line in f:
            l = line.strip().split(' ')
            opponent, choice = l[0], l[1]
            if choice == 'X':
                if opponent == 'A':
                    score += 3
                elif opponent == 'B':
                    score += 1
                else:
                    score += 2
            elif choice == 'Z':
                score += 6
                if opponent == 'A':
                    score += 2
                elif opponent == 'B':
                    score += 3
                else:
                    score += 1
            else:
                score += (choices[opponent] + 3)
    
    return score

print(getFixedScore('day2_input.txt'))
                
def getLargestSnack(file):
    largest = 0
    with open(file, 'r') as f:
        size = 0
        for i in f:
            if i.strip() == '':
                largest = max(largest, size)
                size = 0
            else:
                size += int(i)
    return largest


print(getLargestSnack('day1_input.txt'))



def largestthree(file):
    three = [0, 0, 0]

    with open(file, 'r') as f:
        size = 0
        for i in f:
            if i.strip() == '':
                if size > three[2]:
                    temp1, temp2 = three[1], three[2]
                    three[2] = size
                    three[1] = temp2
                    three[0] = temp1
                elif size > three[1]:
                    temp = three[1]
                    three[1] = size
                    three[0] = temp
                elif size > three[0]:
                    three[0] = size
                size = 0
            else:
                size += int(i)


    return sum(three)

print(largestthree('day1_input.txt'))
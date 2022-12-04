results_scores = {'WIN': 6,'DRAW': 3,'LOSE': 0}

with open('input.txt') as fp:
    Lines = fp.readlines()

priority_sum = 0
for line in Lines:
    line = line.strip()
    half_1, half_2 = line[:len(line)//2], line[len(line)//2:]
    print('-------')
    print("half 1: {} half 2: {}".format(half_1,half_2))

    value = 0
    for ch in half_1:
        if ch in half_2:
            value = ord(ch) - 38 if ch.isupper() else ord(ch) - 96
            print("found {} has value {}".format(ch, value))
            priority_sum += value
            print('-------')
            break
            


print("priority sum would be {}".format(priority_sum))

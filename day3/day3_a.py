with open('input.txt') as fp:
    Lines = fp.readlines()

priority_sum = 0
for line in Lines:
    half_1, half_2 = set(line[:len(line)//2].strip()), set(line[len(line)//2:].strip())

    intersect = half_1.intersection(half_2)
    if len(intersect) == 1:
        ch = intersect.pop()
        value = ord(ch) - 38 if ch.isupper() else ord(ch) - 96
        print("found {} has value {}".format(ch, value))
        priority_sum += value
            
print("priority sum would be {}".format(priority_sum))

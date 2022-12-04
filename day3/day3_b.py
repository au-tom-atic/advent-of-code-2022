with open('input.txt') as fp:
    Lines = fp.readlines()

priority_sum = 0
for line1, line2, line3 in zip(*[iter(Lines)]*3):
    line1, line2, line3 = set(line1.strip()), set(line2.strip()), set(line3.strip())

    intersect = line1.intersection(line2, line3)

    if len(intersect) == 1:
        ch = intersect.pop()
        value = ord(ch) - 38 if ch.isupper() else ord(ch) - 96
        print("found {} has value {}".format(ch, value))
        priority_sum += value
    else:
        print("something went wrong...more than 1 common element found!")
                
print("priority sum would be {}".format(priority_sum))
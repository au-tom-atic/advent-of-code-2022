with open('input.txt') as fp:
    Lines = fp.readlines()

fully_contains_count = 0
for line in Lines:
    first_pair, second_pair = line.strip().split(',')[0].split('-'), line.strip().split(',')[1].split('-')
    first_range= set([*range(int(first_pair[0]), int(first_pair[1]) + 1)])
    second_range = set([*range(int(second_pair[0]), int(second_pair[1]) + 1)])
    
    if first_range.issubset(second_range) or second_range.issubset(first_range):
        fully_contains_count +=1



print("priority sum would be {}".format(fully_contains_count))

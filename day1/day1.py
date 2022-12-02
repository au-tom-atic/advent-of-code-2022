import sys

elf_calories_arr = []

with open('input.txt') as fp:
    Lines = fp.readlines()

elf_calories = 0
elf_count = 0
for line in Lines:
    if line.strip():
        elf_calories += int(line)
    else:
        #print("elf #{} has {} calories".format(elf_count, elf_calories))
        elf_calories_arr.append(elf_calories)
        elf_calories = 0
        elf_count += 1

elf_calories_arr.sort(reverse=True)
calories_sum = sum(elf_calories_arr[:3])
print("sum of the highest calories is {}".format(calories_sum))

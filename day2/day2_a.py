from enum import Enum

scores_dict = {'ROCK': 1, 'PAPER': 2,'SCISSORS': 3}
elf_encrypt_dict = {'A': 'ROCK', 'B': 'PAPER','C': 'SCISSORS'}
my_encrypt_dict = {'X': 'ROCK', 'Y': 'PAPER','Z': 'SCISSORS'}
WIN = 6
DRAW = 3

with open('input.txt') as fp:
    Lines = fp.readlines()

score = 0
for line in Lines:
    scores = line.split(' ')
    en_elf_play = scores[0].strip()
    en_my_play = scores[1].strip()
    de_elf_play = elf_encrypt_dict[en_elf_play]
    de_my_play = my_encrypt_dict[en_my_play]

    #print("{} vs {}".format(de_elf_play, de_my_play))

    #always score for playing
    score += scores_dict[de_my_play]

    #no score
    if de_elf_play == de_my_play:
        score += DRAW
        continue
    
    ## WINNING PLAYS
    if de_elf_play == 'ROCK' and de_my_play == 'PAPER':
        score += WIN
        continue

    if de_elf_play == 'PAPER' and de_my_play == 'SCISSORS':
        score += WIN
        continue

    if de_elf_play == 'SCISSORS' and de_my_play == 'ROCK':
        score += WIN
        continue

    #LOSING PLAYS no points

print("your score would be {}".format(score))

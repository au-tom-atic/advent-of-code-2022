from enum import Enum

scores_dict = {'ROCK': 1, 'PAPER': 2,'SCISSORS': 3}
elf_encrypt_dict = {'A': 'ROCK', 'B': 'PAPER','C': 'SCISSORS'}
my_encrypt_dict = {'X': 'LOSE', 'Y': 'DRAW','Z': 'WIN'}

desired_outcome_combos = {
    'ROCK': {'WIN': 'PAPER', 'LOSE': 'SCISSORS', 'DRAW': 'ROCK'},
    'PAPER': {'WIN': 'SCISSORS', 'LOSE': 'ROCK', 'DRAW': 'PAPER'},
    'SCISSORS': {'WIN' : 'ROCK', 'LOSE': 'PAPER', 'DRAW': 'SCISSORS'}
    }

results_scores = {'WIN': 6,'DRAW': 3,'LOSE': 0}

with open('input.txt') as fp:
    Lines = fp.readlines()

score = 0
for line in Lines:
    scores = line.split(' ')
    en_elf_play = scores[0].strip()
    en_outcome = scores[1].strip()
    de_elf_play = elf_encrypt_dict[en_elf_play]
    de_outcome = my_encrypt_dict[en_outcome]

    my_hand = desired_outcome_combos[de_elf_play][de_outcome]
    score += scores_dict[my_hand]
    score += results_scores[de_outcome]
    print("I need to {} against {}, so I will use {}".format(de_outcome, de_elf_play, my_hand))

print("your score would be {}".format(score))

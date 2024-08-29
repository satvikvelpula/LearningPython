import random

prompt = int(input("How many dice to roll?: "))

total_sum = 0

for i in range(prompt):
    roll = random.randint(1, 6)
    total_sum += roll

print(total_sum)
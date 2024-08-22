from random import randint

threelist = ""

for i in range (3):
    threelist += str((randint(0, 9)))

fourlist = ""

for i in range(4):
    fourlist += str((randint(0, 6)))

print(f'Three numbered code: {threelist}')
print(f'Four numbered code: {fourlist}')
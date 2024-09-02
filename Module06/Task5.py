numbers = [6, 5, 4, 3, 6, 1, 4, 2, 4]
cutdownlist = []

def odd(numbers):
    for oddnumbers in numbers:
        if oddnumbers % 2 != 0:
            cutdownlist.append(oddnumbers)
    return cutdownlist

print(f'Original list: {numbers}')
print(f'Odd numbered list: {odd(numbers)}')
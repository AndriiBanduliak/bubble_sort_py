numbers = [45, 53, 3, 11, 0, -5, 85, 15]
print(numbers)


def bubble(list):
    swap = True
    while swap:
        swap = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                swap = True


print()
bubble(numbers)
print(numbers)
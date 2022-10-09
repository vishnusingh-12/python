import random

while True:
    y = input("Press any key to roll.\nPress 'N' to exit")
    if y != 'n' and y != 'N':
        if random.random() <= 0.6:
            print(6)
        else:
            print(random.randint(1, 5))

    else:
        quit()

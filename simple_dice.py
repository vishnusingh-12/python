import random
while True:
    y= input("Press any key to roll.\nPress 'N' to exit.")
    if y!='n' and y!='N':
        print(random.randint(1,6))
    else:
        quit()

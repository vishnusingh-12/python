import random

signList = ["r", "p", "s"]
cpuCount = 0
userCount = 0
drawCount = 0
choice = input("Welcome to Rock Paper Scissor!\nDo you want to play? (Y/N) ")
if choice == 'y' or choice == "Y":
    while True:
        num_of_rounds = int(input("How many rounds you want to play"))
        for i in range(num_of_rounds):
            cpuSign = (random.choice(signList)).capitalize()
            userSign = input("Enter your Sign").capitalize()
            print(cpuSign)
            if userSign == "R" and cpuSign == "S":
                userCount += 1
                print("You Won This Round !")
            elif userSign == "R" and cpuSign == "P":
                cpuCount += 1
                print("Cpu Won This Round !")
            elif userSign == "P" and cpuSign == "R":
                userCount += 1
                print("You Won This Round !")
            elif userSign == "P" and cpuSign == "S":
                cpuCount += 1
                print("Cpu Won This Round !")
            elif userSign == "S" and cpuSign == "R":
                cpuCount += 1
                print("Cpu Won This Round !")
            elif userSign == "S" and cpuSign == "P":
                userCount += 1
                print("You Won This Round !")
            elif userSign == cpuSign:
                print("This round was a draw")
                drawCount += 1
            else:
                print("Wrong Sign")
                print("Cpu Won This Round !")
                cpuCount += 1
        print("Wins:", userCount)
        print("Loses:", cpuCount)
        print("Draws", drawCount)
        if userCount > cpuCount:
            print("Victory")
        elif userCount == cpuCount:
            print("Draw")
        else:
            print("You lost")
        play_again = input("Do you wanna play again? (Y/N) ")
        if play_again != "y" and play_again != "Y":
            print("See you later")
            quit()
        else:
            pass

else:
    print("See you later")
    quit()

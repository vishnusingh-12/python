import random

print("Welcome to Guess The Number")
while True:
    y = input("Press 'Y' to play and press any key to exit. ")
    if y != 'y' and y != "Y":
        quit()
    else:
        number = random.randint(1, 100)
        num_of_guesses = int(input("Enter Number of Guesses You think You Will Take yo Guess the Number."))
        for j in range(1, num_of_guesses + 1):
            i = int(input("Enter your guess between 1 to 100\n"))
            if i > number:
                if num_of_guesses - j == 0:
                    print("Game Over")
                    print("The number was", number)
                    break
                print("Your guess is greater than the number,try again\n")
            elif i < number:
                if num_of_guesses - j == 0:
                    print("Game Over")
                    print("The number was", number)
                    break
                print("Your guess is smaller than the number,try again\n")
            else:
                print("Hurray , right guess")
                print("You won")
                print("No. of guesses taken are", j)
                break

            print("Number of guesses left", num_of_guesses - j)

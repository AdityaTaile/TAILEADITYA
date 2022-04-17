
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

try:
    chosenInt = int(input('Enter an integer greater than 1: '))

    while chosenInt < 2:
        print("Sorry, your number must be greater than 1.")
        chosenInt = int(input('Enter an integer greater than 1: '))

    print(chosenInt)

    while chosenInt != 1:
        chosenInt = collatz(chosenInt)
        print(chosenInt)

except ValueError:
    print('Sorry, you must enter an integer.')
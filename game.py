from random import randint




def main():
    random = randint(1, 10)
    print("\t\tWelcome to guessing game")
    a = 3
    for i in range(3):
        x = int(input("guess the number btw 1 to 10:"))
        if x == random:
            print("\ngreat u have guess the right no\n\nCongratualtions you won the game!!!!!")
            break
        elif x < random:
            print("\nlower than guess value")
        elif x > random:
            print("greater than guess value")    
        a = a - 1
        print("wrong... try again", a, 'chance left')

    else:
        print("sry...!! no chance left")


main()

s = input("\nwant to play again for yes press y or no for n:")
if s == 'y' or s=='Y':
    main()
else:
    print("thanks for giving u r tym!!!")
    exit()

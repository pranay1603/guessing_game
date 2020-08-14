from random import randint


random = randint(1, 10)

def main():
    a = 3
    for i in range(3):
        x = int(input("enter the no u want to guess btw 1 to 10:"))
        if x == random:
            print("\ngreat u have guess the right no\n\nCongratualtions you won the game!!!!!")
            break
        else:
            a = a - 1
            print("wrong... try again", a, 'left')

    else:
        print("sry...!! no chance left")


main()

s = input("\nwant to play again for yes press y or no for n:")
if s == 'y':
    main()
else:
    print("thanks for giving u r tym!!!")
    exit()

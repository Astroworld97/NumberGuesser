#Source: https://www.youtube.com/watch?v=EBezqslQslc
from random import randrange
def guess():
    n = randrange(1000)
    while True:
        v = int(input("Please enter your guess for the correct number: "))
        if n == v: #if it is the correct number
            print("You win!")
            break
        print("Smaller" if (n < v) else "Bigger")

if __name__ == '__main__':
    guess()
#Source: https://www.youtube.com/watch?v=EBezqslQslc

from random import randrange
n = randrange(1000)
while True:
    v = int(input())
    if n == v: #if it is the correct number
        print("You win!")
        break
    print("Smaller" if (n < v) else "Bigger")

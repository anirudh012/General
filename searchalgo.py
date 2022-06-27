import time, os

os.system('clear')
def newfunc(total,guess):

    divider = 2
    g = round(total/divider)
    guess_no = 0

    while True:
        print(g)
        time.sleep(0.001)
        os.system('clear')
        guess_no += 1
        divider = divider * 2
        if g == guess:
            print(f"Found in {guess_no} steps")
            break
        elif g > guess:
            g = g - round(total/divider)
        elif g < guess:
            g = g + round(total/divider)
        time.sleep(0)

newfunc(int(input("Total: ")),int(input("Guess: ")))
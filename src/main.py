import random

rounds_left = 6

print("Russian Roulette")
input("Load a round [ENTER]")
print("Spinning chamber...")
while True:
    input("Pull the trigger [ENTER]")
    if random.randint(1, rounds_left) == 1:
        print("BANG")
        print("YOU DED")
        break
    else:
        rounds_left -= 1
        print("Safe! 1/" + str(rounds_left) + " chance for next player to die")
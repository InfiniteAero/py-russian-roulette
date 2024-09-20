import random
import time
from rich.console import Console

console = Console()
rounds_left = 6

console.clear()

console.print("Russian Roulette")
input("Press [ENTER] to begin")
console.clear()
input("Load a round [ENTER]")
console.print("Spinning chamber...")
time.sleep(1)
while True:
    input("Pull the trigger [ENTER]")
    if random.randint(1, rounds_left) == 1:
        with console.status("...silence...", spinner='line'):
            time.sleep(1)
            console.print("BANG")
            console.print("[bold red]YOU DED[/]")
            break
    else:
        with console.status("...silence...", spinner='line'):
            rounds_left -= 1
            time.sleep(1)
            console.print("click!")
            time.sleep(0.5)
            console.clear()
            console.print("Safe! 1/" + str(rounds_left) + " chance for next player to die")
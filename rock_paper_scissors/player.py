import random
from move import Move


class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.move = None

    def choose_move(self):
        if self.is_computer:
            choice = random.choice(Move.valid_moves)

        else:
            while True:
                choice = input(
                    f"{self.name}, choose rock, paper, or scissors: "
                ).lower()
                if choice in Move.valid_moves:
                    break
                print("Invalid choice. Try again.")

        self.move = Move(choice)

    def __str__(self):
        return f"{self.name} chose {self.move}"

from player import Player


class Game:
    def __init__(self):
        print("Welcome to Rock, Paper, Scissors!")
        name = input("Enter your name: ")
        self.human = Player(name)
        self.computer = Player("Computer", is_computer=True)

    def play_round(self):
        self.human.choose_move()
        self.computer.choose_move()

        print(self.human)
        print(self.computer)

        if self.human.move.beats(self.computer.move):
            print(f"{self.human.name} wins!")
        elif self.computer.move.beats(self.human.move):
            print("Computer wins!")
        else:
            print("It's a tie!")

    def play(self):
        while True:
            self.play_round()
            again = input("Play again? (y/n): ").lower()
            if again != "y":
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    game = Game()
    game.play()

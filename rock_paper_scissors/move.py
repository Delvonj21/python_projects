class Move:
    valid_moves = ["rock", "paper", "scissors"]

    def __init__(self, move):
        if move not in self.valid_moves:
            raise ValueError(f"{move} is not a valid move.")
        self.move = move

    def beats(self, other_move):
        return (
            ((self.move == "rock" and other_move.move == "scissors"))
            or (self.move == "paper" and other_move.move == "rock")
            or (self.move == "scissors" and other_move == "paper")
        )

    def __str__(self):
        return self.move

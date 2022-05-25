import random

moves = ['rock', 'paper', 'scissors']


class Player:
    @staticmethod
    def move():
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        human_choice = ''
        while human_choice not in moves:
            human_choice = input("Please enter a choice (rock, paper, "
                                 "scissors or quit:\n").lower()
            if human_choice == 'quit':
                exit()

        return human_choice


class Reflectplayer(Player):
    def __init__(self):
        self.last_move = ''

    def move(self):
        if self.last_move == '':
            return random.choice(moves)
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.moveIndex = random.randint(0, 2)

    def move(self):
        self.moveIndex = (self.moveIndex + 1) % 3
        return moves[self.moveIndex]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2, ):
        self.p1 = p1
        self.p2 = p2
        self.p1Score = 0
        self.p2Score = 0

    def play_round(self, retry_count=0):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: You Played {move1}  Player 2: Opponent Played "
              f" {move2}\n")

        if beats(move1, move2):
            self.p1Score += 1
            print("Player 1. Wins!")
            print(f"P1 Score: {self.p1Score}  P2 Score: {self.p2Score}\n")

        elif beats(move2, move1):
            self.p2Score += 1
            print("Player 2. Wins!")
            print(f"P1 Score: {self.p1Score}  P2 Score: {self.p2Score}\n")

        else:
            print("It's a tie!")
            if retry_count <= 3:
                self.play_round(retry_count + 1)

    def play_game(self):
        print("Game start!\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

        if self.p1Score > self.p2Score:
            print("Player 1 wins!\n")
            print(f"Final Score: P1 Score: {self.p1Score}  P2 Score:"
                  f" {self.p2Score}\n")
        elif self.p2Score > self.p1Score:
            print("Player 2 wins!\n")
            print(f"Final Score: P2 Score: {self.p2Score}  P1 Score:"
                  f" {self.p1Score}\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

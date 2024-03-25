# This code sample defines a class that represent a player
# This class was designed as a leaderboard's record
class Player:
    def __init__(self, name, wins, losses, draws):
        self.player = name
        self.wins = wins
        self.losses = losses
        self.draws = draws

    player: str
    wins: int
    loses: int
    draws: int

    def __str__(self):
        return ("Player: " + self.player + "\n"
                + "Wins: " + str(self.wins) + "\n"
                + "Loss: " + str(self.losses) + "\n"
                + "Draws: " + str(self.draws))


player_one = Player(
    name="Vlad",
    wins=10,
    losses=10,
    draws=20)

print(player_one)

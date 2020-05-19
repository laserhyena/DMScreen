class Player:
    def __init__(self, playerName):
        self.player_name = playerName
        self.player_class = self.get_player_class()
        self.player_race = self.get_player_race()

    def get_player_class(self):
        self.player_class = input("What is your player's class?")
        return self.player_class

    def get_player_race(self):
        self.player_race = input("What is your player's race?")
        return self.player_race

from player import Player

playerLst = []

userSelect = int(input("Press 1 to add a new Player Character, 2 to delete a Player Character, 3 to show a list of "
                       "the Player Characters, or 4 to quit:"))

while userSelect != 4:
    if userSelect == 1:
        anotherPlayer = True

        while anotherPlayer:
            playerName = input("What is the name of the Player Character you would like to add?")

            playerLst.append(Player(playerName))

            userCont = input("Would you like to add another player? Y/N")
            userCont = userCont.upper()

            while userCont != "Y" and userCont != "N":
                print("Invalid Entry!")
                userCont = input("Would you like to add another player? Y/N")
                userCont = userCont.upper()

            if userCont == "N":
                anotherPlayer = False
            elif userCont == "Y":
                anotherPlayer = True
    elif userSelect == 2:
        playerToDrop = int(input("Please add the number of the player you would like to drop, from the list of "
                                 "players: "))
        playerToDrop -= 1
        playerLst.remove(playerLst[playerToDrop])
    elif userSelect == 3:
        playerCnt = 1
        for player in playerLst:
            print("Player ", playerCnt, ":")
            print(player.display_player_info())
            print()
            playerCnt += 1
    else:
        print("Invalid entry!")

    userSelect = int(input("Press 1 to add a new Player Character, 2 to delete a Player Character, 3 to show a list "
                           "of the Player Characters, or 4 to quit:"))

playerLst = []
anotherPlayer = True

while anotherPlayer:
    playerName = input("What is the name of the Player Character you would like to add?")

    playerLst.append(playerName)

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


print(playerLst)

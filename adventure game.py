print("*************** WELCOME TO WORD GAME********************")
answer = input("Do you want to play this adventure Game? [yes/no]")
if answer == "yes":
    print("That`s grate")
    print()

    answer = input("Do you want to explore a cave or jungal? [cave/jungal] ")


    if answer =="cave":
        print("you go into the cave and see a sleeping bear")
        print()
        answer = input("Do you want to fight ro run? [fight/run]")
        if answer == "fight":
            print("bear are really strong! You lose!")
        elif answer == "run":
            print ("you ran away ! You win!")
        else:
            print("Invalid option ,you lose!")


    elif answer =="jungal":
        print("you meet tiger and you get eaten!you lose!")
    else:
        print("invalid option,you lose!")

else : print("but this is a really awsome game")




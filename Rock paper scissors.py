try:
    def game():
        import random

        case = input("Do you want to play? Enter yes or no: ")
        while (case.upper()=="TRUE" or case.upper()=="YES"):
            choose = ["rock","paper","scissors"]
            computer = random.choice(choose)
    
            user = input("Enter among - rock, paper and scissors ")
            print("Computer's choice is: "+computer)
            print("User's choice is: "+user)
    
            if(user==computer):
                print("Draw")
            elif(user=="rock" and computer=="scissors"):
                print("You won")
            elif(user=="rock" and computer=="paper"):
                print("Computer won")
            elif(user=="paper" and computer=="rock"):
                print("You won")
            elif(user=="paper" and computer=="scissors"):
                print("Computer won")
            elif(user=="scissors" and computer=="rock"):
                print("Computer won")
            elif(user=="scissors" and computer=="paper"):
                print("You won")
            else:
                print("Enter correctly")
        
            case = input("Do you want to play again? Enter yes or no:  ")
        print("Thank you")
    
    game()
except:
    print("Enter correctly")
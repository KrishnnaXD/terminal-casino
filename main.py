import random
import time
import uuid
from colorama import Fore, Style, init

init(autoreset=True)
print(Fore.RED + "Welcome, Welcome, Welcome to The Terminal Casino!\nHere you get your pocket money and try to either get rich or lose it all, all depends on your.....LUCK!")

user_id = str(uuid.uuid4())[:6]
balance = random.randint(100, 500)
games_played = 0
games_won = 0
games_lost = 0

user_name = str(input(Fore.BLACK + "Please enter your name to get registered in our Casino: "))

while True:
    overview = (Fore.LIGHTRED_EX + f"{user_name.capitalize()}, You are in the Casino!\nChoose an option from below: \n1. Stats\n2. Dice roll (Game 1)\n3. Lucky Number (Game 2)\n4. Exit Menu")
    print(overview)
    choose_overview = int(input(Fore.BLACK + "Use Numbers to Navigate: "))
    print(choose_overview)

    # Stats

    if choose_overview == 1:
        print(f"Your Casino Stats:\nUser_ID: {user_id}\nUsername: {user_name.capitalize()}\nCurrent Balance: ${balance}\nGames Played: {games_played}\nGames Won: {games_won}\nGames Lost: {games_lost}")
        input("Press Enter to get back to Main Menu...")

    # Game 2, dice roll

    if choose_overview == 2:
        print("Dice Roll, in this game you pick a side between 2. If it rolls in your favour, you win. Else... we all know.\nA quick and risky bet... will the dice roll in your favor? We will find out!")
        ask_wager1 = int(input("How much amount do you wanna wager? : "))
        roll = random.randint(1, 6)
        print(f"{roll} is lucky roll for this")  # testing winning prints
        ask_side = int(input(f"Your Wager Amount is ${ask_wager1}, Starting now.....\nPick a side:\n1. Low Roll (1 to 3)\n2. High Roll (4 to 6)\nYour choice (1 or 2): "))

        if ask_side not in [1, 2]:
            print("Invalid side chosen! Please choose 1 or 2.")
            print(ask_side)
        else:
            print("Rolling the dice.......")
            time.sleep(1.5)
            print("Checking your luck....")
            time.sleep(1.5)
            print(f"The dice rolled: {roll}")

            if ask_side == 1 and roll in [1, 2, 3]:
                print(f"You guessed it right! You win ${ask_wager1 * 2}")
                balance += ask_wager1 * 2
                games_played += 1
                games_won += 1
                input("Press Enter to get back to Main Menu...")

            elif ask_side == 2 and roll in [4, 5, 6]:
                print(f"You guessed it right! You win ${ask_wager1 * 2}")
                balance += ask_wager1 * 2
                games_played += 1
                games_won += 1
                input("Press Enter to get back to Main Menu...")

            else:
                print(f"Ahh dang it! You have lost ${ask_wager1}")
                balance -= ask_wager1
                games_played += 1
                games_lost += 1
                input("Press Enter to get back to Main Menu...")

    # Game 3, lucky number

    if choose_overview == 3:
        print(Fore.MAGENTA + "Welcome to the Lucky Number game, in this game you choose a number between 1 to 6, if your number is the Lucky one, you win 3x of your wager! Good luck. ")
        lucky_num = random.randint(1,6)
        print(f"{lucky_num} is Lucky number for this game") #testing winning prints
        ask_wager = int(input("How much amount do you wanna wager? : "))
        print(ask_wager)
        ask_num = int(input(f"Your Wager Amount is ${ask_wager}, Starting now.....\nWhat is your lucky number?:"))
        if ask_num > 6:
            print (int(input("Invalid Number! Give a number between 1 to 6:")))
            print(ask_num)
        else:
             print(ask_num)
             print("Rolling the dice.......")
             time.sleep(1.5)
             print("Checking your luck....")
             time.sleep(1.5)
        if ask_num == lucky_num:
                print(f"Hooray! Your guess was correct. You have won ${ask_wager*3}! ")
                balance += ask_wager*3
                games_played += 1
                games_won += 1
                input("Press Enter to get back to Main Menu...")
        else:
                print(f"Ahh dang it! You have lost ${ask_wager}")
                balance -= ask_wager
                games_played += 1
                games_lost += 1
                input("Press Enter to get back to Main Menu...")

            # Exit Menu
    if choose_overview == 4:
         print("Exiting the casino......")
         time.sleep(1.2)
         print("Casino Ecxited!")
         break

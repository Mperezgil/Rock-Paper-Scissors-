print("Made by Micahel Perez Gil!")
loose = ("The computer wins!")
win = ("You win!")
lives = 5
score = 0
drew = 0
computer_lives = 7
while True:
  print("To being fill in the information below.")
  print("The username and password is admin")
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")
  searchfile = open("accounts.csv", "r")
  for line in searchfile:
    if username and password in line:
      print("Access Granted")
      print("")
      print("")
      print(
        "In the year 2050, the machines rose from the advances of artifical intelligence."
      )
      print(
        "Their war to exterminate mankind had raged for decades, but the the final battle"
      )
      print(
        "Would not be fought in the future. It would be fought here, in our present."
      )
      print("The fate of human kind rests in your hands, in a game of...")
      print("")
      print("")
      print(
        "------------      ---------------    --------------    -----     ------"
      )
      print(
        "--------------    ---------------    --------------    -----     -----"
      )
      print(
        "----       ---    ----       ----    ----              -----    ----")
      print(
        "----     ----     ----       ----    ----              -----  ----")
      print("-----------       ----       ----    ----              ---------")
      print(
        "----    ------    ----       ----    ----              -----  ----")
      print(
        "----     -----    ---------------    --------------    -----    ----")
      print(
        "----      ----    ---------------    --------------    -----      -----"
      )
      print("")
      print("")
      print(
        "----------------      -----------------     ----------------      -----------------     ----------------"
      )
      print(
        "-----------------     -----------------     -----------------     -----------------     -----------------"
      )
      print(
        "----         ----     -----       -----     ----         ----     -----                 ----         ----"
      )
      print(
        "----        ----      -----       -----     ----        ----      -----                 ----        ----"
      )
      print(
        "----      ----        -----       -----     ----      ----        -----------------     ----      ----"
      )
      print(
        "-------------         -----------------     -------------         -----------------     -------------"
      )
      print(
        "------------          -----------------     ------------          -----------------     -------------"
      )
      print(
        "----                  -----       -----     ----                  -----                 ----      ----"
      )
      print(
        "----                  -----       -----     ----                  -----                 ----       ----"
      )
      print(
        "----                  -----       -----     ----                  -----------------     ----        ----"
      )
      print("")
      print("")
      print(
        "------------------     ------------------     ------------------     ------------------     ------------------     ------------------     ----------------"
      )
      print(
        "------------------     ------------------     ------------------     ------------------     ------------------     ------------------     -----------------"
      )
      print(
        "-----                  -----                        ------           -----                  -----                  -----        -----     ----         ----"
      )
      print(
        "-----                  -----                        ------           -----                  -----                  -----        -----     ----        ----"
      )
      print(
        "------------------     -----                        ------           ------------------     ------------------     -----        -----     ----      ----"
      )
      print(
        "------------------     -----                        ------           ------------------     ------------------     -----        -----     -------------"
      )
      print(
        "             -----     -----                        ------                        -----                  -----     -----        -----     -------------"
      )
      print(
        "             -----     -----                        ------                        -----                  -----     -----        -----     ----      ----"
      )
      print(
        "------------------     ------------------     ------------------     ------------------     ------------------     ------------------     ----       ----"
      )
      print(
        "------------------     ------------------     ------------------     ------------------     ------------------     ------------------     ----        ----"
      )
      print("Live Rules")
      print("You start with", lives, "lives")
      print("If you win you get a extrea live.")
      print("If you loose you loose a live.")
      print("If you draw the lives will remain the same.")
      print("--------------------------------------------------")
      print("MAKE SURE YOU DON'T USE CAPITALS!!!")
      print("--------------------------------------------------")
      print("To see a list of rules type rules")
      print("--------------------------------------------------")
      print("The computer has lives aswell.")
      print("Can you beat the computer?")
      print("Good Luck!!!")
      print("--------------------------------------------------")
      while True:
        rps = input("Rock, Paper, or Scissors?   ")
        import random
        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        #rock if statements
        if rps == "rock" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print("You lost this round!")
          print("")
          print("")
          lives -= 1
        if rps == "rock" and computer == "scissors":
          print("The computer chose", computer)
          print("")
          print("You won this round!")
          print("")
          print("")
          score += 1
          #paper if statements
        if rps == "paper" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print("You won this round!")
          computer_lives -= 1
          print("")
          print("")
          score += 1
        if rps == "paper" and computer == "scissors":
          print("The computer chose", computer)
          print("")
          print("You lost this round!")
          print("")
          print("")
          lives -= 1
        #scissor if statements
        if rps == "scissors" and computer == "paper":
          print("The computer chose", computer)
          print("")
          print("You won this round!")
          computer_lives -= 1
          print("")
          print("")
          score += 1
        if rps == "scissors" and computer == "rock":
          print("The computer chose", computer)
          print("")
          print("You lost this round!")
          print("")
          print("")
          lives -= 1
        #duplicates
        if rps == "rock" and computer == "rock":
          print("The computer choose", computer)
          print("")
          print("You Drew!")
          print("")
          print("")
          drew += 1
        if rps == "paper" and computer == "paper":
          print("The computer choose", computer)
          print("")
          print("You Drew!")
          print("")
          print("")
          drew += 1
        if rps == "scissors" and computer == "scissors":
          print("The computer choose", computer)
          print("")
          print("You Drew!")
          print("")
          print("")
          drew += 1
        #system
        if rps == "rules":
          print("**************************************")
          print("Rules")
          print("**************************************")
          print("-Rock looses against Paper")
          print("-Rock beats Scissors")
          print("-Paper beats Rock")
          print("-Paper looses against Scissors")
          print("-Scissors beats Paper")
          print("-Scissors looses against Rock")
          print("**************************************")
        if rps == "display lives":
          print(lives)
        if rps == "display score":
          print(score)
        if rps == "display drew":
          print(drew)

        #lives
        if lives == 0 or rps == "test":
          print("Thanks for playing.")
          print("You have run out of lives")
          print("The machines have won...")
          print("")
          print("")
          print("     _.-^^---....,,--       ")
          print(" _--                  --_  ")
          print("<                        >)")
          print("|                         | ")
          print(" \._                   _./  ")
          print("    ```--. . , ; .--'''  ")
          print("          | |   |             ")
          print("       .-=||  | |=-.   ")
          print("       `-=#$%&%$#=-' ")
          print("          | ;  :|     ")
          print(" _____.,-#%&$@%#&#~,._____")
          print("")
          print("")
          print("You got", score, "correct")
          print("You drew", drew, "times")
          stop = input("Press enter to exit.")
          import time
          time.sleep(900)
        if computer_lives == 0:
          print("Thanks for playing.")
          print("The computer lost all its lives. You Win")
          print("You have saved humanity!!")
          print("")
          print("")
          print("░░░░░░░░░░░░░░░░░░░░░░█████████")
          print("░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███")
          print("░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███")
          print("░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
          print("░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███")
          print("░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██")
          print("░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
          print("░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██")
          print("░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██")
          print("██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██")
          print("█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██")
          print("██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
          print("░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██")
          print("░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█")
          print("░░████████████░░░█████████████████")
          print("")
          print("")
          print("You got", score, "correct")
          print("You drew", drew, "times")
          import time
          time.sleep(900)
        #exit
        if rps == "exit":
          break
    else:
      print("Your username or password is incorrect.")
      print("---------------------------------------")

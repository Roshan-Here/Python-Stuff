#Rock-papper-sissor
import random
cmp_sc = 0
usr_sc = 0
#rock:0, paper:1, scissor:2
GAME = ["rock","paper","scissor"]
while True:
    wow_input = input("Type Rock/Paper/Scissor or Q to Quit ~ ").lower()
    if wow_input == "q":
        break
    if wow_input not in GAME:
        print("invalid option !!!")
        continue
    random_number = random.randint(0,2)
    cmp_pick = GAME[random_number]
    print(f"Computer picked {cmp_pick}")
    if wow_input == cmp_pick:
        print(f"Same bruh, {cmp_pick}")
        continue
    elif cmp_pick == "scissor" and wow_input == "rock":
        print("You won!!!")
        usr_sc += 1
        continue
    elif cmp_pick == "paper" and wow_input == "scissor":
        print("You won!!!")
        usr_sc += 1
        continue
    elif cmp_pick == "rock" and wow_input == "paper":
        print("You won!!!")
        usr_sc += 1
        continue
    else:
        print("Computer Won!!")
        cmp_sc += 1
print(f"""
    your Score : {usr_sc}
    Computer Score : {cmp_sc}
""")
print("Thanks for playing :)")

#Word-Number-Guessing
import random
print("lets play no: Guessing")
givn_number = input("Giv me your no btwn 1-10  ~ ")
if givn_number.isdigit():
    givn_number = int(givn_number)
else:
    print("Not a number!!! ")
    quit()

random_number = random.randrange(0,11)
if random_number == givn_number:
    print(f"Wow Congrats!! nice guessing {givn_number} = {random_number}")
else:
    print("Ooooopz not matching no: ",random_number)
print("""
    Thank you for playing!!!""")

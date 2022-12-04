#Quiz time
WOW = ['central processing unit','network operating system','motherboard','metropolitan area network'
       ,'start','compiler','charles babbage','1024','rom','master file']
score = 0

print("its Quiz time guys !!!")
Wanna_Play = input("Do you wanna play ?? y/n - ")

if Wanna_Play.lower() != "y" :
    quit()
else:
    print("""
    its time Guys!!!! lets begin,- all questions are related to CS :)
    """)
#1
quex = input("What is CPU ,full form ")
if quex.lower() == WOW[0]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[0]}")
#2
quex = input("Full form of NOS? ")
if quex.lower() == WOW[1]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[1]}")
#3
quex = input("Where are the CPU and memory located? ")
if quex.lower() == WOW[2]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[2]}")
#4
quex = input("Full form of MAN? ")
if quex.lower() == WOW[3]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[3]}")
#5
quex = input("Help Menu is available at which button? ")
if quex.lower() == WOW[4]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[4]}")
#6
quex = input("What converts an entire program into machine language? ")
if quex.lower() == WOW[5]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[5]}")
#7
quex = input("Who is the father of Computer science? ")
if quex.lower() == WOW[6]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[6]}")
#8
quex = input("No. of different characters in ASCII coding system? ")
if quex.lower() == WOW[7]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[7]}")
#9
quex = input("What kind of memory is both static and non-volatile? ")
if quex.lower() == WOW[8]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[8]}")
#10
quex = input("Which file contains permanent data and gets updated during the processing of transactions? ")

if quex.lower() == WOW[9]:
    print("Correct")
    score += 1
else:
    print(f"incorrect !! correct ans is : {WOW[9]}")
print("your total score ",score)
print("""

    Thankyou for playing :)
    """)


#~~Note all questions are taken from (https://www.yeahhub.com/100-basic-computer-related-g-k-questions)

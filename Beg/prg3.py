# emogi crush` not completedd
import random
print("Lets play !!!")
BoardList = []
elelments = ["🤣","🥰","🤩","🎄","💥"]
for i in range(25):
    BoardList.append(random.choice(elelments))
print(BoardList)

def PrintBoard(list):
  temp = 0
  for i in range(5):
    for j in range(5):
      print(list[temp],end="")
      temp += 1
    print("")
PrintBoard(BoardList)
print("")

def takeinput():
  currentPos = input("Enter the Position of the item to move ~ ")
  futurePos = input("Enter thw now position ~ ")
  return [currentPos,futurePos]
# to get Board Refenece
def BoardRef():
  temp = 0
  for i in range(5):
    for j in range(5):
      print(temp,end="")
      temp += 1
    print("")
print(BoardRef())
# to get combinations 
def getCombination(num):
  # horizontal 
  c1 = [num-2,num-1,num]
  c2 = [num,num+1,num+3]
  c3 = [num-1,num,num+1]
  # vertical
  c4 = [num-10,num-5,num]
  c5 = [num,num+5,num+10]
  c6 = [num-5,num,num+10]

  return [c1,c2,c3,c4,c5,c6]
print(getCombination(12))
# RUN ~ this much & look again its simple

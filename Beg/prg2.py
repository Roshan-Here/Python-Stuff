#Write A function to check if a number is prime or not
#Use that function, and print first 100 prime numbers

val = int(input("Giv me some value to check !!! "))

def CheckPrime(num):
    if num>1:
        wow = []
        for x in range(2,num):
            if (num%x) == 0:
                print("its a prime value = ",x)
            else:
                wow.insert(num,x)
        else:
            print("Done :)")
            print(f"non prime numbers {wow}")

CheckPrime(val)
print("""
        Lets find First 100 prime numbers
      """)
CheckPrime(100)

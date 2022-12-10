# checking inbuild-replace fuction
def Word_Replacement():
    Given_String = "heii,,,, hola Amigo bei,,,,,,,,,,,"
    print("Given String : ",Given_String)
    Wanna_Change_String = input("Wanna Change String y/n ?~ ").lower()
    if Wanna_Change_String == "y":
        Given_String = input("Giv new String : ")
        print("New String : ", Given_String)
    elif Wanna_Change_String == "n":
        pass
    else:
        print("invalid option")
    R_Word = input("word to replace ~ ")
    Replacement_Word = input("Giv which word to from String ~ ")
    print("Final Product")
    print("")
    print(Given_String.replace(R_Word,Replacement_Word))

Word_Replacement()

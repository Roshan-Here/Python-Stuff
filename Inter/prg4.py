#passs-manager
#Generel password = password
main_pwd = input("Enter the Main password ~ ")
if main_pwd != "password":
    print("Not Correct password~ readCodde!!!")
    quit()
def view():
    with open("passwords.txt","r") as f:
        for x in f.readlines():
            data = x.rstrip()
            user, passw = data.split("|")
            print("User : ", user, ", password : ",passw)
def add():
    name = input("Whats ur name ??? ~ ")
    pwd = input("Whats ur password >> ")
    # with used bcoz no  need of closing the file
    with open("passwords.txt",'a') as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("would u like to add new password or view (add/view) or Quit Q ?? ~ ").lower()
    if mode == "q":
        break
    elif mode == "add":
        add()
        pass
    elif mode == "view":
        view()
        pass
    else:
        print("invalid statement")
        break

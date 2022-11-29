print("Enter Login = 1, Registration = 2, forgot password = 3  ")
z = int(input(""))
if z == 1:
    UserName = input("\nEnter email ID or User name: ")
    userpass = input("\n Enter password: ")
    file10=open("joyal10.txt", "r")
    if UserName==file10.read():
      print("username is correct")
    else:
      print("username is wrong or create account")
    file10.close()
    file20=open("joyal20.txt", "r")
    if userpass==file20.read():
      print("password is correct")
    else:
      print("password is wrong")
    file20.close()


elif z == 2:
    print("\nEmail or user name should have @ followed by .   \n example : joyalthomas@gmail.com ")
    print("It should not be like this eg:- @gmail.com ")
    print("There should not be any . immediate next to @ \n example joyal@.com ")
    print("It should not start with special characters and numbers \n eg:- 123#@gmail.com")
    a = input("Create email ID or User name to signup: ")
    sum = 0
    min = 0
    count = 0
    count2 = 0
    count3 = 0
    txt = []
    for i in a:
        if i == '@':
            sum += 1
        elif i == '.':
            min += 1
    if sum == 1 and min == 1:
        d, e = a.split('@')
        f, g = e.split(".")
        for i in f:
            count += 1
        for i in d:
            count2 += 1
        if g == "com":
            count3 = 1
        for i in d:
            txt.append(i)
            txt1 = txt[0]
        x = txt1.isalpha()
        if x != True:
            count2 = 0
        if count >= 4 and count2 >= 1 and count3 == 1:
            print("Your ID is accepted")
            y = a
        else:
            print("You ented a mistake")



    flagcount = 0
    flaga = 0
    flagnum = 0
    flagup = 0
    flaglow = 0
    flagspec = 0
    print(
        " Create password, Length of password must be more than 5 and less than 16 \nMust have minimum one special character \none digit \none uppercase \none lowercase character ")
    password = input("Enter password: ")

    for i in password:
        flagcount += 1

        if i.isalpha() == True:
            flaga += 1
        elif i.isnumeric() == True:
            flagnum += 1
        else:
            flagspec += 1

    flagup = (any(c.isupper() for c in password))
    flaglow = (any(c.islower() for c in password))
    if flagcount > 5 and flagcount < 16 and flaga >= 1 and flagnum >= 1 and flagspec >= 1 and flagup == True and flaglow == True:
        print("Your Password accepted")
    else:
        print("password is wrong")

    file10=open("joyal10.txt", "w")
    text = [a]
    file10.writelines(text)
    file20=open("joyal20.txt", "w")
    text = [password]
    file20.writelines(text)

elif z == 3:
  p=input("enter your email id or username")
  file10=open("joyal10.txt", "r")
  if p == file10.read():
    file20=open("joyal20.txt", "r")
    print(file20.read())
    file10.close()
    file20.close()
  else:
    print("your email id or user name is wrong, create account")
else:
    print("You enterd a wrong input: ")

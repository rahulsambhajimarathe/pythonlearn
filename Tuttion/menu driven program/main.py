import os



while True:
    print("========================================")
    print("menu driven program for file managment project")
    print("========================================")
    print("1. For Add User")
    print("2. Display ALl User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit the program")
    print("6. search user")
    print("========================================")
    choice = input("enter your index: \t")

    # add a user
    if choice == "1":

        f = open('data.txt', 'a')
        ans = "y"
        while ans == "y" or ans == "Y":
            roll = input("enter a roll number : \t")
            name = input("enter a name : \t")
            phone = input("enter a number : \t")
            rec = roll+"\t"+name+"\t"+phone+"\n"
            f.write(rec)
            ans = input("Do You want to add another record Y/N")
        f.close()


    # dispaly all user
    elif choice == "2":
        f = open("data.txt", "r")
        for i in f:
            print("========================================")
            print(i)
            print("========================================")
        input()
        f.close()
        print("display a value")

    # update user
    elif choice == "3":
        f = open("data.txt", "r")
        fone = open("temp.txt", "w")
        ans = 0
        rn = input("enter user roll number to update : ")
        for x in f:
            rec = x.split()
            if rec.count(rn) == 1:
                print(x)
                rn = input("enter new roll number : ")
                name = input("enter new name : ")
                number   = input("enter new number : ")
                rec = rn + "\t" + name + "\t" + number + "\n"
                fone.write(rec)

                ans = 1
            else:
                fone.write(x)
        f.close()
        fone.close()
        os.remove("data.txt")
        os.rename("temp.txt", "data.txt")
        if ans == 0:
            print("record not found")
            input()
        print("update a value")

    # delete the user for the file
    elif choice == "4":
        f = open("data.txt", "r")
        fone = open("temp.txt", "w")
        ans = 0
        rn = input("enter user roll number to delete : ")
        for x in f:
            rec = x.split()
            if rec.count(rn) == 1:
                print(x)
                print("this record will be deleted ")
                input()
                ans = 1
                continue

            else:
                fone.write(x)
        f.close()
        fone.close()
        os.remove("data.txt")
        os.rename("temp.txt", "data.txt")
        if ans == 0:
            print("record not found")
            input()
        print("update a value")

    # exit the poll modi ji
    elif choice == "5":
        print("exit ...........")
        break


    # seacrch the record
    elif choice == "6":
        f = open('data.txt', "r")
        ans =0
        rn = input("enter the roll number you want to search : \t")
        for x in f:
            rec = x.split()
            if rec.count(rn) == 1:
                print(x)
                input()
                ans = 1
                break
        if ans == 0:
            print("no record found")
        f.close()
    else:
        print("Somitng went wrong re enter the value")
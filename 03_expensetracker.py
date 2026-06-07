# Project: create a expense tracker program in python that allows user to record daily expenses and 
# view summaries like total spending. Use only the concept learned tillchapter 6
print("----WELCOME TO THE EXPENSE TRACKER DEVICE----")
expenselist = []  # list of all expenses in the form of dictionary

# agar user se choice lena ho toh hamesha ye condition valid hai
while True:
    print("======MENU======")
    print("1. Add Expenses")
    print("2. View all Expenses")
    print("3. Total kharcha")
    print("4. Exit")
    
    choice = int(input("Enter your choice(1-4): "))

    if choice==1:
        date = input("Konse date ko kharcha kiya tumne: ")
        category = input("Konsa chij liyaa tumne: ")
        description = input("Aur detail dedo: ")
        amount = float(input("Kitne kaa tha vo: "))

        print("Expenses added successfully")

     #Ab dict mai add kardo in sabko
        expenses = {"Date" : date,
                    "Category" : category,
                    "Description" : description,
                    "Amount" : amount}

     # ab is dict ko list mai add kardo
        expenselist.append(expenses)

    elif choice==2:
        if len(expenselist) == 0:
            print("No expenses added")
        else:
            print("Ye hai aapke saare expenses")
            count = 1
            for eachkharcha in expenselist:
                print(f"Kharcha number{count} -> {eachkharcha["Date"]}, {eachkharcha["Category"]}, {eachkharcha["Description"]}, {eachkharcha["Amount"]}")
                count += 1

    elif choice == 3:
        total = 0
        for eachkharcha in expenselist:
            total = total + eachkharcha["Amount"]
        print("Total kharcha: ",total)

    elif choice == 4:
        print("Thankyou for visiting our app")
        break

    else:
        print("Invalid choice.Try again")

            
        

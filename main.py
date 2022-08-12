import sqlite3

MENU_PROMPT = """ --- Contact Book App ---

Please Choose one of these options ;

1) Add a new Contact 
2) See all Contacts
3) Delete a Contact
4) Update a Contact
5) Exit

Your Selection: """



connector = sqlite3.connect('data.db')
cursor = connector.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS CONTACTBOOK (Id INTEGER PRIMARY KEY, NAME TEXT, ADDRESS TEXT, EMAILADDRESS TEXT, PHONENUMBER INTEGER )")
connector.commit()

def menu():
    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input =="1":
            global Name, Address, EmailAddress, PhoneNumber
            Name = input("Enter name  : ")
            Address = input("Enter address  : ")
            EmailAddress = input("Enter emailaddress : ")
            PhoneNumber = input("Enter phone number : ")

            connector = sqlite3.connect('data.db')
            cursor = connector.cursor()
            cursor.execute("INSERT INTO CONTACTBOOK (Name, Address, EmailAddress, Phonenumber) VALUES (?, ?, ?, ?)", (Name, Address, EmailAddress, PhoneNumber ))
            connector.commit()


        elif user_input =="2":
            connector = sqlite3.connect('data.db')
            cursor = connector.execute("SELECT * FROM CONTACTBOOK")
            fetch = cursor.fetchall()

            for data in fetch:
                print(data)



        elif user_input =="3":
            connector = sqlite3.connect('data.db')
            cursor = connector.cursor()
            Name = input("Enter name you want to delete  : ")
            cursor.execute("DELETE FROM CONTACTBOOK WHERE Name = ? ",[Name])
            connector.commit()
            print(f"{Name} Has been Deleted from the app ")

            
        elif user_input =="4":
            connector = sqlite3.connect('data.db')
            cursor = connector.cursor()
            Id = input("Enter ID want to update  : ")
            Name = input("Enter New Name")
            Address = input("Enter New address  : ")
            EmailAddress = input("Enter New emailaddress : ")
            PhoneNumber = input("Enter New phone number : ")
            cursor.execute("Update CONTACTBOOK SET Name = ? , Address = ?, EmailAddress = ?, PhoneNumber = ? WHERE ID= ?  ",[Name,Address,EmailAddress,PhoneNumber,Id])


            connector.commit()
            print(f" ALL INFORMATION HAS BEEN UPDATED")



        else:
            print("Invalid input , Please try again")

menu()
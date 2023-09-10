import os
from mysql.connector import *

# Connect to the MySQL database
db = connect(
    host="localhost",  
    user="root",       
    password="",  
    database="files_managment"
)
cursor = db.cursor()

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
    # Add a user
    if choice == "1":
        roll = input("Enter a roll number: ")
        name = input("Enter a name: ")
        phone = input("Enter a number: ")

        # Insert user record into the MySQL table
        sql = f"INSERT INTO users (roll_number, name, phone) VALUES ({roll}, {name}, {phone})"
        cursor.execute(sql)
        print("User added successfully.")

    # Display all users
    elif choice == "2":
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        for user in users:
            print("========================================")
            print(f"ID: {user[0]}")
            print(f"Roll Number: {user[1]}")
            print(f"Name: {user[2]}")
            print(f"Phone: {user[3]}")
            print("========================================")
        input("Press Enter to continue...")

    # Update user
    elif choice == "3":
        user_id = int(input("Enter the ID of the user to update: "))
        new_roll = input("Enter new roll number: ")
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone number: ")

        sql = f"UPDATE users SET roll_number = {new_roll}, name = {new_name}, phone = {user_id} WHERE id = {user_id}"
        cursor.execute(sql)
        db.commit()
        print("User updated successfully.")

    # Delete user
    elif choice == "4":
        user_id = int(input("Enter the ID of the user to delete: "))

        # Delete user record from the MySQL table
        sql = f"DELETE FROM users WHERE id = {user_id}"
        cursor.execute(sql)
        db.commit()
        print("User deleted successfully.")

    # Search for a user
    elif choice == "6":
        search_roll = input("Enter the roll number to search for: ")

        # Search for user record in the MySQL table
        sql = f"SELECT * FROM users WHERE roll_number = {search_roll}"
        cursor.execute(sql)
        user = cursor.fetchone()
        if user:
            print("========================================")
            print(f"ID: {user[0]}")
            print(f"Roll Number: {user[1]}")
            print(f"Name: {user[2]}")
            print(f"Phone: {user[3]}")
            print("========================================")
        else:
            print("No record found.")

    # Exit
    elif choice == "5":
        print("Exit...")
        break

    else:
        print("Something went wrong. Please re-enter the value.")



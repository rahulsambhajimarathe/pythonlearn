import os
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="file_manage"
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
    
    if choice == "1":
        roll = input("Enter a roll number: ")
        name = input("Enter a name: ")
        phone = input("Enter a number: ")

        # Insert user record into the MySQL table
        sql = "INSERT INTO users (roll_number, name, phone) VALUES (%s, %s, %s)"
        values = (roll, name, phone)
        cursor.execute(sql, values)
        db.commit()
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
        user_id = input("Enter the ID of the user to update: ")
        new_roll = input("Enter new roll number: ")
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone number: ")

        # Update user record in the MySQL table
        sql = "UPDATE users SET roll_number = %s, name = %s, phone = %s WHERE id = %s"
        values = (new_roll, new_name, new_phone, user_id)
        cursor.execute(sql, values)
        db.commit()
        print("User updated successfully.")

    # Delete user
    elif choice == "4":
        user_id = input("Enter the ID of the user to delete: ")

        # Delete user record from the MySQL table
        sql = "DELETE FROM users WHERE id = %s"
        values = (user_id,)
        cursor.execute(sql, values)
        db.commit()
        print("User deleted successfully.")

    # Search for a user
    elif choice == "6":
        search_roll = input("Enter the roll number to search for: ")

        # Search for user record in the MySQL table
        sql = "SELECT * FROM users WHERE roll_number = %s"
        values = (search_roll,)
        cursor.execute(sql, values)
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

# Close the MySQL database connection
cursor.close()
db.close()

import pickle
import os

class Person:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
       
# save function 
def save_to_file(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
        
def load_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data
    return []


# creat function
def create_new_person():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    return Person(name, phone, email)


# show function
def show_person_info(person):
    print("Name:", person.name)
    print("Phone:", person.phone)
    print("Email:", person.email)



def main():
    filename = "data.txt"
    data = load_from_file(filename)

    while True:
        print("\nAddress Book Menu")
        print("1. Add New Person")
        print("2. View All People")
        print("5. Exit")

        choice = input("Choose an option: ")

        # this is me adding
        if choice == '1':
            new_person = create_new_person()
            data.append(new_person)
            save_to_file(data, filename)
            print("Person added successfully!")
            
        # this is me showing
        elif choice == '2':
            if not data:
                print("Not people in the list.")
            else:
                for idx, person in enumerate(data, start=1):
                    print("=============")
                    print("")
                    print("Person", idx)
                    show_person_info(person)
                    print("")
                    
                    
        # this is me exiting
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("select a vooret option.")


main()

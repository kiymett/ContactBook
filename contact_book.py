def contact_menu(contacts):
    print("**** Contact Book Menu ****")
    print("---- Total ",len(contacts), " contacts ----")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contact")
    print("4. Search Contact")
    print("5. Save Contacts")
    print("6. Exit Contact Book")
    selection = int(input("Enter your selection (1-6): "))
    return selection

def add_contact():
    addnew = "Yes"
    contact_list = []
    while addnew == "Yes" or addnew == "yes":
        name = str(input("Enter the name of the contact: "))
        address = input("Enter the address of the contact: ")
        phone = input("Enter the phone number of the contact: ")
        email = input("Enter the email of the contact: ")
        contact_dict = {}
        contact_dict["name"] = name
        contact_dict["phone"] = phone
        contact_dict["address"] = address
        contact_dict["email"] = email
        contact_list.append(contact_dict)
        print("Do you want to add a new contact?: (Yes/No): ")
        addnew = str(input())
        if addnew == "No" or addnew == "no":
            print("You have added ",len(contact_list)," new contact/s")
    return contact_list

def list_contact(contacts):
    print("List Contact function....")
    for idx in range(len(contacts)):
        print(idx+1,". Contact")
        contact_dict = contacts[idx]
        print("- Name: ", contact_dict["name"])
        print("- Phone: ", contact_dict["phone"])
        print("- Address: ", contact_dict["address"])
        print("- Email: ", contact_dict["email"])

def search_contact(contacts):
    option = input("What do you want to search (name, phone, address or email)?: ")
    found_index = -1
    if option=="name":
        contact_name = input("Please enter name of the contact: ")
        for idx in range(len(contacts)):
            contact_dict = contacts[idx]
            if contact_dict["name"] == contact_name:
                found_index = idx
    elif option=="phone":
        contact_phone = input("Please enter phone of the contact: ")
        for idx in range(len(contacts)):
            contact_dict = contacts[idx]
            if contact_dict["phone"] == contact_phone:
                found_index = idx
    elif option=="address":
        contact_address = input("Please enter address of the contact: ")
        for idx in range(len(contacts)):
            contact_dict = contacts[idx]
            if contact_dict["address"] == contact_address:
                found_index = idx
    elif option =="email":
        contact_email=input("Please enter email of the contact: ")
        for idx in range(len(contacts)):
            contact_dict=contacts[idx]
            if contact_dict["email"] == contact_email:
                found_index = idx
    else:
        print("Invalid option! Please enter name, phone, address or email")
    if found_index == -1:
        print("No contacts found!")
    else:
        print("Contact found: ",contacts[found_index])
    return found_index

def delete_contact(contacts):
    print("Search contact to delete...")
    delete_index=search_contact(contacts)
    if delete_index==-1:
        print("No contacts deleted!")
    else:
        contacts.pop(delete_index)
        print("Contact deleted! Please save before continue")

def save_contacts(contacts, file_name):
    f = open(file_name, "w")

    print("Saving contacts...")
    for contact in contacts:
        f.write(str(contact) + "\n")
    print("Contacts save to ",file_name)
    f.close()

def load_contacts(file_name):
    fr = open(file_name, "r")
    contact_list = []
    for line in fr:
        line_list = line.rstrip().split(" ")
        contact_dict = {}
        contact_dict["name"] = line_list[1][1:-2]
        contact_dict["phone"] = line_list[3][1:-2]
        contact_dict["address"] = line_list[5][1:-2]
        contact_dict["email"] = line_list[7][1:-2]
        contact_list.append(contact_dict)

    return contact_list

contacts = []
contacts=load_contacts("my_contacts.txt")
menu_selection=0
while menu_selection != 6:

    menu_selection = contact_menu(contacts)
    if menu_selection == 1:
        contacts.extend(add_contact())
    elif menu_selection == 2:
        delete_contact(contacts)
    elif menu_selection == 3:
        list_contact(contacts)
    elif menu_selection == 4:
        search_contact(contacts)
    elif menu_selection == 5:
        save_contacts(contacts, "my_contacts.txt")
    elif menu_selection == 6:
        print("Exiting Contact Book...")
    else:
        print("Wrong selection!")








contacts={}
while True:
    print("\n1.Add Contact")
    print("2.View Contacts")
    print("3.Search Contact")
    print("4.Update Contact")
    print("5.Delete Contact")
    print("6.Exit")
    choice=input("Enter choice: ")
    if choice=="1":
        name=input("Name: ")
        phone=input("Phone: ")
        email=input("Email: ")
        address=input("Address: ")
        contacts[name]=[phone, email, address]
        print("Contact Added!")
    elif choice=="2":
        for name, details in contacts.items():
            print("\nName:", name)
            print("Phone:", details[0])
    elif choice=="3":
        name=input("Enter name: ")
        if name in contacts:
            print("Phone:", contacts[name][0])
            print("Email:", contacts[name][1])
            print("Address:", contacts[name][2])
        else:
            print("Contact Not Found")
    elif choice=="4":
        name=input("Enter name to update: ")
        if name in contacts:
            contacts[name][0]=input("New Phone: ")
            contacts[name][1]=input("New Email: ")
            contacts[name][2]=input("New Address: ")
            print("Contact Updated!")
        else:
            print("Contact Not Found")
    elif choice=="5":
        name=input("Enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact Deleted!")
        else:
            print("Contact Not Found")
    elif choice=="6":
        print("Exit")
        break
    else:
        print("Invalid Choice")


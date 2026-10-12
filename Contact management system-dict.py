contacts={}
while True:
    print("\n CONTACT MANAGEMENT SYSTEM")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Display Contact")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        name=input("Enter Name")
        phone=input("Enter Contact number:")
        contacts[name]=phone
        print("Contact added successfully")
    elif(choice==2):
        name=input("Enter Name:")
        if name in contacts:
            print("phone:",contacts[name])
        else:
            print("Contact not found")
    elif(choice==3):
        name=input("Enter Name:")
        if name in contacts:
            phone=input("Enter New Phone number:")
            contacts[name]=phone
            print("Updated Successfully")
        else:
            print("Contact not found")
    elif(choice==4):
        name=input("Enter Name:")
        if name in contacts:
            del contacts[name]
            print("Delected Successfully")
        else:
            print("Contact not found")
    
    elif(choice==5):
        name=input("Enter Name:")
        for name,phone in contacts.items():
            print(name,"\t",phone)
    elif(choice==6):
        Print("Thankyou")
    else:
        print("Invalid")
    

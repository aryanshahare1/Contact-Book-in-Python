contacts = {}

while True:
    print('\nContact Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contacts')
    print('7. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input("Enter your name: ").lower() 
        if name in contacts:
            print(f"Contact name {name} already exists!")
        else:
            age = input("Enter age: ")
            email = input("Enter email: ")
            mobile = input("Enter the mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact name {name} has been created successfully!')

    elif choice == '2':
        name = input('Enter contact name to view: ').lower()  
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {contact["age"]}, Email: {contact["email"]}, Mobile Number: {contact["mobile"]}')
        else:
            print('Contact not found')

    elif choice == '3':
        name = input("Enter name to update contact: ").lower() 
        if name in contacts:
            age = input('Enter updated age: ')
            email = input('Enter updated email: ')
            mobile = input('Enter updated mobile number: ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact {name} has been updated successfully!')
        else:
            print("Contact not found")

    elif choice == '4':
        name = input('Enter contact name to delete: ').lower()  
        if name in contacts:
            del contacts[name]
            print(f'Contact {name} has been deleted successfully!')
        else:
            print('Contact not found')

    elif choice == '5':
        search_term = input('Enter name, email, or mobile number to search: ').lower()  
        found = False
        for name, details in contacts.items():
            if search_term in name or search_term in details['email'].lower() or search_term in details['mobile']:
                print(f'Found: Name: {name}, Age: {details["age"]}, Email: {details["email"]}, Mobile Number: {details["mobile"]}')
                found = True
        if not found:
            print('No contact found with the given search term.')

    elif choice == '6':
        print(f'Total contacts: {len(contacts)}')

    elif choice == '7':
        print('Exiting Contact Book App.')
        break

    else:
        print('Invalid choice! Please try again.')

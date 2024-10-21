from contact_menu import menu
import pickle
contact_book=[]
def add_contact(name,phone_no,email,address):
    contact_book.append({'name':name,"phone_no":phone_no,"email":email,"address":address})
def remove_contact(email):
    global contact_book
    contact_book=[contact for contact in contact_book if contact['email']!=email]
def view_contacts():
    if not contact_book:
        print("contact book is Empty")
    else:
        for contact in contact_book:
            print(f" Name:{contact['name']},Email:{contact['email']},phone_no:{contact['phone_no']},Address:{contact['address']}")
def save_contacts(filename):
    try:
        with open(filename,'wb') as f:
            pickle.dump(contact_book,f)
        print(f'contacts aved to {filename}')
    except Exception as e:
        
        print(f'error saving contacts:{e}')
def load_contacts(filename):
    global contact_book
    try:
        with open(filename,'rb') as f:
            contact_book=pickle.load(f)
            print(f'loaded {len(contact_book)} contacts')
    except FileNotFoundError:
        print("no previous contacts found")
    except Exception as e:
        print(f'error loading contacts:{e}')
load_contacts("contacts.data")
while(True):
    menu()
    choice=input("choose your option(1-5):")
    if choice=='1':
        name=input("enter name:")
        email=input("enter email:")
        phone_no=input("enter phone number:")
        address=input("enter address:")
        add_contact(name,phone_no,email,address)
        print(f"contact {name} added")
    elif choice=='2':
        email=input("enter email for removing.")
        remove_contact(email)
        print(f'contact with email{email} removed.')
    elif choice=='3':
        view_contacts()
    elif choice=='4':
        save_contacts('contacts.data')
        print("contacts saved")
    elif choice=='5':
        save_contacts('contacts.data')
        print("Existing the contact book")
        break
    else:
        print('invalid option please try again later')




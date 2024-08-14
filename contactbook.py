class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=None):
        if name in self.contacts:
            print(f"Contact {name} already exists.")
        else:
            self.contacts[name] = {
                'phone': phone,
                'email': email
            }
            print(f"Contact {name} added.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} removed.")
        else:
            print(f"Contact {name} does not exist.")

    def get_contact(self, name):
        return self.contacts.get(name, f"Contact {name} does not exist.")

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            print(f"Contact {name} updated.")
        else:
            print(f"Contact {name} does not exist.")

    def list_contacts(self):
        if self.contacts:
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
        else:
            print("No contacts in the contact book.")

# Usage example
contact_book = ContactBook()

# Adding contacts
contact_book.add_contact("Rohit sharma", "123-456-7890", "rohit.sh@example.com")
contact_book.add_contact("Steve Smith", "098-765-4321")

# Listing contacts
contact_book.list_contacts()

# Updating a contact
contact_book.update_contact("Rohit sharma", phone="111-222-3333")

# Retrieving a contact
print(contact_book.get_contact("Rohit sharma"))

# Removing a contact
contact_book.remove_contact("Steve Smith")

# Listing contacts again
contact_book.list_contacts()

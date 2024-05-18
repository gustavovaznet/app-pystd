# AGENDA APP
AGENDA = {}

# FUNCTIONS
# SHOW CONTACT FUNCTION
def show_contact():
    if AGENDA:
        for contact in AGENDA:
            get_contact(contact)
    else:
        print('>>>> Empty')

# GET CONTACT FUNCTION
def get_contact(contact):
    try:
        print('Name:', contact)
        print('Phone:', AGENDA[contact]['phone'])
        print('Email:', AGENDA[contact]['email'])
        print('Adress:', AGENDA[contact]['address'])
        print('--------------------------------------------')
    except KeyError:
        print('>>>> Contact does not exist')
    except Exception as error:
        print('>>>> Unexpected error occurred')
        print(error)

# READ CONTACT FUNCTION
def read_detail_contact():
    phone = input('Enter the phone: ')
    email = input('Enter the email: ')
    address = input('Enter the address: ')
    return phone, email, address

# INCLUD/EDIT CONTACT FUNCTION
def includ_edit_contact(contact, phone, email, address):
    AGENDA[contact] = {
        'phone': phone,
        'email': email,
        'address': address,
    }
    save()
    print()
    print('>>>> Contact {} included/edited with success!'.format(contact))
    print()

# DELETE CONTACT FUNCTION
def delete_contact(contact):
    try:
        AGENDA.pop(contact)
        save()
        print()
        print('>>>> Contact {} deleted with success!'.format(contact))
        print()
    except KeyError:
        print('>>>> Contact does not exist')
    except Exception as error:
        print('>>>> Unexpected error occurred')
        print(error)

# EXPORT CONTACT FUNCTION
def export_contact(archive_name):
    try:
        with open(archive_name, 'w') as archive:
            for contact in AGENDA:
                phone = AGENDA[contact]['phone']
                email = AGENDA[contact]['email']
                address = AGENDA[contact]['address']
                archive.write("{},{},{},{}\n".format(contact, phone, email, address))
        print('>>>> Agenda exported with success!')
    except Exception as error:
        print('>>>> Unexpected error occurred')
        print(error)

# IMPORT CONTACT FUNCTION
def import_contact(archive_name):
    try:
        with open(archive_name, 'r') as archive:
            lines = archive.readlines()
            for line in lines:
                details = line.strip().split(',')

                name = details[0]
                phone = details[1]
                email = details[2]
                address = details[3]

                includ_edit_contact(name, phone, email, address)
    except FileNotFoundError:
        print('>>>> Archive not found')
    except Exception as error:
        print('>>>> Unexpected error occurred')
        print(error)

# SAVE DATABASE FUNCTION
def save():
    export_contact('database.csv')

# LOAD DATABASE FUNCTION
def load():
    try:
        with open('database.csv', 'r') as archive:
            lines = archive.readlines()
            for line in lines:
                details = line.strip().split(',')

                name = details[0]
                phone = details[1]
                email = details[2]
                address = details[3]

                AGENDA[name] = {
                    'phone': telefone,
                    'email': email,
                    'address': address,
                }
        print('>>>> Database loaded with success!')
        print('>>>> {} contacts carregados'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>>> archive not found')
    except Exception as error:
        print('>>>> Unexpected error occurred')
        print(error)

# SHOW MENU FUNCTION
def show_menu():
    print('------------------------------------------')
    print('1 - Show all contacts')
    print('2 - Search contact')
    print('3 - Add contact')
    print('4 - Edit contact')
    print('5 - Delete contact')
    print('6 - Export contacts to CSV')
    print('7 - Import contacts from CSV')
    print('0 - Exit agenda')
    print('------------------------------------------')


# INSTRUCTIONS
load()
while True:
    show_menu()

    option = input('Choose an option below: ')
    if option == '1':
        show_contact()
    elif option == '2':
        contact = input('Enter contact name: ')
        get_contact(contact)
    elif option == '3':
        contact = input('Enter contact name: ')

        try:
            AGENDA[contact]
            print('>>>> Contact already exist')
        except KeyError:
            telefone, email, endereco = read_detail_contact()
            includ_edit_contact(contact, telefone, email, endereco)
    elif option == '4':
        contact = input('Enter contact name: ')

        try:
            AGENDA[contact]
            print('>>>> Edit contact:', contact)
            telefone, email, endereco = read_detail_contact()
            includ_edit_contact(contact, telefone, email, endereco)
        except KeyError:
            print('>>>> Contact does not exist')

    elif option == '5':
        contact = input('Enter contact name: ')
        delete_contact(contact)
    elif option == '6':
        archive_name = input('Enter archive name to be exported: ')
        export_contact(archive_name)
    elif option == '7':
        archive_name = input('Enter archive name to be imported: ')
        import_contact(archive_name)
    elif option == '0':
        print('>>>> Farewell!!!')
        break
    else:
        print('>>>> Invalid option!')

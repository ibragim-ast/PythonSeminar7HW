
def add_contact():
    name = input('Введите имя: ')
    firstname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    directory = name + ' ' + firstname + '||' + phone + '\n'
    return directory


def find_contact(f):
        a = input('Введите данные для поиска: ')
        fnd = list(filter(lambda x: a in x, f.split('\n')))
        return fnd
        

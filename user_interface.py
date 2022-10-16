from model import add_contact, find_contact
from logger import write_contact, read_contact

print('Выберите режим работы со справочником: ')
print('1. Записать нового абонента\n2. Поиск по справочнику \n3. Вывести справочник на экран')
mode = int(input())
if mode == 1:
    a = add_contact()
    write_contact(a)

elif mode == 2:
    print(find_contact(read_contact()))

elif mode == 3:
    print(read_contact())

else: 
    print('Введено неверное значение!')

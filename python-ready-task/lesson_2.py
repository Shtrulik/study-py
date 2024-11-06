'''
integer = 3
string = '3'
float = 3.0
bool = True
list = [1, 2, 3]
dict = {"age":30, "year":1994}
tuple = ("year", -1, 3.0)
NonE = None

prac = integer == float
prac_str = string == integer
prac_int = integer + int(string)

print(prac_int)
print(prac_str)
print("year" in dict or tuple)
print("y" in tuple and tuple[2] >= integer or NonE != bool)
print(dict["age"] == float)
'''

# Робота з рядками:
'''
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
string_num = str(num_str)
print(type(string_num))
#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити усі букви 'y' на '0' та 'i' на '1'. 
message = 'Hi, my name is Python!'
a = message.replace("y", "0")
b = a.replace("i", "1")
print(b)
#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за 
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
c = split_test.split()
string_join = "".join(c)
print(c)
print(string_join)
#  4. Визначити довжину рядку string_join за допомогою функції len()
print(len(string_join))
'''

# Робота зі списками:

'''
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)
#  2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)
#  3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
x = list_extend.index(6)
print(x)
#  4. Визначити довжину списку list_append за допомогою функції len()
x = len(list_append)
print(x)
'''

# Робота зі словниками:

'''
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'], dict_test['where'])
#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
key_words = dict_test.keys()
key_words_v = dict_test.values()
print(key_words)
print(key_words_v)
#  3. За допомогою функції items() вивести на екран пари ключ - значення
all_invo = dict_test.items()
print(all_invo)
'''
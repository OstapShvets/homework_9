####1 Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни.

# my_list = ['ostap', 'shv', 'hello', 'hillel']

# def transform_list(my_list):
#     new_list = []
#     for i in range(len(my_list)):
#         fin = my_list[i]
#         if i % 2 == 0:
#             new_list.append(fin)
#         else:
#             new_list.append(fin[::-1])
#     return new_list

# new_list = transform_list(my_list)
# print(new_list)

##### 2)Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".


# def filter_list(my_list):
#     return [x for x in my_list if x.startswith('a')]
# my_list = ['aostap', 'shv', 'hello', 'hillel']
# new_list = filter_list(my_list)
# print(new_list)


###3.Написати функцію яка приймає один параметр – список рядків my_list.
#Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.


# def filter_list(my_list):
#     return [elem for elem in my_list if 'a' in elem]
# my_list = ['ostap', 'shv', 'hello', 'hillel']
# filtered_list = filter_list(my_list)
# print(filtered_list)


###4 Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
#Функція повертає новий список у якому містяться лише рядки з my_list.

# def filter_strings(my_list):
#     return [elem for elem in my_list if isinstance(elem, str)]
#
# my_list = ['hello', 123, 'world', True, 'python', 3.14]
# new_list = filter_strings(my_list)
# print(new_list)


###5 Написати функцію яка приймає один параметр – рядок my_str.
#Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.


# def unique_chars(my_str):
#
#     all_chars = set(my_str)
#     unique_chars = []
#     for char in all_chars:
#         if my_str.count(char) == 1:
#             unique_chars.append(char)
#
#     return unique_chars
#
# my_str = "hello world"
# print(unique_chars(my_str))


###6 Написати функцію яка приймає один параметр - два рядки.
#Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.

# def common_chars(str1, str2):
#     set1 = set(str1)
#     set2 = set(str2)
#     common = set1.intersection(set2)
#
#     return list(common)
# s1 = "hello"
# s2 = "world"
# result = common_chars(s1, s2)
# print(result)

##7Написати функцію яка приймає два параметри - два рядки.
#Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.

# def common_chars(str1, str2):
#     set1 = set(str1)
#     set2 = set(str2)
#     common = set1.intersection(set2)
#     result = list(common)
#     return result
# str1 = 'hello'
# str2 = 'world'
# result = common_chars(str1, str2)
# print(result)

####8   Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
# "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.


import random

def create_email(domains, names):
    name = random.choice(names)
    domain = random.choice(domains)
    number = random.randint(100, 999)
    letter = random.choice(letters)
    return f"{name}.{number}@{letter}.{domain}"
names = ["oleg", "andriy", "ostap"]
letters = ["gmail", "ukr"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
print(e_mail)
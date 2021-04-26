# def square(value):
#     a = value ** 2
#     print(a)
#
# val = int(input("Please enter a number to get square of it: "))
# square(val)

# __________________________________________________________________________________________

# def subjectToWord(subject, arg):
#
#     print(arg.join(subject))
#
# subjects = ('math', 'english', 'russian')
# subjectToWord(subjects, ' & ')

# __________________________________________________________________________________________

# def smth(abs):
#     while abs:
#         print(abs.pop(-1))
#
# abs = ["kia", "toyota", 'bmw', "nissan"]
# smth(abs);

# __________________________________________________________________________________________

# def reverses(word):
#     print(word[::-1])
#
# reverses('kalla')

# __________________________________________________________________________________________

# def longestWord(words):
#     longest = max(words.split(), key=len)
#     longest_size = len(longest)
#     print(longest)
#     print(longest_size)
#
# wordss = input('Please enter words: ')
# longestWord(wordss)
# __________________________________________________________________________________________

# def absol_val(num):
#     if num > 0:
#         return num
#     else:
#         return -num
# print(absol_val(2))
# print(absol_val(-6))

# __________________________________________________________________________________________

# def itemInfo(item, price, quantity):
#     print(f'Do you really want to purchase {item}, for this {price}, at this {quantity}?')
#     ans = input('Please press "Y" for Yes, "N" for No.\nYour answer :')
#     if(ans.lower() == 'y'):
#         from random import randint
#         cost = randint(100, 1000)
#         print(f"Total cost is {cost}")
#     else:
#         print('You cancelled your purchase, thanks')
#
# item = input("Please enter item: ")
# price = input("Please enter its price: ")
# quantity = input("Please enter quantity: ")
#
# itemInfo(item, price, quantity)

# __________________________________________________________________________________________


# def getNamebyInd(ind):
#     asd = ['Bob', 'Tom', 'Ken', 'Lucas', 'Jim']
#     if ind < len(asd):
#         getName = asd[ind]
#         print(getName)
#     else:
#         print(f'You entered big number, please enter from 0 to {len(asd)}')
#
# index = int(input('Please enter index number: '))
# getNamebyInd(index)

# __________________________________________________________________________________________

# def farToCel(f):
#     c = (f - 32) * 5.0/9.0
#     print("Temperature:", f, "Fahrenheit = ", c, "C")
#     return c
#
# def celToFar(c):
#     f = c * 1.8 + 32
#     print("Temperature:", c, "Celcius = ", f, "F")
#     return f
#
# def temp():
#     num = int(input('Please choose: \n 1: Fahrenheit to Celcius\n 2: Celcius to Fahrenheit\nYour choise:'))
#     if num == 1:
#         Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
#         farToCel(Fahrenheit)
#     else:
#         Celcius = int(input("Enter celcius: "))
#         celToFar(Celcius)
# temp()

# # __________________________________________________________________________________________
#
# def toCapLetter(word):
#     cap = word.capitalize()
#     print(cap)
#
# toCapLetter('somsa')

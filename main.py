print("hoshi lodicakes")

print("o____/")
print("  l l l l")

print("hoshi\nlodicakes")
# the \n is for seperating words or phrase in a different line

print("\"Dino is kpop's future" + "\" ")
# \" is used when you want quotation marks to be literally in the string

print("seungkwan\sexy")

phrase = "Seungkwan Sexy"
print(phrase.lower())
print(phrase.upper())
# .lower() function will make the strings lower case while .upper() will make the strings upper case

svt_visual = "kim mingyu"
print(svt_visual.isupper())
# .isupper() function will check if the strings are in upper case while .islower() will check if the strings are in lower case, the answer will either be True or False. kim mingyu is written in lower case hence the answer for print(svt_visual.isupper()) is False.

print(svt_visual.upper().isupper())
# we converted kim mingyu into upper case hence the answer is True when we asked if it's .isupper()

print(len(svt_visual))
# len is a function that counts the numbers of characters in variable svt.visual (kim mingyu). There are total of 10 characters including the space.

print(svt_visual[9])
# square brackets [] can be used to know the equivalent string of an jndex number. indexes always start with 0 hence index 9 is the letter "u" in kim mingyu.

print(svt_visual.index("g"))
# .index is a function to know what is the equivalent index number of a string. hence g is at index 7

print(svt_visual.replace("kim", "CEO"))
# .replace is function that let's you replace a part of string. we replaced kim with "CEO" thats wht the console showed "CEO mingyu""

name_first = "hoshi kwon"
age = "25"
pronoun = "he"
is_male = True
is_woman = False
print(name_first + " is " + age + " years old")
print(pronoun + " is a seventeen member")
print(is_woman)

name_scnd = "seungcheol"
position = "leader"
is_male = True
print(name_scnd + " is one of the best " + position + " in kpop industry")
print(pronoun + " is responsible and trustworthy")
print(is_male)

print(2*7) # multiplication
print(3+4) # addition
print(6/3) # division
print(4-2) # subtraction  
print(10%3) # remainder
print(5+7*2) # operation
print((5+7)*2) # parenthesis is used to specify order of operation

num = -5
print(str(num) + " is not my fave number")
print(abs(num))
print(pow(2, 2))
# str function can convert numbers into strings
# abs function can make the number absolute and positive
# pow function means "in the power of"

print(max(2, 8, 6))
print(min(2, 7, 3))
# max function finds the highest number in a string
# min function finds the lowest number in a string

print(round(5.7))
# round function rounds off decimal numbers. hence the result in the console is 6

from math import *
# we are using this to import other external python functions

print(floor(5.3))
# floor function chops off decimal points and grabs the whole number

print(ceil(7.8))
# ceil function rounds off decimal values

print(sqrt(100))
# sqrt function means "square root of"

bias = input("Who's your bias in Seventeen?"  )
print("I see that " + bias + " is your favorite member. What a coincidence! I like him too!")

name = input("enter your name: ")
print(name + "'s bias in Seventeen was " + bias + '.')

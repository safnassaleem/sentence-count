# 
# 1) Write a function to find the number of sentences in a
#    string. e.g. it should return 5 for 'I am a programmer. What do I
#    do? I program. Which language do I program in? Why, Python of
#    course!'

def sentence_count():
    word=0
    string="I am a programmer. What do I do? I program. Which language do I program in? Why, Python ofcourse!"
    characters= ['.','?','!']
    for i in characters:
        for j in string:
            if i in j:
                word=word+1
    print("sentence=",word)
sentence_count()

# By using regular Expression

import numbers
import re
def sentence():

    string="I am a programmer. What do I do? I program. Which language do I program in? Why, Python ofcourse!"
    characters= re.split(r'\.\s|\?\s', string)
    print(characters)
    print(len(characters))
sentence()


# 2) a function to return the number of words in a sentence.


def word_count():
    string="I am a programmer. What do I do? I program. Which language do I program in? Why, Python ofcourse!"
    print(len(string.split(" ")))

word_count()


# Write a function that will return the most frequently occurring number
# in a list of numbers. 
# Write a function that will return the most frequently occurring 2 numbers
#    in a list of numbers. 


list=[5,8,9,6,5,5,7]
def repeat():
    count=0
    temp=0
    for i in range(0,len(list)):
        temp=list.count(list[i])
        if(temp>count):
            count=temp
            number=i
            
    mostfrequentnumber=list[number]
    print('frequent number is {} '.format(mostfrequentnumber))

repeat()
#

# Write a function that will remove everything except strings in a
# given list.


def exceptstring():

    list1=['aaa',4,6,'hkjkj']

    result=list(filter(lambda x: type(x)==str,list1))
    print(result)
exceptstring()


# Write a function that will return the most frequently occurring 2 numbers
#    in a list of numbers. 

from collections import Counter
def mostoccuring(numbers):
    counter=Counter(numbers)
    numbers=counter.most_common(2)
    print(numbers)  
number=[2,1,4,8,7,4,5,4,4,2]

mostoccuring(number)



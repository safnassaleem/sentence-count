# import string


# def wordcount(string):
#     return len(string.split(' '))
# print(wordcount("i am programer"))

def sentence_count(string):
    dot=string.count(".")
    questionmark=string.count("?")
    exclamatory=string.count("!")
    count=dot+questionmark+exclamatory
    return(count)
print(sentence_count("wow! i cant't believe we wom! it was nice.is there is any issue?"))
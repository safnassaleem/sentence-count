import string


def wordcount(string):
    return len(string.split(' '))
print(wordcount("i am programer"))

def sentence_count(string):
    dot=string.count(".")
    questionmark=string.count("?")
    comma=string.count(",")
    count=dot+questionmark+comma
    return(count)
print(sentence_count("iam a officer,working at? its good,to see."))
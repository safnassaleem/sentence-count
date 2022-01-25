
def sentence_count():
    word=0
    x="I am a programmer. What do I do? I program. Which language do I program in? Why, Python ofcourse!"
    a = ['.','?','!']
    for i in a:
        for j in x:
            if i in j:
                word=word+1
    print("sentence=",word)
sentence_count()



def word_count():
    x="I am a programmer. What do I do? I program. Which language do I program in? Why, Python ofcourse!"
    print(len(x.split(" ")))

word_count()
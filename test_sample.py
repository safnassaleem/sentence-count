import sample
def test_wordcount():
    assert sample.wordcount("i am programmer")==3

def test_sentencecount():
    assert sample.sentence_count("wow! i cant't believe we wom! it was nice.is there is any issue?")==4
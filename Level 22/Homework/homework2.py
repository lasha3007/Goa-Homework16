def hashtag_generator(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    hashtag = '#' + ''.join(capitalized_words)
    return hashtag

print(hashtag_generator("abc def ghi"))  # Output: #AbcDefGhi

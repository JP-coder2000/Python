def is_anagram(word1,word2):
    word1 = word1.lower()
    word2 = word2.lower()

    letters_word1 = []
    letters_word2 = []

    #this is one way to convert a word to a list of elements
    for letter1 in word1:
        letters_word1.append(letter1)

    for letter2 in word2:
        letters_word2.append(letter2)

    #Here´s the other way
    #letters_word1 = list(word1)
    #letters_word2 = list(word2)
    
    letters_word1.sort()
    letters_word2.sort()

    if letters_word1 == letters_word2:
        return True
    else:
        return False

print(is_anagram("restful", "fluster"))
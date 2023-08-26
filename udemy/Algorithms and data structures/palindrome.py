def palindrome(word):
    word = word.lower()
    # creating a list with the letters of the word
    letters = []
    for letter in word:
        letters.append(letter)

    # points to the first and the last element of the list
    letters_one = 0
    letters_final = len(letters)-1

    # cheking if they are the same

    while letters_final > letters_one:
        if letters[letters_one] != letters[letters_final]:
            return False  # No es un palíndromo
        letters_one = letters_one + 1
        letters_final = letters_final - 1
    return True  # Es un palíndromo


print(palindrome("radar"))

def palindrome_python(word):
    word = word.lower()
    #Here we are reversing the word
    #this is called slicing
    #here are more examples of slicing:
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False
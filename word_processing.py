"""
Beginning of psychological trauma
"""

# text = open("words.txt", "r")
# print(text.read())
file = open("words.txt", "r")


def get_words(file):
    words = file.read().split()
    return words


print(type(get_words(file)))


def cleaning_words(words):
    """
    function lowers all words
    args:: words list
    returns:: lowers words ready from processing
    """
    words_lowercase = [word.lower() for word in words]
    return words_lowercase


def get_userinput():
    """
    take user input then filters by making sure its alphabet
    """
    user_input = input("search for word: ")
    while not user_input or not user_input.isalpha():
        user_input = input("search for word (enter a valid word): ")
    return user_input


def user_word_split(words):
    """
    if the user enters a space we assume the word is complete
    args:: words list

    returns the list of words
    """
    ...


def user_word_count_sort(words):
    """
    sorts the list based on most typed words
    args:: words list

    returns the sorted list of most used words
    """
    return {words.count(word): word for word in words}


def main():
    words = get_words()
    while True:
        user = get_userinput()

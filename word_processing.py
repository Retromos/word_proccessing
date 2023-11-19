"""
Beginning of psychological trauma
"""


def get_words(file):
    """
    function returns a list of all words from the read txt file
    args:: file - file directo
    returns:: a list of words...
    """
    f = open("words.txt", "r")
    words = f.read()
    f.close()
    return words


def cleaning_words(words):
    """
    function lowers all words
    args:: words list
    returns:: lowers words ready from processing
    """


def get_userinput():
    """
    take user input then filters by making sure its alphabet
    """
    ...


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
    ...

"""
Beginning of psychological trauma
"""


def get_words(file):
    with open(file) as f:
        return f.readlines()



def show_filtered_words(user_input,words_list):
    return  [list_word for list_word in words_list if list_word.startswith(user_input)]




def word_recursion( word_list,user_input=''):
    if user_input == 'exit' or word_list == []:
        return word_list
    user_input = get_userinput()
    word_list = show_filtered_words(user_input,word_list)
    print(word_list)

    word_recursion(user_input,word_list)




def cleaning_words(words):
    """
    function lowers all words
    args:: words list
    returns:: lowers words ready from processing
    """
    words_lowercase = [word.replace('\n','').lower() for word in words]
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
    words = cleaning_words(get_words('words.txt'))
    while True:
        user = get_userinput()
        words = show_filtered_words(user, words)
        print(words)




if __name__ == '__main__':
    main()
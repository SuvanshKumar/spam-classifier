import os
import re

'''
This function reads the stop-words from a text file, and returns them as a list of strings
'''
def read_stop_words(file_path = 'data/stopwords.txt'):
    with open(file_path) as f:
        stop_words = [word[:-1] for word in f]
    return stop_words

'''
Function to remove all punctuation from a string except the apostrophe sign 
(e.g.It is that boy's pen -- boy's will remain boy's and not change)
'''
def remove_punctuations(text: str) -> str:
    text = text.replace('\n', ' ')
    text = re.sub(r'[^A-Za-z\' ]+', '', text)
    return text

'''
runs os.walk and returns the relative paths of all the files of training data, as a tuple of 2 elements
each element of the tuple is a list (the first list for spams and second one for hams)
both of these contain strings which are relative paths of file names from the root of the project
e.g. (['data/train/spam/file1.txt', 'data/train/spam/file2.txt'], ['data/train/ham/file1.txt'])
'''
def get_file_paths():
    spam_train_dir = 'data/train/spam/'
    ham_train_dir = 'data/train/ham/'
    for file_paths in os.walk(spam_train_dir):
        spam_file_paths = [spam_train_dir + spam_file_name for spam_file_name in file_paths[2]]
    for file_paths in os.walk(ham_train_dir):
        ham_file_paths = [ham_train_dir + ham_file_name for ham_file_name in file_paths[2]]
    return (spam_file_paths, ham_file_paths)

'''
Input: the list of file paths (relative path from root of project should work), and the list of stop words
Output: returns the tokens, which is the list of all the words (excluding punctuation, numbers but including apostrophes) occurring in all the files in the file_paths list
'''
def get_words_list(file_paths, stop_words):
    tokens = []
    for file_path in file_paths:
        tokens_this_file = []
        with open(file_path, encoding='latin-1') as f:
            text = f.read()
        text = remove_punctuations(text)
        split_list = text.split(' ')
        tokens_this_file = [token for token in split_list if token != '' and not token.isnumeric() and token not in stop_words]  
        tokens.extend(tokens_this_file)
    return tokens

def main():
    stop_words = read_stop_words()
    spam_file_paths, ham_file_paths = get_file_paths()
    spam_words_list = get_words_list(spam_file_paths, stop_words)
    ham_words_list = get_words_list(ham_file_paths, stop_words)

if __name__ == '__main__':
    main()

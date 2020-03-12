import os
import re

def read_stop_words(file_path = 'data/stopwords.txt'):
    with open(file_path) as f:
        stop_words = [word[:-1] for word in f]
    return stop_words

def remove_punctuations(text: str) -> str:
    text = text.replace('\n', ' ')
    text = re.sub(r'[^A-Za-z\' ]+', '', text)
    return text

def get_file_paths():
    spam_train_dir = 'data/train/spam/'
    ham_train_dir = 'data/train/ham/'
    spam_file_paths, ham_file_paths = [], []
    for file_paths in os.walk(spam_train_dir):
        spam_file_paths = [spam_train_dir + spam_file_name for spam_file_name in file_paths[2]]
    for file_paths in os.walk(ham_train_dir):
        ham_file_paths = [ham_train_dir + ham_file_name for ham_file_name in file_paths[2]]
    return (spam_file_paths, ham_file_paths)

def get_words_list(file_paths, stop_words):
    tokens = []
    for file_path in file_paths:
        tokens_this_file = []
        with open(file_path, encoding='latin-1') as f:
            text = f.read()
        text = remove_punctuations(text)
        split_list = text.split(' ')
        # print(split_list)
        tokens_this_file = [token for token in split_list if token != '' and not token.isnumeric() and token not in stop_words]  
        tokens.extend(tokens_this_file)
    return tokens


def main():
    stop_words = read_stop_words()
    spam_file_paths, ham_file_paths = get_file_paths()
    print(spam_file_paths[:10])
    print(ham_file_paths[:10])
    spam_words_list = get_words_list(spam_file_paths, stop_words)
    ham_words_list = get_words_list(ham_file_paths, stop_words)
    print(len(spam_words_list))
    print(len(ham_words_list))

if __name__ == '__main__':
    main()

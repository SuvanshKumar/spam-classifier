import os
import re

from naive_bayes_classifier import NaiveBayes

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
runs os.walk and returns the relative paths of all the files of training data, as a tuple of 4 elements
each element of the tuple is a list (the first list for spams and second one for hams)
all four of these contain strings which are relative paths of file names from the root of the project
e.g. (['data/train/spam/file1.txt', 'data/train/spam/file2.txt'], ['data/train/ham/file1.txt'], [], [])
'''
def get_file_paths():
    spam_train_dir = 'data/train/spam/'
    ham_train_dir = 'data/train/ham/'
    spam_test_dir = 'data/test/spam/'
    ham_test_dir = 'data/test/ham/'
    for file_paths in os.walk(spam_train_dir):
        spam_train_file_paths = [spam_train_dir + spam_file_name for spam_file_name in file_paths[2]]
    for file_paths in os.walk(ham_train_dir):
        ham_train_file_paths = [ham_train_dir + ham_file_name for ham_file_name in file_paths[2]]
    for file_paths in os.walk(spam_test_dir):
        spam_test_file_paths = [spam_test_dir + spam_file_name for spam_file_name in file_paths[2]]
    for file_paths in os.walk(ham_test_dir):
        ham_test_file_paths = [ham_test_dir + ham_file_name for ham_file_name in file_paths[2]]
    return (spam_train_file_paths, ham_train_file_paths, spam_test_file_paths, ham_test_file_paths)

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
        tokens_this_file = [token.lower() for token in split_list if token != '' and not token.isnumeric() and token.lower() not in stop_words]  
        tokens.extend(tokens_this_file)
    return tokens

def naive_bayes_classify(spam_words_list, ham_words_list, spam_test_file_paths, ham_test_file_paths, spam_file_count, ham_file_count, stop_words):
    bayes_classifier = NaiveBayes(spam_words_list, ham_words_list, spam_file_count, ham_file_count)
    ham_f_paths = ham_test_file_paths
    spam_f_paths = spam_test_file_paths
    correct_classifications, wrong_classifications = 0, 0
    for f1_path in spam_f_paths:
        tokens_test = get_words_list((f1_path, ), stop_words)
        result = bayes_classifier.classify(tokens_test)
        if result == 'spam':
            correct_classifications += 1
        else:
            wrong_classifications += 1
    for f1_path in ham_f_paths:
        tokens_test = get_words_list((f1_path, ), stop_words)
        result = bayes_classifier.classify(tokens_test)
        if result == 'ham':
            correct_classifications += 1
        else:
            wrong_classifications += 1
    return (correct_classifications, wrong_classifications)

def main():
    stop_words = read_stop_words()
    spam_train_file_paths, ham_train_file_paths, spam_test_file_paths, ham_test_file_paths = get_file_paths()
    spam_file_count, ham_file_count = (len(spam_train_file_paths), len(ham_train_file_paths))
    spam_words_list = get_words_list(spam_train_file_paths, stop_words)
    ham_words_list = get_words_list(ham_train_file_paths, stop_words)

    # Without removing the stop words, the list will be different
    # Spam words list including stop words
    spam_words_list_incl_sw = get_words_list(spam_train_file_paths, stop_words=[])
    # Ham words list including stop words
    ham_words_list_incl_sw = get_words_list(ham_train_file_paths, stop_words=[])

    # Using the Naive Baye's classifier
    print('Naive Baye\'s classifier:')
    
    # Without stop words
    correct_classifications1, wrong_classifications1 = naive_bayes_classify(spam_words_list_incl_sw, ham_words_list_incl_sw, spam_test_file_paths, ham_test_file_paths, spam_file_count, ham_file_count, stop_words=[])
    print('Including stop words, the accuracy is:', (correct_classifications1)/(correct_classifications1+wrong_classifications1) )
    
    # With stop words
    correct_classifications2, wrong_classifications2 = naive_bayes_classify(spam_words_list, ham_words_list, spam_test_file_paths, ham_test_file_paths, spam_file_count, ham_file_count, stop_words)
    print('After removing stop words, the accuracy is:', (correct_classifications2)/(correct_classifications2+wrong_classifications2) )
    
if __name__ == '__main__':
    main()

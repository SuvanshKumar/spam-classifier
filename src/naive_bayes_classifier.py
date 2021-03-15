import math
import collections

class NaiveBayes:

    classes = ['spam', 'ham']
    # Word Lists
    spam_list = []
    ham_list = []
    spam_file_count = 0
    ham_file_count = 0

    def __init__(self, spam_list, ham_list, spam_file_count, ham_file_count):
        self.spam_list = spam_list
        self.ham_list = ham_list
        self.spam_file_count = spam_file_count
        self.ham_file_count = ham_file_count
        self.vocabulary = set(spam_list).union(set(ham_list))
        self.spam_counter = collections.Counter(spam_list)
        self.ham_counter = collections.Counter(ham_list)

    def classify(self, test_file_word_list):
        '''
        it tests the testing data
        log P(spam | test_file) proportional to --> log P(spam) + log P(word1|spam) + log P(word2|spam) + ... + log P (wordn|spam)
        log P(spam) = len spam / (len spam + len ham)
        log P(word i | spam) = log ( ( (count of word i) + 1 ) / ( (count of all words in both lists including duplicates) + len vocabulary ) )
        denominator = (count of all words in both lists including duplicates) + len vocabulary --> is same for all terms except first term which is log P(spam)
        '''
        log_prob_spam = math.log(len(self.spam_list)/(len(self.spam_list)+len(self.ham_list)))
        denominator = len(self.spam_list) + len(self.vocabulary)
        for word in test_file_word_list:
            numerator = self.spam_counter.get(word.lower(), 0) + 1
            log_prob_spam += math.log(numerator/denominator)

        log_prob_ham = math.log(len(self.ham_list)/(len(self.spam_list)+len(self.ham_list)))
        denominator = len(self.ham_list) + len(self.vocabulary)
        for word in test_file_word_list:
            numerator = self.ham_counter.get(word.lower(), 0) + 1
            log_prob_ham += math.log(numerator/denominator)

        if log_prob_spam > log_prob_ham:
            return self.classes[0]
        else:
            return self.classes[1]
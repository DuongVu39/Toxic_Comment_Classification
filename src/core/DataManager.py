# Utility Libraries
import time

# Data libraries
import pandas as pd
import numpy as np

# NLP Libraries
import nltk
from nltk import tokenize

# Self imports
from src import logging_wrapper


class DataManager(object):

    def __init__(self, path, logging_level=3, logging_path="logs/data_manager{}.txt".format(time.time()), train_only=False):
        self.train = pd.read_csv(path + "/train.csv")
        self.test = pd.read_csv(path + "/train.csv") if not train_only else False
        self.id_dict = self.dat[['id', 'comment_text']].set_index('id').to_dict()
        self.logger = logging_wrapper(logging_level, logging_path)

    def tokenize(self):
        self.logger.info("Tokenizing training input")
        st = time.time()
        self.train['tokenized'] = self.train['comment_text'].apply(tokenize.word_tokenize)
        self.logger.info("Tokenizing all training documents took {}s".format(time.time() - st))

        if self.test:
            self.logger.info("Tokenizing test input")
            st = time.time()
            self.test['tokenized'] = self.test['comment_text'].apply(tokenize.word_tokenize)
            self.logger.info("Tokenizing all test documents took {}s".format(time.time() - st))



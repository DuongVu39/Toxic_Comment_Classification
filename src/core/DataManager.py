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
        self.test = False if train_only else pd.read_csv(path + "/train.csv")  # For some if checks down the road.
        self.train_id_dict = self.train[['id', 'comment_text']].set_index('id').to_dict()
        self.test_id_dict = self.test[['id', 'comment_text']].set_index('id').to_dict()
        self.logger = logging_wrapper(logging_level, logging_path)

    def tokenize(self):
        self.logger.info("Tokenizing training input")
        st = time.time()
        self.train['tokenized'] = self.train['comment_text'].apply(tokenize.word_tokenize)
        self.logger.info("Tokenizing all training documents took {}s".format(time.time() - st))

        if isinstance(self.test, pd.DataFrame):
            self.logger.info("Tokenizing test input")
            st = time.time()
            self.test['tokenized'] = self.test['comment_text'].apply(tokenize.word_tokenize)
            self.logger.info("Tokenizing all test documents took {}s".format(time.time() - st))
        else:
            self.logger.info("Train only mode is enabled, exiting function.")


    def _pad_sentences(self):
        self.train

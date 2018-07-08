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

    def __init__(self, loc, logging_level=3, logging_path="logs/data_manager{}".format(time.time())):
        self.dat = pd.read_csv(loc)
        self.id_dict = self.dat[['id', 'comment_text']].set_index('id').to_dict()
        self.logger = logging_wrapper()

    def tokenize(self):
        self.dat['tokenized'] = self.dat['comment_text'].apply(tokenize.word_tokenize)


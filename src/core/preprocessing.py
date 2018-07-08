# Util libraries
import re
import string
import logging

# Data libraries:

# NLP libraries
from nltk.corpus import stopwords


def replace_number(tokenized_list, logger=None):  # Tested [Y]
    """
    Delete all number after tokenize
    Args:
        tokenized_list(list): A list of tokenized word
        logger (Logger)     : Logger object from the Logging package which has already been configured. If None, no logging
                             is performed.

    Returns:
        The tokenized list that does not contain any number but instead only special character
    """
    digits = r"\d+"

    for i in range(len(tokenized_list)):
        if str(tokenized_list[i]).isdigit():  # Branch A
            tokenized_list.pop(i)

        # handle digit attaches to a string
        if len(re.split(digits, tokenized_list[i])) != 1:  # Branch B
            tokenized_list[i] = re.findall(r"\w+", re.sub('\d+', '', tokenized_list[i]))[0]

    return tokenized_list


def combine_contractions(sentence, logger=None):
    len_before = len(sentence)
    for index in range(len_before):
        if sentence[index] in ["n't", "'m", "'ll"]:
            sentence[index - 1] += sentence[index]
            sentence.pop(index)
    if logger:
        logger.info("Combining contractions. Length of document before: {}. "
                "Length of document after: {}".format(len_before, len(sentence)))

    return sentence


def preprocess_tokens(sentence,
                      remove_stop_words=True,
                      remove_punctuation=True, tag_numbers=True, lower_case=True,
                      stop_words_list=stopwords.words('english'), logger=None):
    """
    Performs additional preprocessing steps on the already tokenized documents.

    Args:
        sentence (list): A list of strings where elements are the tokens from your document.
        remove_stop_words (bool):
        remove_punctuation (bool):
        tag_numbers (bool):
        lower_case (bool):
        stop_words_list (bool):
        logger (Logger):

    Returns:

    """
    sentence = combine_contractions(sentence, logger=logger)

    if lower_case:
        if logger:
            logger.info("Turning all tokens to lower-case")
        sentence = [i.lower() for i in sentence]

    if remove_stop_words:
        len_before = len(sentence)
        sentence = [i for i in sentence if i not in stop_words_list]
        if logger:
            logger.info("Removed stopwords. Length of document before: {}. Length of document after: {}".format(len_before, len(sentence)))

    if remove_punctuation:
        len_before = len(sentence)
        sentence = [i for i in sentence if i not in ['...'] + list(string.punctuation)]
        if logger:
            logger.info("Removed punctuation. Length of document before: {}. Length of document after: {}".format(len_before, len(sentence)))

    if tag_numbers:
        len_before = len(sentence)
        sentence = replace_number(sentence)
        if logger:
            logger.info("Converting numbers to a tag. Length of document before: {}. "
                        "Length of document after: {}".format(len_before, len(sentence)))

    return sentence


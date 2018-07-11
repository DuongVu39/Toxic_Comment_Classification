# Util libraries
import re
import string
import logging

# Data libraries:

# NLP libraries
from nltk.corpus import stopwords


def replace_number(sentence, logger=None):  # Tested [Y]
    """
    Delete all number after tokenize
    Args:
        sentence(list)  : A list of tokenized word
        logger (Logger) : Logger object from the Logging package which has already been configured. If None, no logging
                             is performed.

    Returns:
        The tokenized list that does not contain any number but instead only special character
    """
    digits = r"\d+"

    for i in range(len(sentence)):
        if str(sentence[i]).isdigit():  # Branch A
            sentence.pop(i)

        # handle digit attaches to a string
        if len(re.split(digits, sentence[i])) != 1:  # Branch B
            sentence[i] = re.findall(r"\w+", re.sub('\d+', '', sentence[i]))[0]

    return sentence


def combine_contractions(sentence, logger=None):
    """

    Args:
        sentence:
        logger:

    Returns:

    """
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
                      remove_punctuation=False, tag_numbers=True, lower_case=True,
                      stop_words_list=stopwords.words('english'), logger=None):
    """
    Performs additional preprocessing steps on the already tokenized documents.

    Args:
        sentence (list): A list of strings where elements are the tokens from your document.
        remove_stop_words (bool):
        remove_punctuation (bool): Choose to remove punctuation or not. It seems like people with aggressive comment would use a lot more punctuation.
        tag_numbers (bool):
        lower_case (bool):
        stop_words_list (bool):
        logger (Logger):

    Returns:
        Tokenized documents after preprocessing

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

def padding(corpus, logger=None):
    """
    Performs padding on the already tokenized documents

    Args:
        corpus (list): A list of strings where elements are the tokens from your document.
        logger (Logger):

    Returns:
        A list of strings where elements are all at equal length

    """

    new_list = sorted(corpus, key=len)
    max_length = len(new_list[-1])
    for i in corpus:
        i.extend(("<PAD>",) * (max_length - len(i)))

    return corpus


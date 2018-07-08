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
            tokenized_list[i] = re.sub('\d+', '', tokenized_list[i])

    return tokenized_list


def preprocess_tokens(sentence,
                     remove_stop_words=True,
                     remove_punctuation=True, tag_numbers=False, lower_case=True,
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

   if lower_case:

       logger.info("Turning all tokens to lower-case")
       sentence = [i.lower for i in sentence]


   if remove_stop_words:

       len_before = len(sentence)
       sentence = [i for i in sentence if i not in stop_words_list]
       logger.info("Removed stopwords. Length of document before: {}. Length of document after: {}".format(len_before, len(sentence)))

   if remove_punctuation:

       len_before = len(sentence)
       sentence = [i for i in sentence if i not in ['...'] + list(string.punctuation)]
       logger.info("Removed punctuation. Length of document before: {}. Length of document after: {}".format(len_before, len(sentence)))

   if tag_numbers:
       sentence = replace_number(sentence)
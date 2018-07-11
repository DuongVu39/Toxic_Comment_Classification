from gensim.models import FastText, Word2Vec

def general_embed(sentence, model):
    """

    Args:
        sentence (list):
        model (gensim.model):

    Returns:

    """
    new_sentence = [model[i] for i in sentence]
    return new_sentence


def create_wtv(corpus, epochs=5):
    """

    Args:
        corpus:
        epochs:

    Returns:

    """
    wtv = Word2Vec(corpus)
    wtv.train(corpus, total_examples=corpus.shape[0], epochs=epochs)
    return wtv


def embed_to_wtv(corpus, epochs=5):
    """

    Args:
        corpus:
        epochs:

    Returns:

    """
    wtv = create_wtv(corpus, epochs=epochs)
    result = corpus.apply(general_embed, args=(wtv,))
    return result

def embed_to_ft():
    """"




    """
    pass




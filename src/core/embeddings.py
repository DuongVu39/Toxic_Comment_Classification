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
    wtv = Word2Vec(corpus)
    wtv.train(corpus, total_examples=corpus.shape[0], epochs=epochs)
    return wtv

def embed_to_wtv(corpus, epochs=5):
    wtv = create_wtv(corpus, epochs=epochs)
    corpus.apply(general_embed, args=(wtv,))

def embed_to_ft():
    pass




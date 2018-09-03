import numpy as np
from lib.singleton import Singleton
import pickle
from chatbot_ner.config import EMBEDDINGS_PATH_VOCAB, EMBEDDINGS_PATH_VECTORS


class LoadWordEmbeddings(object):

    __metaclass__ = Singleton

    def __init__(self):
        self.vocab, self.word_vectors = LoadWordEmbeddings.load_word_vectors_local()

    @staticmethod
    def load_word_vectors_local():
        """
        Thus function is used to load the word_list and word_vectors from the specified paths.
        Returns:
        vocab (list): word_list present at the specified path.
        word_vectors (numpy.ndarray): word_vectors present at the specified path.
        """
        file_handler = open(EMBEDDINGS_PATH_VOCAB, 'rb')
        vocab = pickle.load(file_handler)
        file_handler = open(EMBEDDINGS_PATH_VECTORS, 'rb')
        word_vectors = np.array(pickle.load(file_handler))
        return vocab, word_vectors

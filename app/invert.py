# import pandas as pd
import nltk


class Invert:

    @staticmethod
    def stem_list(string=str):
        """Transform str to stemmed list"""
        splitter = string.split()
        porter = nltk.PorterStemmer()

        listed = [porter.stem(word) for word in splitter]

        return listed

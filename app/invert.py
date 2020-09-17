import pandas as pd
import nltk


class Invert:

    @staticmethod
    def stem_list(string=str):
        """Transform str to stemmed list"""
        splitter = string.split()
        porter = nltk.PorterStemmer()

        listed = [porter.stem(word) for word in splitter]

        return listed

    @staticmethod
    def terms_series(series):
        """Test transform of series of lists into a series of unique terms"""
        series_list = list(series)
        flatlist = [item for sublist in series_list for item in sublist]
        flatlist = list(set(flatlist))
        final_series = pd.Series(flatlist).sort_values().reset_index(drop=True)

        return final_series

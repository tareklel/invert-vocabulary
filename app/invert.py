import pandas as pd
import nltk


class Invert:

    @staticmethod
    def stem_list(string: str):
        """Transform str to stemmed list"""
        splitter = string.split()
        porter = nltk.PorterStemmer()

        listed = [porter.stem(word) for word in splitter]

        return listed

    @staticmethod
    def terms_series(series: pd.Series):
        """transforms series of lists into a series of unique terms"""
        series_list = list(series)

        flatlist = [item for sublist in series_list for item in sublist]
        flatlist = list(set(flatlist))
        final_series = pd.Series(flatlist).sort_values().reset_index(drop=True)

        return final_series

    @staticmethod
    def create_inverse(terms: pd.Series, listseries: pd.Series):
        """uses series to create inverted DataFrame"""
        df = terms.to_frame("term")
        diction = listseries.to_dict()
        # creates list of indexes in which term has appeared for each row
        df["indexes"] = df["term"].apply(lambda x:
                                         [key for key, value in
                                          diction.items() if x in value])

        df["frequency"] = df["indexes"].apply(lambda x: len(x))

        return df






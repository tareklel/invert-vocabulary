import pandas as pd
from pandas.util.testing import assert_series_equal

import numpy as np

import unittest

from app.invert import Invert


class InverseTableTests(unittest.TestCase):

    def setUp(self):
        """Sets things up before test. Creates pandas table"""
        self.table = pd.DataFrame(np.array([['I ate a computer',
                                             'I eat computing books',
                                             'Computation is fun'],
                                            [4, 5, 6],
                                            [4, 8, 9]]),
                                  columns=['a', 'b', 'c'])

        self.series = pd.Series([['dog', 'cat', 'bird'],
                                ['dog', 'ogre'],
                                ['ogre', 'dog']])

    def test_stems_list(self):
        """Tests if string is transformed into list of stems"""
        string = self.table.loc[0, "a"]
        stems = Invert.stem_list(string)
        self.assertEqual(stems, ['I', 'ate', 'a', 'comput'])

    def test_terms_series(self):
        """Test transform of series of lists into a series of unique terms"""
        series = Invert.terms_series(self.series)
        series_test = pd.Series(['bird', 'cat', 'dog', 'ogre'])
        assert_series_equal(series, series_test)


if __name__ == '__main__':
    unittest.main()

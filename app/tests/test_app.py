import pandas as pd
from pandas.util.testing import assert_series_equal, assert_frame_equal

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

        self.testTable = pd.DataFrame({'term': ['bird', 'cat',
                                                'dog', 'ogre'],
                                       'indexes': [[0], [0],
                                                   [0, 1, 2], [1, 2]],
                                       'frequency': [1, 1, 3, 2]
                                       })

        self.seriesTest = pd.Series(['bird', 'cat', 'dog', 'ogre'])

    def test_stems_list(self):
        """Tests if string is transformed into list of stems"""
        string = self.table.loc[0, "a"]
        stems = Invert.stem_list(string)

        self.assertEqual(stems, ['I', 'ate', 'a', 'comput'])

    def test_terms_series(self):
        """Test transform of series of lists into a series of unique terms"""
        series = Invert.terms_series(self.series)

        assert_series_equal(series, self.seriesTest)

    def test_create_inverse(self):
        """Takes series and creates inverse table"""
        inverse = Invert.create_inverse(self.seriesTest, self.series)

        assert_frame_equal(inverse, self.testTable)


if __name__ == '__main__':
    unittest.main()

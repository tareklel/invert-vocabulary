import pandas as pd
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

    def test_stems_list(self):
        """Tests if string is transformed into list of stems"""
        string = self.table.loc[0, "a"]
        stems = Invert.stem_list(string)
        self.assertEqual(stems, ['I', 'ate', 'a', 'comput'])


if __name__ == '__main__':
    unittest.main()

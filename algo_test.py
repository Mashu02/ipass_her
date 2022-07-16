import unittest
from algo import cosine_sim_score
import pandas as pd
df = pd.read_csv('data_full_full.csv', sep=';')
df_list = df.values.tolist()

class TestData(unittest.TestCase):
    def test_data(self):
        result = cosine_sim_score([1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0], 1, (1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0), df_list)
        result2 = cosine_sim_score([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 1, (1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0), df_list)
        result3 = cosine_sim_score([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1], 1,(0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1), df_list)

        self.assertEqual(result, [0.8164965809277259])
        self.assertEqual(result2, [0.7071067811865475])
        self.assertEqual(result3, [0.8164965809277259])
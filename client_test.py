import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            expected_result = (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)
            self.assertEqual(getDataPoint(quote), expected_result)

    def test_getDataPoint_emptyQuote(self):
        # Test scenario with an empty quote
        quote = {}
        expected_result = ('', 0, 0, 0)
        self.assertEqual(getDataPoint(quote), expected_result)

    def test_getDataPoint_zeroPrices(self):
        # Test scenario with zero prices
        quote = {'top_ask': {'price': 0, 'size': 10}, 'timestamp': '2020-01-01 00:00:00', 'top_bid': {'price': 0, 'size': 15}, 'id': '12345', 'stock': 'XYZ'}
        expected_result = ('XYZ', 0, 0, 0)
        self.assertEqual(getDataPoint(quote), expected_result)

if __name__ == '__main__':
    unittest.main()

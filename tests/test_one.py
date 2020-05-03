from unittest import TestCase


class TestOne(TestCase):

    def test_sum(self):
        data = [1, 2, 3, 4]
        result = sum(data)
        self.assertEqual(result, 10)

    def test_string(self):
        data = ("Fabian", "Pepe", "Juan", "Pedro")
        self.assertIn("Pepe", data)


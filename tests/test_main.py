from unittest import TestCase

from main import calculate_distances


class Test(TestCase):
    def test_calculate_distances(self):
        tests_map = (
            {'count': 5, 'cells': [0, 1, 4, 9, 0], 'result': [0, 1, 2, 1, 0]},
            {'count': 7, 'cells': [0, 7, 9, 4, 4, 8, 20], 'result': [0, 1, 2, 3, 4, 5, 6]},
        )
        for case in tests_map:
            n, c, r = case.values()
            with self.subTest('test_calculate_distances'):
                self.assertEqual(r, calculate_distances(n, c))


if __name__ == '__main__':
    Test.run()


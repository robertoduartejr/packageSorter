from package_sorter import sort, PackageType
import unittest

class TestSortFunction(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(50, 50, 50, 10), PackageType.STANDARD.value)

    def test_special_bulky(self):
        self.assertEqual(sort(150, 30, 30, 10), PackageType.SPECIAL.value)

    def test_special_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), PackageType.SPECIAL.value)

    def test_rejected_exact_volume(self):
        self.assertEqual(sort(100, 100, 100, 25), PackageType.REJECTED.value)

    def test_rejected_multiple(self):
        self.assertEqual(sort(150, 150, 150, 25), PackageType.REJECTED.value)

    def test_edge_case_volume(self):
        self.assertEqual(sort(100, 100, 100, 19.9), PackageType.SPECIAL.value)

    def test_edge_case_dimension(self):
        self.assertEqual(sort(150, 10, 10, 15), PackageType.SPECIAL.value)
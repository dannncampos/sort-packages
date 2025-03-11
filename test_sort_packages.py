import unittest
from sort_packages import sort_packages


class TestSortPackagesFunction(unittest.TestCase):
    
    def test_standard_package(self) -> None:
        self.assertEqual(sort_packages(50, 50, 50, 10), "STANDARD")
    
    def test_bulky_package_max_volume(self) -> None:
        self.assertEqual(sort_packages(200, 100, 50, 10), "SPECIAL")

    def test_bulky_package_max_size(self) -> None:
        self.assertEqual(sort_packages(150, 50, 50, 10), "SPECIAL")
    
    def test_heavy_package(self) -> None:
        self.assertEqual(sort_packages(50, 50, 80, 25), "SPECIAL")
    
    def test_rejected_package_bulky_and_heavy(self) -> None:
        self.assertEqual(sort_packages(149, 149, 149, 25), "REJECTED")

    def test_rejected_package_max_size_and_heavy(self) -> None:
        self.assertEqual(sort_packages(150, 100, 100, 20), "REJECTED")
    
    def test_edge_cases(self) -> None:
        """ Exactly at the volume threshold """
        self.assertEqual(sort_packages(100, 100, 100, 19.9), "SPECIAL")
        """ Exactly at the heavy mass and dimension threshold """
        self.assertEqual(sort_packages(100, 100, 100, 20), "REJECTED")
        """ Exactly at the dimension threshold """
        self.assertEqual(sort_packages(150, 20, 20, 19.9), "SPECIAL")

if __name__ == '__main__':
    unittest.main()

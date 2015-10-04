import unittest
import sys
sys.path.insert(0,'..')

from cruncher import *

class CruncherTest (unittest.TestCase):
	def test_if_we_exist(self):
		self.assertTrue(cruncher(1))

	def test_assembler_assebles_correctly(self):
		self.assertEqual(assembler({1:3, 5:1}), 3115)




def main():
    unittest.main()

if __name__ == '__main__':
	main()
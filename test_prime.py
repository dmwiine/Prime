import unittest
from prime import Prime
class TestPrime(unittest.TestCase):
	def setUp(self):
		self.prime = Prime()

	def test_prime_returns_error_if_arg_is_not_positive_integer(self):
		self.assertRaises(TypeError, self.prime.prime, -10)

	def test_prime_returns_error_message_if_arg_is_string(self):
		self.assertRaises(TypeError, self.prime.prime, '10')

	def test_prime_returns_error_message_if_arg_is_float(self):
		self.assertRaises(TypeError, self.prime.prime, 10.0)

	def test_prime_returns_empty_list_when_arg_is_0(self):
		result = self.prime.prime(0)
		self.assertEqual([], result)

	def test_prime_returns_2_when_arg_is_2(self):
		result = self.prime.prime(2)
		self.assertEqual(2, result)


	if __name__ == '--main--':
		unittest.main()
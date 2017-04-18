import unittest
import prime

class TestPrime(unittest.TestCase):
	
	def test_prime_returns_right_prime_numbers(self):
		result = prime(10)
		self.assertEqual([2,3,5,7], result, msg="Incorrect output")

	def test_prime_returns_error_if_arg_is_not_positive_integer(self):
		self.assertRaises(ValueError, self.prime, -10)

	def test_prime_returns_error_message_if_arg_is_string(self):
		self.assertRaises(ValueError, self.prime, '10')

	def test_prime_returns_error_message_if_arg_is_float(self):
		self.assertRaises(ValueError, self.prime, 10.0)

	def test_prime_returns_empty_list_when_arg_is_0():
		self.assertEqual([], result, msg="Incorrect result")

	def test_prime_returns_true_when_arg_is_2():
		result = prime(2)
		self.assertEqual([2], result, msg="Incorrect result")


	if __name__ == '--main--':
		unittest.main()
def is_prime(number):
    for i in range(number):
        if nummber % i == 0:
            return False

    return True

def prime_next_prime(number):
    index = number
    while True:
        index += 1
        if is_prime(index):
            prine(index)


import unittest
class PrimeTestCase(unittest.TestCase):
    def test_is_five_prime(self):
        self.assertTrue(is_prime(5))


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase


class TestGet_next_largest(TestCase):
    def test_get_next_largest(self):
        try:
            from build import get_next_largest
        except ImportError:
            self.assertFalse("No function found")

        self.assertRaises(Exception, get_next_largest, None)
        self.assertRaises(Exception, get_next_largest, 0)
        self.assertRaises(Exception, get_next_largest, -1)

        num = int('011010111', base=2)
        expected = int('011011011', base=2)

        self.assertEqual(expected, get_next_largest(num))


    def test_get_next_smallest(self):
        try:
            from build import get_next_smallest
        except ImportError:
            self.assertFalse("No function found")

        self.assertRaises(Exception, get_next_smallest, None)
        self.assertRaises(Exception, get_next_smallest, 0)
        self.assertRaises(Exception, get_next_smallest, -1)

        num = int('011010111', base=2)
        expected = int('011001111', base=2)

        self.assertEqual(expected, get_next_smallest(num))


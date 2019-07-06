import unittest

from pydapt.exceptions import InvalidArgumentException
from pydapt.models import PyFlex


class FlexibleObjectTest(unittest.TestCase):

    def test_set_attributes_with_dict(self):
        test_dict = {
            'a': 1,
            'b': 2,
            'c': {
                'aa': 11,
                'bb': 22
            }
        }
        flexible_object = PyFlex(test_dict)

        self.assertEqual(flexible_object.a, 1)
        self.assertEqual(flexible_object.b, 2)
        self.assertEqual(flexible_object.c.aa, 11)
        self.assertEqual(flexible_object.c.bb, 22)
        self.assertTrue(isinstance(flexible_object.c, PyFlex))

    def test_set_attributes_with_kwargs(self):
        test_dict = {
            'a': 1,
            'b': 2,
            'c': {
                'aa': 11,
                'bb': 22
            }
        }
        flexible_object = PyFlex(test_dict, abc=100, abd=200)

        self.assertEqual(flexible_object.a, 1)
        self.assertEqual(flexible_object.b, 2)
        self.assertEqual(flexible_object.c.aa, 11)
        self.assertEqual(flexible_object.c.bb, 22)
        self.assertEqual(flexible_object.abc, 100)
        self.assertEqual(flexible_object.abd, 200)
        self.assertTrue(isinstance(flexible_object.c, PyFlex))

    def test_drop(self):
        test_dict = {
            'a': 1,
            'b': 2,
            'c': {
                'aa': 11,
                'bb': 22
            }
        }
        flexible_object = PyFlex(test_dict, abc=100, abd=200)

        self.assertEqual(flexible_object.a, 1)
        self.assertEqual(flexible_object.b, 2)
        self.assertEqual(flexible_object.c.aa, 11)
        self.assertEqual(flexible_object.c.bb, 22)
        self.assertEqual(flexible_object.abc, 100)
        self.assertEqual(flexible_object.abd, 200)
        self.assertTrue(isinstance(flexible_object.c, PyFlex))

        flexible_object.drop('c')
        flexible_object.drop('abc')
        flexible_object.drop('abd')
        self.assertIsNone(getattr(flexible_object, 'd', None))
        self.assertIsNone(getattr(flexible_object, 'abc', None))
        self.assertIsNone(getattr(flexible_object, 'abd', None))

    def test_str(self):
        test_dict = {
            'a': 1,
            'b': 2,
            'c': {
                'aa': 11,
                'bb': 22
            }
        }
        flexible_object = PyFlex(test_dict)
        self.assertEqual(str(flexible_object), "{'a': 1, 'b': 2, 'c': {'aa': 11, 'bb': 22}}")

    def test_invalid_exception(self):
        with self.assertRaises(InvalidArgumentException) as context:
            PyFlex(1)

        self.assertEqual(context.exception.message, 'Argument supplied to Flexible Object is not of type: <dict>')
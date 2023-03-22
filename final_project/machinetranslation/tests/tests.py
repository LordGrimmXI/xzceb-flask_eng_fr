import unittest
from translator import frenchToEnglish, englishToFrench

class TestTranslator1(unittest.TestCase):
    def test_simple_translation1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(None), '')
        
class TestTranslator2(unittest.TestCase):
    def test_simple_translation2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(None), '')

if __name__ == '__main__':
    unittest.main()

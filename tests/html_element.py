import unittest
from objects import HTMLElement

class TestHTMLElement(unittest.TestCase):

    def test_base_element(self):
        self.assertEqual(
            str(HTMLElement(tag="h1")),
            "<h1 ></h1>"
        )
        self.assertEqual(
            str(HTMLElement(tag="h1",
                            innerHTML="test")),
            "<h1 >test</h1>"
        )
        self.assertEqual(
            str(HTMLElement(tag="h1",
                            style="test")),
            "<h1 style = \"test\"></h1>"
        )
        self.assertEqual(
            str(HTMLElement(tag="h1",
                            innerHTML="test",
                            style="test")),
            "<h1 style = \"test\">test</h1>"
        )
        with self.assertRaises(TypeError):
            HTMLElement()

if __name__ == '__main__':
    unittest.main()
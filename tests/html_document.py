import unittest
from objects import HTMLDocument
from objects import HTMLElement

class TestHTMLDocument(unittest.TestCase):

    def test_base_element(self):
        create_test_case = lambda head, body: f"""<!DOCTYPE html>
<html>
<head>{"".join([str(e) for e in head])}</head>
<body>{"".join([str(e) for e in body])}</body>
</html>"""

        self.assertEqual(
            str(HTMLDocument()),
            create_test_case([],[])
        )
        self.assertEqual(
            str(HTMLDocument(
                body=[HTMLElement(tag="h1")])),
            create_test_case(
                [],
                [HTMLElement(tag="h1")])
        )
        self.assertEqual(
            str(HTMLDocument(
                head=[HTMLElement(tag="h1")])),
            create_test_case(
                [HTMLElement(tag="h1")],
                [])
        )
        self.assertEqual(
            str(HTMLDocument(
                head=[HTMLElement(tag="h1")],
                body=[HTMLElement(tag="h1")])),
            create_test_case(
                [HTMLElement(tag="h1")],
                [HTMLElement(tag="h1")])
        )

if __name__ == '__main__':
    unittest.main()
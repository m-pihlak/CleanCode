from objects import HTMLElement
from typing import List

class HTMLDocument:

    def __init__(self,
                 head: List[HTMLElement] = [],
                 body: List[HTMLElement] = []):
        self.__head = head
        self.__body = body

    def __repr__(self):
        return f"""<!DOCTYPE html>
<html>
<head>{"".join([str(e) for e in self.__head])}</head>
<body>{"".join([str(e) for e in self.__body])}</body>
</html>"""
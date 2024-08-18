class HTMLElement:

    def __init__(self, 
                 tag: str,
                 innerHTML: str = ""):
        self.tag: str = tag
        self.innerHTML = innerHTML
    

    def __str__(self):
        return f"<{self.tag}>{self.innerHTML}</{self.tag}>"
from objects import HTMLDocument, HTMLElement

def create_base_website():
    return HTMLDocument(body = [
            HTMLElement(
                    tag="h1", 
                    innerHTML="Hey",
                    style="color: green;",
                    ),
            HTMLElement(
                    tag="h2", 
                    innerHTML="How is it going?",
                    style="color: cyan;",
                    ),
        ])
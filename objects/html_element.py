class HTMLElement:

    def __init__(self, 
                 tag: str,
                 innerHTML: str = "",
                 **kwargs):
        self.__tag: str = tag
        self.__innerHTML: str = innerHTML
        self.__arguments: dict = kwargs
    
    """
    Returns argument key-value pairs as space separated
    strings in the form: key = "value"
    Example:
        argument:
            key: "style"
            value: "color: cyan;"
        string:
            "style = \"color: cyan;\""
    """
    def args(self):
        return " ".join([
            f"{key} = \"{value}\""
            for key, value in self.__arguments.items()
        ])
    
    def __str__(self):
        return f"<{self.__tag} {self.args()}>{self.__innerHTML}</{self.__tag}>"
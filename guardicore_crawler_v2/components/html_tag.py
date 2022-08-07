class HTMLTag(object):
    """
        Class to interface use of HTML tags
    """

    def __init__(self, tag):
        self.tag = tag
    
    def get_attribute(self, attribute):
        return self.tag.get(attribute)

    def get_text(self):
        return self.tag.text
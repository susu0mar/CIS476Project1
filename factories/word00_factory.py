from .abstract_factory import abstractFactory
from components import word00Button, word00Textbox, word00Panel


class word00_factory(abstractFactory):
    _instance = None #have class level variable For Singleton
    _instance_count = 0 #have class level variable to keep track of count of instances!

    def __new__(cls):
        
        if cls._instance_count >= 2:
            print("Warning: Word00Factory cannot be instantiated more than twice.\n")
            return None  # Prevents creation of a new instance

        if cls._instance is None:
            cls._instance = super(word00_factory, cls).__new__(cls)
        
        cls._instance_count += 1
        return cls._instance
    
    def createButton(self):

        return word00Button()
    
    def createTextbox(self):

        return word00Textbox()
    
    def createPanel(self):
        
        return word00Panel()



from .abstract_factory import abstractFactory
from components import word10Button, word10Textbox, word10Panel


class word10_factory(abstractFactory):
    _instance = None #have class level variable For Singleton
    _instance_count = 0 #have class level variable to keep track of count of instances!

    def __new__(cls):
        
        if cls._instance_count >= 2:
            print("Warning: Word10Factory cannot be instantiated more than twice.\n")
            return None  # Prevents creation of a new instance

        if cls._instance is None:
            cls._instance = super(word10_factory, cls).__new__(cls)
        
        cls._instance_count += 1
        return cls._instance
    
    def createButton(self):

        return word10Button()
    
    def createTextbox(self):

        return word10Textbox()
    
    def createPanel(self):
        
        return word10Panel()



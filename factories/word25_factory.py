from .abstract_factory import abstractFactory
from components import word25Button, word25Textbox, word25Panel


class word25_factory(abstractFactory):
    _instance = None #have class level variable For Singleton
    _instance_count = 0 #have class level variable to keep track of count of instances!

    def __new__(cls):
        
        if cls._instance_count >= 2:
            print("Warning: Word25Factory cannot be instantiated more than twice.")
            return None  # Prevents creation of a new instance

        if cls._instance is None:
            cls._instance = super(word25_factory, cls).__new__(cls)
        
        cls._instance_count += 1
        return cls._instance
    
    def createButton(self):

        return word25Button()
    
    def createTextbox(self):

        return word25Textbox()
    
    def createPanel(self):
        
        return word25Panel()



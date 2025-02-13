from abc import ABC, abstractmethod

class abstract_factory(ABC):

    """Abstract class to create the different factories off of. Has methods to create the different UI components"""

    @abstractmethod
    def createButton(self):
        pass #abstract method so dont implement here!
    
    @abstractmethod
    def createPanel(self):
        pass #abstract method so dont implement here!
    
    @abstractmethod
    def createTextbox(self):
        pass #abstract method so dont implement here!


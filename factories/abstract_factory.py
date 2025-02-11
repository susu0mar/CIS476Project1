from abc import ABC, abstractmethod

class abstract_factory(ABC):

    @abstractmethod
    def createButton():
        pass #abstract method so dont implement here!
    
    @abstractmethod
    def createPanel():
        pass #abstract method so dont implement here!
    
    @abstractmethod
    def createTextbox():
        pass #abstract method so dont implement here!
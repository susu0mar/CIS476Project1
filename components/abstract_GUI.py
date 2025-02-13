from abc import ABC, abstractmethod

class abstract_GUI(ABC):
    
    @abstractmethod
    def testComponent(self):
        pass #not defining here since its abstract
from abc import ABC, abstractmethod

class AbstractGUI(ABC):
    
    @abstractmethod
    def testComponent(self):
        pass #not defining here since its abstract
from abc import ABC, abstractmethod

class AbstractGUI(ABC):
    """Abstract GUI component- used to create the concrete components"""

    @abstractmethod
    def testComponent(self):
        pass #not defining here since its abstract
from noinput import ContinueNoInputBehavior

class SSVMIR:
    """
    This class represents the SSVM Intermediate Representation.
    It abstracts iOS/iPadOS/macOS version related details and provides a high level interface.
    The compiler will take an instance of this class and compile it into a .plist file.
    """

    def __init__(self) -> None :
        self._actions = []
        self._name = ""
        self._no_input_behavior = ContinueNoInputBehavior()

    @property
    def name(self):
        """
        This is the name of the Shortcut. It will be displayed in the Shortcuts app.
        This propery modifies the WFWorkflowName key in the compiled .plist file.
        """
        return self._name

    @property.setter
    def name(self, name):
        self._name = name

    @property
    def no_input_behavior(self):
        """
        No input behavior is what happens when the Shortcut is run without input.
        This property modifies the WFWorkflowNoInputBehavior key in the compiled .plist file.
        """
        return self._no_input_behavior
    
    @property.setter
    def no_input_behavior(self, behavior):
        self._no_input_behavior = behavior

    def save(self, path):
        raise NotImplementedError()
    
    @staticmethod
    def load(self, path):
        raise NotImplementedError()
    
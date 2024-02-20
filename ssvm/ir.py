from .noinput import ContinueNoInputBehavior

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
        self._has_input_variables = False
        self._actions = []

    @property
    def name(self):
        """
        This is the name of the Shortcut. It will be displayed in the Shortcuts app.
        This propery modifies the WFWorkflowName key in the compiled .plist file.
        """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def has_input_variables(self):
        """
        This property is True if the Shortcut has an input variable.
        """
        return self._has_input_variables
    
    @has_input_variables.setter
    def has_input_variables(self, has_input):
        self._has_input_variables = has_input 

    @property
    def no_input_behavior(self):
        """
        No input behavior is what happens when the Shortcut is run without input.
        This property modifies the WFWorkflowNoInputBehavior key in the compiled .plist file.
        """
        return self._no_input_behavior
    
    @no_input_behavior.setter
    def no_input_behavior(self, behavior):
        self._no_input_behavior = behavior

    @property
    def actions(self):
        """
        This is a list of actions in the Shortcut.
        This property modifies the WFWorkflowActions key in the compiled .plist file.
        """
        return self._actions
    
    def save(self, path):
        raise NotImplementedError()
    
    @staticmethod
    def load(self, path):
        raise NotImplementedError()
    
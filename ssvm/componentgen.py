import abc

class ShortcutComponentGenerator(metaclass=abc.ABCMeta):
    """
    Generates a part of a plist file for a shortcut.
    This will serve as an interface for all the components of SSVM IR to generate their respective plist parts. 
    
    For example:
    - NoInputBehavior(ShortcutComponentGenerator) will generate the value for WFWorkflowNoInputBehavior key.
    """
    def __init__(self):
        pass

    def componentgen(self):
        raise NotImplementedError(
            self.__class__.__name__ + " did not implement componentgen()\n" \
            "This functionality has not been implemented in SSVM yet. You can create an issue on the GitHub repository to request this feature."
        )
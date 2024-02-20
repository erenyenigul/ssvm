from .componentgen import ShortcutComponentGenerator

class NoInputBehavior(ShortcutComponentGenerator):
    """
    This class is used to define the behavior when no input is provided.
    The existing behaviors in different versions vary, but it is possible to implement missing ones using actions
    """
    def __init__(self, name) -> None:
        self._name = name

class ContinueNoInputBehavior(NoInputBehavior):
    """
    This behavior will continue the workflow without input.
    This is the default behavior. Whenever this behavior is set, the compiled .plist file will not contain the WFWorkflowNoInputBehavior key.
    """
    def __init__(self) -> None:
        super().__init__(None)
    
    def componentgen(self):
        return ""

class ShowErrorNoInputBehavior(NoInputBehavior):
    def __init__(self, error) -> None:
        super().__init__("WFWorkflowNoInputBehaviorShowError")
        self._error = error
    
    def componentgen(self):
        return {
            "Name": self._name,
            "Parameters": {
                "Error": self._error
            }
        }

class AskForInputNoInputBehavior(NoInputBehavior):
    def __init__(self, prompt) -> None:
        super().__init__("WFWorkflowNoInputBehaviorAskForInput")
        self._prompt = prompt

    def componentgen(self):
        return {
            "Name": self._name,
            "Parameters": {
            }
        }

class GetClipboardNoInputBehavior(NoInputBehavior):
    def __init__(self) -> None:
        super().__init__("WFWorkflowNoInputBehaviorGetClipboard")
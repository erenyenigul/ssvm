class NoInputBehavior:
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

class ShowErrorNoInputBehavior(NoInputBehavior):
    def __init__(self) -> None:
        super().__init__("WFWorkflowNoInputBehaviorShowError")

class AskForInputNoInputBehavior(NoInputBehavior):
    def __init__(self) -> None:
        super().__init__("WFWorkflowNoInputBehaviorAskForInput")

class GetClipboardNoInputBehavior(NoInputBehavior):
    def __init__(self) -> None:
        super().__init__("WFWorkflowNoInputBehaviorGetClipboard")
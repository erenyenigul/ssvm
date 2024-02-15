class NoInputBehaviour:
    """
    This class is used to define the behaviour when no input is provided.
    The existing behaviours in different versions vary, but it is possible to implement missing ones using actions
    """
    def __init__(self, name) -> None:
        self._name = name

class ContinueNoInputBehaviour(NoInputBehaviour):
    """
    This behaviour will continue the workflow without input.
    This is the default behaviour. Whenever this behaviour is set, the compiled .plist file will not contain the WFWorkflowNoInputBehaviour key.
    """
    def __init__(self) -> None:
        super().__init__(None)

class ShowErrorNoInputBehaviour(NoInputBehaviour):
    def __init__(self) -> None:
        super().__init__("WFWorkflowNoInputBehaviourShowError")

class AskForInputNoInputBehaviour(NoInputBehaviour):
    def __init__(self) -> None:
        super().__init__("WFWorkflowNoInputBehaviourAskForInput")

class GetClipboardNoInputBehaviour(NoInputBehaviour):
    def __init__(self) -> None:
        super().__init__("WFWorkflowNoInputBehaviourGetClipboard")
import plistlib, json
from .ir import SSVMIR
import pathlib

class Compiler:
    """
    Compiles SSVM IR to a Shortcut file.
    """

    def __init__(self, target='ios17') -> None:
        self.target = target

    def compile(self, ir: SSVMIR, out_path: str = None):
        """Compiles the SSVM IR to a shortcut file.
        """

        # This part exists since not all parts of the Shortcut file are implemented in SSVM IR.
        parent_dir = pathlib.Path(__file__).parent.resolve()
        template_path = parent_dir / "template/a-shortcut.json" 

        with open(template_path, "r") as f:
            plist = json.load(f)

        # Name
        plist['WFWorkflowName'] = ir.name

        # Input Variables
        plist['WFWorkflowHasShortcutInputVariables'] = ir.has_input_variables
        
        # No Input Behavior
        plist['WFWorkflowNoInputBehavior'] = ir.no_input_behavior.componentgen()
        
        #Actions
        plist['WFWorkflowActions'] = []
        for action in ir.actions:
            plist['WFWorkflowActions'] += action.componentgen()

        if not out_path:
            out_path = ir.name + ".shortcut"

        with open(out_path, "wb") as f:
            plistlib.dump(plist, f)
import plistlib
from ir import SSVMIR

class Compiler:
    """
    Compiles SSVM IR to a Shortcut file.
    """

    def __init__(self, target='ios17') -> None:
        self.target = target

    def compile(self, out_path, ir: SSVMIR):
        
        plist = {
            'WFWorkflowClientVersion': '2106.0.3',
            'WFWorkflowHasOutputFallback': False,
            'WFWorkflowHasShortcutInputVariables': False,
            'WFWorkflowIcon': {
                'WFWorkflowIconGlyphNumber': 59740,
                'WFWorkflowIconStartColor': 4282601983,
            },
            'WFWorkflowImportQuestions': [],
            'WFWorkflowInputContentItemClasses': [
                'WFFolderContentItem', 'WFLocationContentItem', 'WFPDFContentItem', 'WFStringContentItem',
                'WFNumberContentItem', 'WFEmailAddressContentItem', 'WFGenericFileContentItem',
                'WFPhoneNumberContentItem', 'WFRichTextContentItem', 'WFSafariWebPageContentItem',
                'WFArticleContentItem', 'WFContactContentItem', 'WFiTunesProductContentItem',
                'WFAVAssetContentItem', 'WFAppStoreAppContentItem', 'WFDateContentItem',
                'WFImageContentItem', 'WFDCMapsLinkContentItem', 'WFURLContentItem'
            ],
            'WFWorkflowMinimumClientVersion': 900,
            'WFWorkflowMinimumClientVersionString': '900',
            'WFWorkflowOutputContentItemClasses': [],
            'WFWorkflowTypes': [],
            'WFWorkflowNoInputBehavior': {
                'Name': 'WFWorkflowNoInputBehaviorShowError',
                'Parameters': {
                    'Error': 'You must provide a program to run.'
                }
            },
            'WFWorkflowName': ir.name,
            'WFWorkflowActions': [],
        }
        
        for action in ir.actions:
            plist['WFWorkflowActions'].append({
                'WFWorkflowActionIdentifier': action.identifier
            })

        with open(out_path, "wb") as f:
            plistlib.dump(plist, f)
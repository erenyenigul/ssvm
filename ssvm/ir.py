from action import Action
import os

class SSVMIR:
     
    def __init__(self) -> None :
        self.actions = []
        self.name = ""

    def save(self, path):
        with open(path, "w") as f:
            f.write("(\n")
            f.write("\tversion 17.0\n")
            f.write("\tactions\n")
            for action in self.actions:
                    f.write(f"\t({action.identifier})\n")
            
            f.write(")\n")

    def action(self, identifier):
        action = Action(identifier)
        self.actions.append(action)
        return action
    
    def no_input_behavior(self, name, parameters):
        self.no_input_behavior = {
            'Name': name,
            'Parameters': parameters
        }
        
        return self.no_input_behavior
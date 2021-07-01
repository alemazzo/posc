
class Operation:

    def __init__(self, command: str):
        self.command = command

    def execute(self, depth: int):
        print("  "*depth + f"Executing operation : {self.command}")

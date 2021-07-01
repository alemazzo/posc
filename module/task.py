from module.operation import Operation


class Task:

    def __init__(self, name: str, operations: list, requirements: list = []):
        self.name = name
        self.requirements = requirements
        self.operations = operations

    def _executeRequirements(self, depth=1):
        if len(self.requirements) == 0:
            return
        print("  "*depth + f"Executing requirements for Task : {self.name}")
        for requirement in self.requirements:
            requirement.executeTask(depth + 1)

    def executeTask(self, depth=1):
        print("  "*depth + f"Task: {self.name}")
        self._executeRequirements(depth + 1)
        print("  "*(depth + 1) + f"Executing Task: {self.name}")
        for operation in self.operations:
            operation.execute(depth + 2)

import json
from posc import Operation, Task

print("Loading tasks...")
configuration = dict()
with open('setup.json') as conf:
    configuration = json.loads(conf.read())
print("Configuration loaded")


def getOperations(operations: list):
    # Get list of operations from the list of string
    return [Operation(operation) for operation in operations]


def getRequirements(requirements: list):
    # Get list of requirements task from the list of string
    return [getTask(requirement) for requirement in requirements]


def getTask(taskConfig):
    requirement_tasks = []
    if "requirements" in taskConfig:
        requirements = taskConfig["requirements"]
        requirement_tasks = [getTask(req) for req in requirements]
    return Task(taskConfig["name"], getOperations(taskConfig["operations"]), requirement_tasks)


tasks = [getTask(taskConfig) for taskConfig in configuration["tasks"]]
for task in tasks:
    print("\n" + "-" * 30)
    task.executeTask()

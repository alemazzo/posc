import json

print("Loading tasks...")
configuration = dict()
with open('setup.json') as conf:
    configuration = json.loads(conf.read())
print("Configuration loaded")

INSTALL_KEYWORD = "install"
COMMAND_KEYWORD = "command"
ARGUMENTS_KEYWORD = "arguments"
REPLACE_KEYWORD = "${}"

tasks = configuration["tasks"]
for task_name in tasks:
    print(f"Task: {task_name}")
    task = tasks[task_name]

    if INSTALL_KEYWORD in task:
        install = task[INSTALL_KEYWORD]
        print(f"\tinstall : {install}")

    command = task[COMMAND_KEYWORD]
    print(f"\tcommand : {command}")

    arguments = task[ARGUMENTS_KEYWORD]
    for arg in arguments:
        exec_command = command.replace(REPLACE_KEYWORD, arg)
        print(f"\t\t{exec_command}")

from mythic_container.MythicCommandBase import *
import json


class SleepArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = [
            CommandParameter(
                name="sleep",
                type=ParameterType.Number,
                description="Adjust the callback interval in seconds",
            ),
        ]

    async def parse_arguments(self):
        self.load_args_from_json_string(self.command_line)


class SleepCommand(CommandBase):
    cmd = "sleep"
    needs_admin = False
    help_cmd = 'sleep {"sleep":10}'
    description = "Change the sleep interval for an agent"
    version = 1
    author = "@xorrior"
    argument_class = SleepArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        task.display_params = str(task.args.get_arg("sleep")) + "s"
        return task

    async def process_response(self, task: PTTaskMessageAllData, response: any) -> PTTaskProcessResponseMessageResponse:
        resp = PTTaskProcessResponseMessageResponse(TaskID=task.Task.ID, Success=True)
        return resp

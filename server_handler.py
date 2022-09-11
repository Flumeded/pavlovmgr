import subprocess
import re
import constant
import exceptions


class ScwExecutor:
    @staticmethod
    def execute(command, server_id):
        result = subprocess.run(f"scw instance server {command} {server_id}", shell=True,
                                stdout=subprocess.PIPE,
                                text=True, check=True)
        return result


class Server:
    def __init__(self, server_id):
        self.id = server_id
        self.status = Server.__get_status(self)
        if self.status == constant.ServerStatus.INCORRECT:
            raise exceptions.ServerStatusError("Server status not ON or OFF")

    def get_status(self) -> constant.ServerStatus:
        return self.status

    def is_running(self):
        server_status = self.get_status()
        return server_status == constant.ServerStatus.RUNNING

    def is_stopped(self):
        server_status = self.get_status()
        return server_status == constant.ServerStatus.ARCHIVED

    def start(self):
        if Server.is_running(self):
            print(constant.Messages.server_is_running)
        else:
            ScwExecutor.execute(constant.Commands.start, constant.SERVER_ID)
            ScwExecutor.execute(constant.Commands.wait, constant.SERVER_ID)
            print(constant.Messages.server_has_started)

    def stop(self):
        if Server.is_stopped(self):
            print(constant.Messages.server_is_stopped)
        else:
            ScwExecutor.execute(constant.Commands.stop, constant.SERVER_ID)
            ScwExecutor.execute(constant.Commands.wait, constant.SERVER_ID)
            print(constant.Messages.server_has_stopped)

    def __get_status(self):
        output = ScwExecutor.execute(constant.Commands.get, self.id)
        try:
            server_status = re.findall(r"(?<=\sState)\s+(archived|running)", output.stdout)[0]
            match server_status:
                case "archived":
                    return constant.ServerStatus.ARCHIVED
                case "running":
                    return constant.ServerStatus.RUNNING
                case _:
                    return constant.ServerStatus.INCORRECT

        except subprocess.CalledProcessError as err:
            print(f'Error command execution: {str(err)}')
            raise err

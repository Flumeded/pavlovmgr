from enum import Enum, auto

SERVER_ID = '076a3d44-d44e-4026-a680-42c629066295'


class Commands:
    start = "start"
    wait = "wait"
    stop = "stop"
    get = "get"


class ServerStatus(Enum):
    ARCHIVED = auto()
    RUNNING = auto()
    INCORRECT = auto()


class Messages:
    server_is_running = "Server is already running"
    server_is_stopped = "Server is already stopped"
    server_is_starting = "Server is starting..."
    server_has_started = "Server has been successfully started"
    server_is_stopping = "Server is stopping..."
    server_has_stopped = "Server has been successfully stopped"
    server_incorrect_state = "Server state not ON or OFF"
    enter_server_zone = "Please enter where instance is locate.\n(e.g fr-par-1, fr-par-2, nl-ams-1, pl-waw-1):\n"
    enter_server_id = "Please enter server ID:\n"
    enter_server_api = "Please enter Scaleway API key:\n"

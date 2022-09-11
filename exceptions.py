class Error(Exception):
    pass


class ServerStatusError(Error):
    """Server statis not ON or OFF"""
    pass

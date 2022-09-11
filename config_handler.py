import json
import constant
import os.path


class Config(object):
    def __init__(self, server_zone: str, server_id: str, api_key: str):
        self.server_zone = server_zone
        self.server_id = server_id
        self.api_key = api_key

    def __str__(self):
        return f"Server Zone = {self.server_zone}, Server ID= {self.server_id}, API Key = {self.api_key}"


class ConfigManager:

    def __init__(self):
        pass

    @staticmethod
    def read_config_from_file(file_path):
        file = open(file_path, "r")
        text = file.read()
        return Config(**json.loads(text))

    @staticmethod
    def create_config_from_parameters(server_zone: str, server_id: str, api_key: str) -> Config:
        return Config(server_zone, server_id, api_key)

    @staticmethod
    def create_config_from_input() -> Config:
        server_zone = input(constant.Messages.enter_server_zone)
        server_id = input(constant.Messages.enter_server_id)
        api_key = input(constant.Messages.enter_server_api)
        config = Config(server_zone, server_id, api_key)
        return config

    @staticmethod
    def save_config_to_file(file_path: str, config: Config):
        json_data = json.dumps(config.__dict__)
        file = open(file_path, "w")
        file.write(json_data)
        file.close()

    @staticmethod
    def create_config_if_not_exists(file_path):
        if os.path.exists(file_path):
            return ConfigManager.read_config_from_file(file_path)
        else:
            config = ConfigManager.create_config_from_input()
            ConfigManager.save_config_to_file(file_path, config)
            return config

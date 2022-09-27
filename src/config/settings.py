import json
import yaml
import os


class Settings:
    def __init__(self) -> None:
        env: str = os.getenv("NODE_ENV", "dev")
        app_config: dict = yaml.safe_load(open("src/config/app.yml")) or dict()
        env_config: dict = yaml.safe_load(open(f"src/config/app-{env}.yml")) or dict()

        app_config.update(env_config)
        self.configs = app_config

    def server_port(self):
        return self.configs["port"]


settings = Settings()

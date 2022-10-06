import os

import yaml


class Settings:
    """
        `NODE_ENV` is a variable used to distinguish between environments.
        For example, when set to `dev`, `app.yml` and `app-dev.yml` will be loaded
    """
    def __init__(self) -> None:
        env: str = os.getenv("NODE_ENV", "dev")
        app_config: dict = yaml.safe_load(open("src/config/app.yml")) or dict()
        env_config: dict = yaml.safe_load(open(f"src/config/app-{env}.yml")) or dict()

        app_config.update(env_config)
        self.configs = app_config

    def server_port(self) -> int:
        return self.configs["port"]


settings = Settings()

from loguru import logger

logger.add("logs/flask-template.log", level="INFO", rotation="1 day")

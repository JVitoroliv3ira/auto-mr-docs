import logging
import sys

class LoggerConfig:
    @staticmethod
    def get_logger(name: str = 'auto-mr-docs') -> logging.Logger:
        logger = logging.getLogger(name)
        
        if logger.hasHandlers():
            return logger
        
        logger.setLevel(logging.DEBUG)
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        console_handler.setFormatter(formatter)
        console_handler.stream.reconfigure(encoding="utf-8")
        logger.addHandler(console_handler)
        
        return logger

        
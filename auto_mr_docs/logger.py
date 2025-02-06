import logging
import sys

from config import Config

class LoggerConfig:
    
    @staticmethod
    def get_logger(name: str = "auto-mr-docs") -> logging.Logger:
        logger = logging.getLogger(name)
        
        if logger.hasHandlers():
            return logger
        
        debug_mode = Config.DEBUG.lower() == "true"
        logger.setLevel(logging.DEBUG if debug_mode else logging.INFO)
        
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
        console_handler.setFormatter(formatter)
        console_handler.stream.reconfigure(encoding="utf-8")
        logger.addHandler(console_handler)
        
        return logger

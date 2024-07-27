import logging
import os
import platform

def get_log_file_path():
    if platform.system() == "Windows":
        log_dir = r"C:\Users\Public"
    else:  # Assuming Linux/Unix
        log_dir = "/var/log"
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    return os.path.join(log_dir, "myapp.log")

def setup_logger():
    log_file_path = get_log_file_path()
    
    logger = logging.getLogger('myapp')
    logger.setLevel(logging.DEBUG)
    
    # Create file handler which logs even debug messages
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.DEBUG)
    
    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    
    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # Add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger

def log_debug(message):
    logger = setup_logger()
    logger.debug(message)

def log_info(message):
    logger = setup_logger()
    logger.info(message)

def log_warning(message):
    logger = setup_logger()
    logger.warning(message)

def log_error(message):
    logger = setup_logger()
    logger.error(message)

def log_critical(message):
    logger = setup_logger()
    logger.critical(message)

